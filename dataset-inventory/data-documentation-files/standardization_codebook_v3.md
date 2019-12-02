#### DATA CODEBOOK FOR FILES WITH TEMPLATE: name_dataset_final_2.csv



**FIELD:** last_name

**DESCRIPTION:** Surname of the author of a written work.

**DATA VALUES:** character

**REASON FOR MISSING VALUES:** Author is mononymous.

- Missing value = "not_applicable"

**KNOWN MISSING VALUES:** TBD



**FIELD:** first_name

**DESCRIPTION:** First name of the author of a written work. In some cases, mononym for a mononymous author

**DATA VALUES:** character

**REASON FOR MISSING VALUES:** N/A

**KNOWN MISSING VALUES:** TBD



**FIELD:** title

**DESCRIPTION:** Holds "Mrs." modifier - many female authors are only cited in reference to their spouse.

**DATA VALUES:** character

**REASON FOR MISSING VALUES:** Original author citation does not use "Mrs." title

- Missing value = "not_applicable"

**KNOWN MISSING VALUES:** TBD



**FIELD:** birthdate

**DESCRIPTION:** The birth year of the author. Or: *floruit* value ("a date or period during which a person was known to have been alive or active"). Or: approximate birth year of the author.

**DATA VALUES:** integer

**REASON FOR MISSING VALUES:** no dates listed in data source

**KNOWN MISSING VALUES:** TBD



**FIELD:** deathdate

**DESCRIPTION:** The death year of the author. Or: approximate death year of the author.

**DATA VALUES:** integer

**REASON FOR MISSING VALUES:** no dates listed in data source



**KNOWN MISSING VALUES:** TBD



**FIELD:** count

**DESCRIPTION:** Number of times the author appears in the collected corpus from the given dataset.

**DATA VALUES:** integer

**REASON FOR MISSING VALUES:** N/A

**KNOWN MISSING VALUES:** TBD



**FIELD:** fraction-total

**DESCRIPTION:** The 'count' field divided by the total number of records in the dataset.

**DATA VALUES:** integer

**REASON FOR MISSING VALUES:** N/A

**KNOWN MISSING VALUES:** TBD



**SAMPLE RECORD:**

| last_name | first_name | birthdate | deathdate | count | fraction-total |
| --------- | :--------: | --------- | --------- | ----- | -------------- |
| de Mornay |  Philippe  | 1549      | 1623      | 28    | 0.000293034    |