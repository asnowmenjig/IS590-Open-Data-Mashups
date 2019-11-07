# Stage 1:

Manually standardize column names in datasets

**Naming convention**: name_dataset_standard_1.csv

**Table: Field available in raw dataset?**

| FIELD          | EEBO | ESTC | OPEN-SYLLABUS | OTA  | PROJECT-GUTENBERG |
| -------------- | :--: | :--: | :-----------: | :--: | :---------------: |
| author_name    |  o   |  o   |       o       |  o   |         o         |
| count          |  o   |  o   |       o       |  o   |         o         |
| fraction-total |  o   |  o   |       o       |  o   |         o         |
| birthdate      |      |      |               |      |         o         |
| deathdate      |      |      |               |      |         o         |



# Stage 2:

First round of splitting fields using Excel "text to columns" feature

**Naming convention**: name_dataset_standard_2.csv

**Table: Can data be transformed to fit field?**

| FIELD          | DESCRIPTION | DATA VALUES | MISSING - REASON | KNOWN MISSING |
| -------------- | :---------: | :---------: | :--------------: | :-----------: |
| first_name     |      o      |      o      |        o         |       o       |
| last_name      |      o      |      o      |        o         |       o       |
| count          |      o      |      o      |        o         |       o       |
| fraction-total |      o      |      o      |        o         |       o       |
| birthdate      |      o      |      o      |                  |       o       |
| deathdate      |      o      |      o      |                  |       o       |

**Table: character split point**

| DATASET           | SPLIT POINT |
| ----------------- | :---------: |
| EEBO              | comma, dash |
| ESTC              |    comma    |
| Open Syllabus     |    space    |
| OTA               |    comma    |
| Project Gutenberg |    comma    |



# Stage 3:

Manually clean records and cells

**Naming convention:** name_dataset_standard_3.csv

- Sort dataset based on the last column that has content (Z-A)

  - When rows are more fractured across more columns, they require more cleaning. Highest rate of error when splitting (e.g. “Mornay, Philippe de, seigneur du Plessis-Marly, 1549-1623.” is split across 6 columns when it should only be split across 4)

- Move values to appropriate columns

  - e.g. Mornay, Philippe de, seigneur du Plessis-Marly, 1549-1623.

    Original:

    | last_name | first_name  | birthdate                 | deathdate |      |
    | --------- | :---------: | ------------------------- | --------- | ---- |
    | Mornay    | Philippe de | seigneur du Plessis-Marly | 1549      | 1623 |

    Cleaned:

    | last_name | first_name | birthdate | deathdate |
    | --------- | :--------: | --------- | --------- |
    | de Mornay |  Philippe  | 1549      | 1623      |

- Cleaning standards for names:
  - For names without surnames, use title (“Saint of”, “Prince of”, “King of”, “of Garland”, etc.) in last_name column
  - For surnames with nobiliary particles (“de”, “di”, “von”, etc.), put particle at the beginning of last_name column
    - e.g. “Philippe de Mornay” = “de Mornay, Philippe”
  - For records with *floruit* (fl.) instead of birthdate, use numerical *floruit* value only
  - For records with approximate dates (“ca.”,
    “approximately”, “active”), use numerical date only
  - For records from B.C.E., keep “B.C.” in
    birthdate and deathdate columns
  - For records with varying birthdates or
    deathdates (e.g. “1553 or 4”, “1579 or 80”), keep both values

