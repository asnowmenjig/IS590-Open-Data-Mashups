infile = open('ota-2_source_edited.html','r', encoding='utf-8')   #import data and close infile
text = str(infile.read())
infile.close()
print("Success: opened, read, and closed text!")
#
# split into lines
lines_list = text.split('\n')                       #split full
print("Success: split into lines!")
#

#starts on 139
#ends on 24649

# print(lines_list[146])                                       #used to locate start/end lines of actual ctalogue


dict = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[]}     #setting up dictionary to hold catalog fields
alpha = 65                      #set dictionary key indexing to A
# print(alpha)
# print(chr(alpha))
for line in lines_list[146:24642]:                      #line index of OTA TEI texts
    # print(line)
    if '<tr>' in line:                                  #ending point for a single record; reset dictionary index value
        alpha = 65
    else:
        dict[chr(alpha)].append(line)       #parse through record and add content to appropriate index key-value
        alpha = alpha + 1

print(dict['C'])
print(len(dict['C']))

import csv

print('printing to csv')
for line in dict['C']:
    with open("OTA_authors_dataset_new.csv", 'w', newline = '', encoding="UTF-8") as outfile_csv: #create csv to hold extracted data
        filewriter = csv.writer(outfile_csv, delimiter=',')
        filewriter.writerow(dict['C'])                              #write author name key values to csv

outfile_csv.close()
print("Success: file closed!")
