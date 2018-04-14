import os
import glob
import re
import json
import certifi
import csv
import time
import elasticsearch as es
import elasticsearch_dsl as edsl
from create_hedis_perc_queries import create_query
from config import QUERIES_DOCTYPE, CHART_DOCTYPE, HEDIS_INDEX_NAME

def connect(url):
    """ Connect to an Elasticsearch cluster.  Supports SSL connections. """
    if 'localhost' in url:
        conn = edsl.connections.connections.create_connection(hosts=[url])
    else:
        auth = re.search('https\:\/\/(.*)\@', url).group(1).split(':')
        host = url.replace('https://%s:%s@' % (auth[0], auth[1]), '')

        # Connect to cluster over SSL using auth for best security:
        es_header = [{
            'host': host,
            'port': 443,
            'use_ssl': True,
            'http_auth': (auth[0], auth[1]),
            'verify_certs': True,
            'ca_certs': certifi.where()
        }]
        conn = edsl.connections.connections.create_connection(hosts=es_header)
    return conn

def index_queries(conn, index_name, queries_doctype, queries):
    bulk_metadata = {
        '_index': index_name,
        '_type': queries_doctype,}
    for query in queries:
        query.update(bulk_metadata)
    count, errors = es.helpers.bulk(conn, queries)
    return count, errors

def add_mappings(conn, index_name, queries_doctype,
                 chart_doctype):
    """ Add document mappings to the index.  This creates two mappings -
    one for the queries we'll be indexing to percolate against, and a second
    for preprocessing the chart documents we want to percolate.
    This would be where any special options should be applied to use different
    highlighters, special analyzers, etc. """
    # Add two mappings to the index.  One for the queries we'll index,
    # and one for the documents that will be percolated.
    # query_mapping = edsl.Mapping(queries_doctype)
    # query_mapping.field('query', 'percolator')
    # query_mapping.field('type', type='keyword')
    # query_mapping.field('code', type='keyword')
    # query_mapping.save(index_name)

    # NOTE: We have to use this lower-level method due to the fact that the
    # elasticsearch_dsl library doesn't yet support percolator Field type
    percolator_mapping = {
        'properties': {
            'query': {
                'type': 'percolator'
            }
        }
    }
    conn.indices.put_mapping(
        doc_type=queries_doctype,
        body=percolator_mapping,
        index=index_name,
    )

    # Add the map for charts that will be percolated, so we know
    # how to preprocess them before searching
    chart_mapping = edsl.Mapping(chart_doctype)
    # chart_mapping.field('chart_id', 'keyword')
    chart_mapping.field('DOC', 'text')
    chart_mapping.save(index_name)


def create_index(index_name):
    """ Creates a new index, destroying any existing index with the same
        name. """
    index = edsl.Index(index_name)
    index.settings(number_of_shards=1)
    if index.exists():
        index.delete()
        print('old index deleted')
    index.create()
    return index

# NOTE: program Start's here
if __name__ == '__main__':
    import sys
    from datetime import datetime

    queries_doctype = QUERIES_DOCTYPE
    chart_doctype = CHART_DOCTYPE
    index1_name = HEDIS_INDEX_NAME
    #index2_name = MEASURES_INDEX_NAME

    claims_queries = []
    with open(r'HEDIS_searchterm_V1.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        # [uid , 'OriginalClaimID', 'RenderingProviderLastName', 'RenderingProviderFirstName', 'FromDate']
        for row in data:
            claims_queries.append(create_query(row))

    es_url = 'http://localhost:9200'
    conn = connect(es_url)
    info = conn.info()
    index = create_index(index1_name)

    add_mappings(conn, index1_name, queries_doctype, chart_doctype)

    def es_hit(res):
        try:
            ct, errors = index_queries(conn, index1_name, queries_doctype, res)
            return True
        except:
            return None

    if len(claims_queries) >=1 :
        print('Total {0} queries'.format(len(claims_queries)))
        response = es_hit(claims_queries)

        while not response:
            print('had error going to try again..')
            time.sleep(2)
            response = es_hit(claims_queries)

        print('Successfully indexed queries -- {0}'.format(response))