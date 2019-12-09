# DATASET NAME: Project Gutenberg

## DATA DOCUMENTATION

### Provenance:

This data was extracted from Project Gutenberg (<https://www.gutenberg.org/>), a digital library that contains full-text eBooks of public domain texts (based on U.S. copyright). The initiative is largely volunteer-run and contains over 60,000 texts. The site is hosted by ibiblio at UNC Chapel Hill. The vast majority of texts are free to use without restrictions.

### Contents:

This file contains author attribution data extracted from the Project Gutenberg catalog.

**Data used:** 

- author name information (first/last names, birthdates, and deathdate)
- citation counts

**Collection date:** October 8, 2019



## Collection Process:

1. Navigate to <http://gutenberg.readingroo.ms/cache/generated/feeds/> and download the TAR archive (**rdf-files.tar.zip**)

   **Note:** The catalog is updated nightly. The TAR archive used for this dataset reflects the catalog as it was downloaded on 2019/10/8, ‏‎9:27:42 AM.

2. Using Python, extract author names, birthdates, and death dates.

   **Product:** project-gutenberg-2_dataset.csv



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
2. Hand edit encoding errors for characters with diacritic marks.
3. Follow standardization process (documentation: **standardization_phases.md**)



## Data Structure:

**Data formats:** xlsx, csv

**Entity representation:** A cited author and the number of times they appear in the Project Gutenberg catalog.

**Dimensions:** 

- **Number of records:** 20,801
- **Properties:** 6

**Data types:** integer, name

### Codebook

See **standardization_codebook.md**