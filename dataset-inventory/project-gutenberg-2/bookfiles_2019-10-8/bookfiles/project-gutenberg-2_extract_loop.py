def clean(l):
    return " ".join(" ".join(l).split())

from lxml import etree

authors_list = []
birthdate_list = []
deathdate_list = []

file_counter = 1

#pg1.rdf = pg1041.rdf = 1 author
#pg2.rdf = pg37942.rdf = 2 authors


while file_counter < 1001:
    # print('pg'+str(file_counter)+'.rdf')
    with open('pg'+str(file_counter)+'.rdf', 'rb') as xmlin:
        text = xmlin.read()

    root = etree.fromstring(text)

    for creator in root.xpath('//dcterms:creator', namespaces = root.nsmap):
        authors_list.append(clean(creator.xpath('./pgterms:agent/pgterms:name/text()', namespaces = root.nsmap)))
        if len(creator.xpath('./pgterms:agent/pgterms:birthdate/text()', namespaces = root.nsmap)) == 0:
            birthdate_list.append("no_birthdate")
        else:
            birthdate_list.append(clean(creator.xpath('./pgterms:agent/pgterms:birthdate/text()', namespaces = root.nsmap)))
        if len(creator.xpath('./pgterms:agent/pgterms:deathdate/text()', namespaces = root.nsmap)) == 0:
            deathdate_list.append("no_deathdate")
        else:
            deathdate_list.append(clean(creator.xpath('./pgterms:agent/pgterms:deathdate/text()', namespaces = root.nsmap)))

    # print('redefining file_counter')
    file_counter = file_counter + 1

print("Authors list created!")

# print(authors_list)
# print(birthdate_list)
# print(deathdate_list)

print('authors_list = ' + str(len(authors_list)))
print('birthdate_list = ' + str(len(birthdate_list)))
print('deathdate_list = ' + str(len(deathdate_list)))




### writing to CSV file ###

index_counter = 0

import csv

outfile = open('project-gutenberg-2_dataset.csv', 'w', encoding = 'utf-8', newline = '')
csvout = csv.writer(outfile)
csvout.writerow(['author', 'birthdate', 'deathdate'])

for item in authors_list:
    author = authors_list[index_counter]
    birthdate = birthdate_list[index_counter]
    deathdate = deathdate_list[index_counter]
    row = [author, birthdate, deathdate]
    csvout.writerow(row)
    index_counter = index_counter + 1

outfile.close()
print("Success: data written and file closed!")
