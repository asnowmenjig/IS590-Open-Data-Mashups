# DATASET NAME: Early English Books Online (EEBO)

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



## COLLECTION PROCESS

1. Navigate to dataset source: <https://search.proquest.com/eebo/index>
2. Define dataset parameters:

   - Collection: Early English Books, 1475-1640 (STC), Early English Books, 1641-1700 (Wing)
   - **Language:** English
   - **Publication Date (specific date range):** 1470-1759
3. Filter author titles by shorter year chunk
4. View authors.
5. Copy “Author” and “Count” columns, paste into Excel

   - For full documentation of raw data chunks and links to searches, see: eebo_dataset_raw_DO-NOT-EDIT.xlsx



## DATA CLEANING ASSESSMENT

### Required programs/processes:

- OpenRefine
- Excel "text to column" feature
- Hand editing

### Time:

5 hours?

### Cleaning Process: 

1. Manually reorganize data into two columns

   **Product:** eebo_dataset_combined.csv

2. Use OpenRefine to consolidate author multiples and get total author counts. Hand edit encoding errors for characters with diacritic marks.

   **Product:** eebo_dataset_cleaned.xlsx

3. Follow standardization process (documentation: **standardization_phases.md**)

   **Product:** eebo_dataset_cleaned.xlsx



## DATA STRUCTURE

**Data formats:** xlsx, csv

**Entity representation:** A cited author and the number of times they were cited in the EEBO collection.

### Dimensions:

- **Number of records:** 860
- **Properties:** 6

**Data types:** integer, name, year

### Codebook

See **standardization_codebook_final.md**



