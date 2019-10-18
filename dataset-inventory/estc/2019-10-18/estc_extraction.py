import json

infile = open('estc_for-parsing', 'r', encoding = 'utf-8')
data = json.load(infile)
infile.close()

author_dictionary = {}

for record in data:
    if 'author' in record:
        author_name = record['author']
    else:
        author_name = 'missing_author'

    if author_name in author_dictionary:
        author_dictionary[author_name] += 1
    else:
        author_dictionary[author_name] = 1

# print(author_dictionary)

import csv

outfile = open('estc_dataset.csv', 'w', newline = '')
csvout = csv.writer(outfile)
csvout.writerow(['author', 'count'])

for pair in author_dictionary.items():
    label = pair[0]
    count = pair[1]
    row = [label, count]
    csvout.writerow(row)
