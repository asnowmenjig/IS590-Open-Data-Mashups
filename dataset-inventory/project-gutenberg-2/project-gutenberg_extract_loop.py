def clean(l):                                       #cleaning function
    return " ".join(" ".join(l).split())

from lxml import etree

authors_list = []                                   #list for author name values
birthdate_list = []                                 #list for birthdate values
deathdate_list = []                                 #list for deathdate values

file_counter = 1                                    #file counter value


while file_counter < 60453:#total number of files
    if file_counter == 1691:
        file_counter = file_counter + 1
    elif file_counter == 28520:
        file_counter = file_counter + 1
    elif file_counter == 30254:                     #if-elif chunk:
        file_counter = file_counter + 1             #  skipping missing files; added through hard-coding when
    elif file_counter == 30360:                     #  loop hit an error
        file_counter = file_counter + 1
    elif file_counter == 36169:
        file_counter = file_counter + 1
    elif file_counter == 58783:
        file_counter = file_counter + 1
    elif file_counter == 59328:
        file_counter = file_counter + 1
    elif file_counter == 59665:
        file_counter = file_counter + 1
    elif file_counter == 59705:
        file_counter = file_counter + 1
    elif file_counter == 60001:
        file_counter = file_counter + 1

    with open('pg'+str(file_counter)+'.rdf', 'rb') as xmlin:        #looping through RDF files and reading individually
        text = xmlin.read()

    root = etree.fromstring(text)

    for creator in root.xpath('//dcterms:creator', namespaces = root.nsmap):                #look at creator namespace
        authors_list.append(clean(creator.xpath('./pgterms:agent/pgterms:name/text()', namespaces = root.nsmap)))       #add author name to authors_list
        if len(creator.xpath('./pgterms:agent/pgterms:birthdate/text()', namespaces = root.nsmap)) == 0:
            birthdate_list.append("no_birthdate")                                                                                   #if birthdate absent, add "no_birthdate" to birthdate_list;
        else:                                                                                                                       #otherwise add birthdate value
            birthdate_list.append(clean(creator.xpath('./pgterms:agent/pgterms:birthdate/text()', namespaces = root.nsmap)))
        if len(creator.xpath('./pgterms:agent/pgterms:deathdate/text()', namespaces = root.nsmap)) == 0:
            deathdate_list.append("no_deathdate")                                                                                   #if deathdate absent, add "no_deathdate" to deathdate_list
        else:                                                                                                                       #otherwise add deathdate value
            deathdate_list.append(clean(creator.xpath('./pgterms:agent/pgterms:deathdate/text()', namespaces = root.nsmap)))


    file_counter = file_counter + 1             #move to next RDF file

print("Authors list created!")

# print(authors_list)
# print(birthdate_list)
# print(deathdate_list)

# print('authors_list = ' + str(len(authors_list)))
# print('birthdate_list = ' + str(len(birthdate_list)))
# print('deathdate_list = ' + str(len(deathdate_list)))






### WRITING TO CSV FILE ###

index_counter = 0               #index counter for values lists

import csv

outfile = open('project-gutenberg-2_dataset.csv', 'w', encoding = 'utf-8', newline = '')        #create csv
csvout = csv.writer(outfile)
csvout.writerow(['author', 'birthdate', 'deathdate'])                                           #create column headers

for item in authors_list:
    author = authors_list[index_counter]                    #assign author name to author variable
    birthdate = birthdate_list[index_counter]               #assign birthdate to birthdate variable
    deathdate = deathdate_list[index_counter]               #assign deathdate to deathdate variable
    row = [author, birthdate, deathdate]                    #assign values to row
    csvout.writerow(row)                                    #write row to csv
    index_counter = index_counter + 1                       #move to next index

outfile.close()
print("Success: data written and file closed!")
