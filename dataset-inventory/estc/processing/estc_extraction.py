import json

infile = open('estc_for-parsing.json', 'rb')        #import data and close infile
data = json.load(infile)
infile.close()

author_dictionary = {}

print('building author_dictionary')

for record in data:
    if 'author' in record:
        author_name = record['author']              #if object has an author name field, set author_name variable to
    else:                                           #  the string contained in that field. if no author name, set
        author_name = 'missing_author'              #  variable to 'missing_author'

    if author_name in author_dictionary:            #if the string assigned to author_name variable is already in the
        author_dictionary[author_name] += 1         #  counting dictionary, count +1. if not, add to the dictionary
    else:                                           #  and assign count=1
        author_dictionary[author_name] = 1

print("writing to csv")

import csv

outfile = open('estc_dataset_raw.csv', 'w', encoding = 'utf-8', newline = '')       #create csv to hold extracted data
csvout = csv.writer(outfile)
csvout.writerow(['author', 'count'])

for pair in author_dictionary.items():              #for each row in csv, write author names into first column and
    label = pair[0]                                 #  counts into second column
    count = pair[1]
    row = [label, count]
    csvout.writerow(row)

outfile.close()                                     #close outfile
print("Success: data written and file closed!")
