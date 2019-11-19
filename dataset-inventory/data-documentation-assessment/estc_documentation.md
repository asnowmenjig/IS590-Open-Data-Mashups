# DATASET NAME: English Short Title Catalogue (ESTC)

## DATA CLEANING ASSESSMENT

### Required programs/processes:

- Python
- OpenRefine
- Excel "text to column" feature
- Hand editing

### Time:

8 hours?

### Cleaning Process: 

1. Using OpenRefine, consolidate author multiples to get list of unique authors and their total counts.
2. Hand edit encoding errors for characters with diacritic marks. Hand edit records containing multiple author names - split out into individual records. Consolidate author multiples again.
3. Follow standardization process (documentation: standardization_phases.md)

## DATA DOCUMENTATION

### Provenance:

This data was extracted from the English Short Title Catalog collection in the HathiTrust Digital Library (<https://babel.hathitrust.org/cgi/mb?a=listis&c=247770968>). This collection is based on the English Short Title Catalogue published by The British Library (<http://estc.bl.uk/>).

The HathiTrust collection description states that the works in the collection were "published between 1473 and 1800 mainly, but not exclusively, in English in the British Isles and North America." The collection contains 10,474 items. Of these items, 3 are not available for full-text searching.

The metadata used to create this dataset can be found in the file **english-short-title-catalog.json**.

### Contents:

This file contains author attribution data ("Author" and "Count") extracted from the HathiTrust English Short Title Catalog collection.

**Data used:** 

- biographical author information (first/last names, birthdates, and deathdates)
- citation counts

**Collection date:** September 15, 2019

### Collection Process:

1. Navigate to dataset source: <https://babel.hathitrust.org/cgi/mb?a=listis&c=247770968>

2. Download metadata ("Linked Data (JSON)")

3. Using Python, extract author names and take count of repeated citations. Write results to CSV file.

   **Program file:** estc_extraction.py

   **Product:** estc_dataset.csv

### Data Structure:

**Data formats:** xlsx, csv

**Entity representation:** A cited author and the number of times they were cited in the ESTC collection.

**Dimensions:** 

- **Number of records:** 3,137
- **Properties:** 6

**Data types:** integer, name, year

### Codebook

See **standardization_codebook.md**