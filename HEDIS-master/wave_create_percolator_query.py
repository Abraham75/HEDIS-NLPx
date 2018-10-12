from utils import alter_date_format


def create_exclusion_query(row):
    # {'uid': row[0], 'OriginalClaimID': row[1],
    #  'RenderingProviderLastName': row[2], 'RenderingProviderFirstName': row[3],
    #  'FromDate': row[4]}

    query = {
            '_id': row[0],
            'QueryID': row[1],
            'searchTerm':row[2],
            'Instructions': row[5],
            'Measure': row[6],
            'QueryType': row[7],
            'Notes': row[8],
            'highlight': {
                    'pre_tags': ['~~'],
                    'post_tags': ['~~'],
                    'fields': {
                            "DOC": {
                                    'type': 'plain',
                                    'fragment_size': 150,
                                    'number_of_fragments': 0
                                    }
                            }
                        },
             'query': {
					 'match_phrase': {"DOC": {"query": row[2], "slop": row[4]}}
                 }
             }
    return query
	
	#,"slop":row[3]
def create_measures_query(row):
    # {'uid': row[0], 'OriginalClaimID': row[1],
    #  'RenderingProviderLastName': row[2], 'RenderingProviderFirstName': row[3],
    #  'FromDate': row[4]}

    query = {
            '_id': row[0],
            'QueryID': row[1],
            'searchTerm':row[2],
            'Instructions': row[5],
            'Measure': row[6],
            'SubMeasure': row[7],
            'QueryType': row[8],
            'Notes': row[9],
            'highlight': {
                    'pre_tags': ['~~'],
                    'post_tags': ['~~'],
                    'fields': {
                            "DOC": {
                                    'type': 'plain',
                                    'fragment_size': 150,
                                    'number_of_fragments': 0
                                    }
                            }
                        },
             'query': {
					 'match_phrase': {"DOC": {"query": row[2], "slop": row[4]}}
                 }
             }
             
    return query
