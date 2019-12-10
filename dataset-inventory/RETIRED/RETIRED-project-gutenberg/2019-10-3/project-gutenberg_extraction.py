from lxml import etree

# read in RDF file
infile = open('project-gutenberg_catalog_sample.rdf','rb')
xml = infile.read()
infile.close()

#parse into tree
tree = etree.fromstring(xml)

# define namespace

ns = {'pgterms' : 'http://www.gutenberg.org/rdfterms/',
      'rdf' : "http://www.w3.org/1999/02/22-rdf-syntax-ns",
      'rdfs':"http://www.w3.org/2000/01/rdf-schema#",
      'xsd':"http://www.w3.org/2001/XMLSchema#",
      'dc':"http://purl.org/dc/elements/1.1/",
      'dcterms':"http://purl.org/dc/terms/",
      'dcmitype':"http://purl.org/dc/dcmitype/",
      'cc':"http://web.resource.org/cc/",
      'pgterms':"http://www.gutenberg.org/rdfterms/"
     }

#for titles with a single author
authors_list_singles = tree.xpath('//dc:creator[@rdf:parseType="Literal"]/text()', namespaces = ns)   #FAILS
authors_list_singles = tree.xpath('//dc:creator/text()', namespaces = ns)                             #WORKS

#for titles with multiple authors
authors_list_multis = tree.xpath('//dc:creator/rdf:Bag/rdf:li/text()', namespaces = ns)               #FAILS


print(authors_list_singles)
print(authors_list_multis)


### Code below is for writing to CSV file ###

import csv

# with open("project-gutenberg_authors_dataset.csv", 'w', newline = '', encoding="UTF-8") as singles_outfile:
#     filewriter = csv.writer(singles_outfile)
#     for author in authors_list_singles[0:100]:
#         filewriter.writerow([author])

with open("project-gutenberg_authors_dataset.csv", 'w', newline = '', encoding="UTF-8") as multis_outfile:
    filewriter = csv.writer(multis_outfile)
    for author in authors_list_multis:
        filewriter.writerow([author])

# singles_outfile.close()
multis_outfile.close()
print("Success: file closed!")
