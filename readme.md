
# WaveHedis: Automated HEDIS Term Extraction Framework

**Intelligent NLP Pipeline for Healthcare Quality Metrics**

---

##  Overview

WaveHedis is a sophisticated Natural Language Processing toolkit developed to streamline the extraction of HEDIS (Healthcare Effectiveness Data and Information Set) quality metric terms from structured and unstructured data sources. Designed with semantic precision, it enables:

- High-throughput identification of HEDIS measure terminology
- Customizable filtering and exclusion logic
- Integration with search engine indexing (e.g., Elasticsearch Percolators)
- Support for both CSV and XML inputs through extensible pipelines

This repository reflects rigorous health informatics design, ontology-informed keyword modeling, and Python-centric modularity for enterprise-grade workflows.

---

##  Features

- **CSV-Based Term Extraction**: Integrates HEDIS search term sheets, exclusion lists, and measure-specific keyword mappings.
- **Multi-Source Parsers**: Includes XML and JSON preprocessing with flexible pipelines (`xml_to_text.py`, `loads_xml_to_json.py`).
- **Indexing Support**: Scripts like `index_percolator_from_csv.py` facilitate integrating HEDIS terms into search index systems (ElasticSearch, Solr).
- **Filtering Mechanics**: Enables exclusion of false positives with configurable logic (`exclusions.py`, `bcs_filter.py`, `cdc_filter.py`, `aba_filter.py`).
- **Configurable Architecture**: Central config management via `config.py`, with utility operations supported by `utils.py`.
- **Core Engine**: Orchestrated through `main.py`, which manages extraction flow—input ingestion, term lookup, filtering, and output generation.

---

##  Installation

```bash
git clone https://github.com/Abraham75/WaveHedis.git
cd WaveHedis
pip install -r requirements.txt
````

---

## Usage Examples

Run full extraction pipeline:

```bash
python main.py --input-dir ./queries --output-dir ./results
```

Index terms into a Percolator service:

```bash
python index_percolator_from_csv.py --terms HEDIS_searchterm_V1.csv
```

Customize exclusion filters or search term scopes by editing the relevant CSVs or filter modules.

---

## Science-Driven Approach

WaveHedis embodies a layered NLP strategy aligned with semantic interoperability and HEDIS measurement standards:

1. **Data Standardization**: Utilizes controlled vocabularies (HEDIS measure codes, SNOMED mappings).
2. **Modular Pipeline Design**: Separates ingestion, indexing, filtering, and analysis—enabling reproducibility and extensibility.
3. **Ontology-Driven Filtering**: Exclusion logic informed by domain ontologies to minimize false positives.
4. **Search Integration**: Designed for seamless embedding into enterprise knowledge retrieval systems via percolator frameworks.
5. **Code Flexibility**: Generic infrastructure allows adaptation to new quality standards (e.g., MIPS, NCQA dimensions).

---

## Key Modules

| Module                                   | Purpose                                         |
| ---------------------------------------- | ----------------------------------------------- |
| `querys/`                                | Example input term definitions for testing      |
| `ExclusionTerms.csv`, `MeasureTerms.csv` | Control lists for term filtering                |
| `select scripts (e.g., aba_filter.py)`   | Defined filter rules tailored per use-case      |
| `config.py`                              | Central configuration and environment variables |
| `main.py`                                | Orchestrates pipeline execution flow            |
| `utils.py`                               | Reusable helper functions (I/O, parsing)        |
| `index_percolator_from_csv.py`           | Integrates terms into indexing systems          |
| XML/Text loaders (`xml_to_text.py`)      | Supports unstructured input conversion          |

---

## Contribution Guidelines

* Fork the current repo and submit pull requests for improvements.
* Push tests for incremental functionality (particularly around percolator integration and filtering logic).
* Ensure backward compatibility with core CSV schemas and utility modules.

---

## Contact & Collaboration

For inquiries, contributions, or collaboration:

* **Abraham Gilbert** — ML Architect specializing in healthcare semantics
* Email: [abrahamgilbert.ai@gmail.com](mailto:abrahamgilbert.ai@gmail.com)
* GitHub: [@Abraham75](https://github.com/Abraham75)

---

> **“Semantic precision bridges healthcare data to intelligent action. WaveHedis enables that bridge—one heuristic at a time.”**

```

---
::contentReference[oaicite:0]{index=0}
```
