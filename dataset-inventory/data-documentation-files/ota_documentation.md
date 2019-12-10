# DATASET NAME: Oxford Text Archive (OTA)

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



## Collection Process:

1. View page source of catalog (<https://ota.ox.ac.uk/catalogue/index.html>) and download as HTML.

   **Product:** view-source_ota.ox.ac.uk_catalogue_index_DO-NOT-EDIT.html

2. Open HTML file in Google Chrome and, using XPATH Helper, extract all data in author column

   **XPATH Query:** /html/body/div[@id='main']/div[@id='onecol']/div[@id='tabs']/div[@id='tabs-1']/table[@class='catalogue']/tbody/tr[*]/td[3]

3. Copy author name results and paste into an Excel spreadsheet.

   **Products:** ota_dataset_raw.xlsx



## DATA CLEANING ASSESSMENT

### Required programs/processes:

- XPATH
- OpenRefine
- Excel "text to column" feature
- Hand editing

### Time:

4 hours?

### Cleaning Process: 

1. Split records where multiple authors are included in one line (locate by searching for split string, ";") and hand-edit encoding errors for characters with diacritic marks.
2. Create **count** column and assign count value of 1 to each record.
3. Using OpenRefine, consolidate author multiples to get list of unique authors and their total counts.
4. Hand-edit top 31 most cited-authors (top 5%).
5. Follow standardization process (documentation: **standardization_phases.md**).



## Data Structure:

**Data formats:** xlsx, csv

**Entity representation:** A cited author and the number of times they were cited in the Oxford Text Archive collection.

**Dimensions:** 

- **Number of records:** 600
- **Properties:** 6

**Data types:** integer, name, year

### Codebook

See **standardization_codebook_final.md**



## VERSIONING

- **_raw**: raw form of the extracted data
- **_cleaned**: repeating author records consolidated; hand-edited for encoding errors
- **_standard**: organized according to **standardization_phases.md**
- **_final**: final version used for processing final dataset