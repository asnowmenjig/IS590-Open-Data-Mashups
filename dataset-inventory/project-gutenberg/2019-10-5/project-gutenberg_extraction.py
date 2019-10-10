from lxml import etree

with open('project-gutenberg_catalog.rdf', 'rb') as xmlin:
    text = xmlin.read()

root = etree.fromstring(text)

# cleaning function
def clean(l):
    return " ".join(" ".join(l).split())

authors_list = []

# adding author names to author_names
for creator in root.xpath('//dc:creator', namespaces = root.nsmap):
    # print("Title:", end = "")
    # print(clean(creator.xpath('../dc:title/text()', namespaces = root.nsmap)))
    if len(creator) == 0:
        authors_list.append(clean(creator.xpath('./text()', namespaces = root.nsmap)))
    else:
        for each in creator.xpath('rdf:Bag/rdf:li', namespaces = root.nsmap):
            authors_list.append(clean(each.xpath('./text()')))


root.xpath('//dc:creator', namespaces = root.nsmap)

print("Authors list created!")

# print(authors_list)
print(len(authors_list))

# print(authors_list[6400:6410])                   #tester to find broken index point

dud_authors = []

### writing to CSV file ###

import csv

with open("project-gutenberg_dataset.csv", 'w', newline = '', encoding = "UTF-8") as outfile_csv:
    filewriter = csv.writer(outfile_csv)
    for author in authors_list:
        filewriter.writerow([author])

print("Written to CSV!")

outfile_csv.close()
print("Success: file closed!")
