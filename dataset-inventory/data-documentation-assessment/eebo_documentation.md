# DATASET NAME: Early English Books Online (EEBO)

## DATA CLEANING ASSESSMENT

### Required programs/processes:

- OpenRefine
- Excel "text to column" feature
- Hand editing

### Time:

5 hours?

### Cleaning Process: 

1. Once raw data is collected in Excel file, manually reorganize records into two columns: author names and title counts.
2. Using OpenRefine, consolidate author multiples to get list of unique authors and their total counts.
3. Hand edit encoding errors for characters with diacritic marks.
4. Follow standardization process (documentation:
   **standardization_phases.md**)

## DATA DOCUMENTATION

### Provenance:

This data was extracted from the Early English Book Online collection housed on the ProQuest platform (<https://search.proquest.com/eebo/index>). The platform was accessed using University of Illinois at Urbana-Champaign credentials and subscription. The dataset is sourced from two sub-collections in EEBO: "Early English Books 1475-1640 (STC)" and "Early English Books 1641-1700 (Wing)".

"Early English Books 1475-1640 (STC)" contains 34,211 items. This digitized microfilm collection contains works from the English Renaissance.

"Early English Books 1641-1700 (Wing)" contains 71,449 items. It contains works from the English Civil War, the Interregnum, and the Restoration.

### Contents:

This file contains author attribution data ("Author" and "Count) extracted from the ProQuest "Early English Books 1475-1640 (STC)" and "Early English Books 1641-1700 (Wing)" collections.

**Data used:** 

- biographical author information (first/last names, birthdates, and deathdates)
- citation counts

**Collection date:** October 3, 2019

### Collection Process:

1. Navigate to dataset source: <https://search.proquest.com/eebo/index>

2. Define dataset parameters:

   - Collection: Early English Books, 1475-1640 (STC), Early English Books, 1641-1700 (Wing)
   - **Language:** English
   - **Publication Date (specific date range):** 1470-1759

3. Filter author titles by shorter year chunk

4. View authors.

5. Copy “Author” and “Count” columns, paste into Excel

   - For full documentation of raw data chunks and links to searches, see: eebo_dataset_raw_DO-NOT-EDIT.xlsx

6. Manually reorganize data into two columns

   **Product:** eebo_dataset_combined.csv

7. Use OpenRefine to consolidate author multiples and get total author counts

   **Product:** eebo_dataset_cleaned.xlsx

### Data Structure:

**Data formats:** xlsx, csv

**Entity representation:** A cited author and the number of times they were cited in the EEBO collection.

**Dimensions:** 

- **Number of records:** 860
- **Properties:** 6

**Data types:** integer, name, year

### Codebook

See DATASET NAME: English Short Title Catalogue (ESTC)

## DATA CLEANING ASSESSMENT

### Required programs/processes:

- Python
- OpenRefine
- Excel "text to column" feature
- Hand editing

### Timeline:

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

- **Number of records:** 860
- **Properties:** 6

**Data types:** integer, name, year

### Codebook

See **standardization_codebook.md**