from lxml import etree

with open('pg37942.rdf', 'rb') as xmlin:
    text = xmlin.read()

#pg37942.rdf = 2 authors
#pg1041.rdf = 1 author (shakesepare)

root = etree.fromstring(text)

# define namespace

ns = {'xmlns:dcterms':"http://purl.org/dc/terms/",
      'xmlns:rdfs':"http://www.w3.org/2000/01/rdf-schema#",
      'xmlns:dcam':"http://purl.org/dc/dcam/",
      'xmlns:pgterms':"http://www.gutenberg.org/2009/pgterms/",
      'xmlns:rdf':"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      'xmlns:cc':"http://web.resource.org/cc/"
      }

# cleaning function
def clean(l):
    return " ".join(" ".join(l).split())

authors_list = []

# adding author names to author_names
for creator in root.xpath('//dc:creator', namespaces = ns):
    # print("Title:", end = "")
    # print(clean(creator.xpath('../dc:title/text()', namespaces = root.nsmap)))
    if len(creator) == 0:
        authors_list.append(clean(creator.xpath('./text()', namespaces = ns)))
    else:
        for each in creator.xpath('rdf:Bag/rdf:li', namespaces = ns):
            authors_list.append(clean(each.xpath('./text()')))


root.xpath('//dc:creator', namespaces = root.nsmap)

print("Authors list created!")

# print(authors_list)
print(len(authors_list))


### writing to CSV file ###

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
