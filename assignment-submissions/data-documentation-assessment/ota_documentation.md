# DATASET NAME: Oxford Text Archive (OTA)

## DATA CLEANING ASSESSMENT

### Required programs/processes:

- Python
- OpenRefine
- Excel "text to column" feature
- Hand editing

### Time:

4 hours?

### Cleaning Process: 

1. Using OpenRefine, consolidate author multiples to get list of unique authors and their total counts.
2. Hand edit encoding errors for characters with diacritic marks.
3. Follow standardization process (documentation: **standardization_phases.md**)

## DATA DOCUMENTATION

### Provenance:

This data was extracted from the Oxford Text Archive, published by the University of Oxford (<http://ota.ox.ac.uk/>).

[OTA website is down for maintenance as I'm writing this - will update provenance information when site is back up]

### Contents:

This file contains author attribution data ("Author" and "Count") extracted from the Oxford Text Archive catalog.

**Data used:** 

- biographical author information (first/last names, birthdates, and deathdates)
- citation counts

**Collection date:** September 15, 2019

### Collection Process:

1. View page source of catalog (<https://ota.ox.ac.uk/catalogue/index.html>) and download as HTML.

   **Product:** view-source_ota.ox.ac.uk_catalogue_index.html

2. Using Python, extract author names. Manually reformat HTML file as program gets stuck on inconsistencies (i.e. author names span more than one line)

   **Program file:** ota_extraction.py

   **Products:** ota_source_edited.html ; ota_authors_dataset.csv

### Data Structure:

**Data formats:** xlsx, csv

**Entity representation:** A cited author and the number of times they were cited in the ESTC collection.

**Dimensions:** 

- **Number of records:** 606
- **Properties:** 6

**Data types:** integer, name, year

### Codebook

See **standardization_codebook.md**