from lxml import etree

with open('pg37942.rdf', 'rb') as xmlin:
    text = xmlin.read()

#pg37942.rdf = 2 authors
#pg1041.rdf = 1 author

root = etree.fromstring(text)

# cleaning function
def clean(l):
    return " ".join(" ".join(l).split())

authors_list = []
birthdate_list = []
deathdate_list = []

# adding author names to author_names
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


    # print("Title:", end = "")
    # print(clean(creator.xpath('./pgterms:agent/pgterms:name/text()', namespaces = root.nsmap)))
    # if len(creator) == 0:
    #     authors_list.append(clean(creator.xpath('./pgterms:agent/pgterms:name/text()', namespaces = root.nsmap)))
    # else:
    #     for each in creator.xpath('rdf:Bag/rdf:li', namespaces = root.nsmap):
    #         authors_list.append(clean(each.xpath('../pgterms:agent/pgterms:name/text()')))

# root.xpath('//dcterms:creator', namespaces = root.nsmap)

print("Authors list created!")

print(authors_list)
# print(len(authors_list))
print(birthdate_list)
print(deathdate_list)




# ### writing to CSV file ###
#
# import csv
#
# with open("project-gutenberg_dataset.csv", 'w', newline = '', encoding = "UTF-8") as outfile_csv:
#     filewriter = csv.writer(outfile_csv)
#     for author in authors_list:
#         filewriter.writerow([author])
#
# print("Written to CSV!")
#
# outfile_csv.close()
# print("Success: file closed!")
