# DATASET NAME: Open Syllabus Project

## DATA DOCUMENTATION

### Provenance:

This data was extracted from the Open Syllabus Project Explorer (<https://opensyllabus.org/>). The Open Syllabus Project is an initiative that extracts metadata from public/contributed syllabi from colleges and universities. The Explorer presents this data along parameters such as citation count (how often a title appears in the collection), rank (a title's count compared against the other titles in the collection), field of study, country, etc.

Open Syllabus 2.0 was published on July 16, 2019. At the time of data collection, the Open Syllabus has "a corpus of seven million English-language syllabi from over 80 countries."

### Contents:

This file contains author attribution data ("Author" and "Count") extracted from the Open Syllabus Project Explorer results, filtered by "Field = English Literature".

**Data used:** 

- author name information (first/last names)
- citation counts

**Collection date:** September 15, 2019



## Collection Process:

1. View Explorer and filter by "Authors" and "Field = English Literature". Set list view to 5000.

   **URL:** [https://opensyllabus.org/results-list/authors?size=5000&fields=English%20Literature](https://opensyllabus.org/results-list/authors?size=5000&fields=English Literature)

2. Using XPATH Helper, highlight author names column and appearances column. Paste into Excel spreadsheet.

   **Products:** open-syllabus_dataset.xlsx



## DATA CLEANING ASSESSMENT

### Required programs/processes:

- XPATH Helper
- Excel "text to column" feature
- Hand editing

### Time:

2 hours?

### Cleaning Process: 

1. Follow standardization process (documentation: **standardization_phases.md**)



## Data Structure:

**Data formats:** xlsx

**Entity representation:** A cited author and the number of times they appear in the Open Syllabus Project database.

**Dimensions:** 

- **Number of records:** 5,000
- **Properties:** 4

**Data types:** integer, name

### Codebook

See **standardization_codebook_final.md**