#with open('OTA_edited.txt','r', encoding='utf-8') as file:
#    x = file.read()

#print(x[4500:5371])


#print(x[5200:5800])

#remove <td> and </td> and blank lines

#create dictionary: dictionaryb = {'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[]}

#split text into lines
#when see [ a href ], append line to dictionary key 'a', add to key counter
#successively append lines to b,c,d,e,f,g until hit '</tr>'
#restart key counter



# open text
infile = open('OTA_edited.txt','r', encoding='utf-8')
text = str(infile.read())
infile.close()
print("Success: opened, read, and closed text!")
#
# split into lines
lines_list = text.split('\n')
print("Success: split into lines!")
#

#print(lines_list[1:51])


dict = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[]}
alpha = 65       #a
print(alpha)
print(chr(alpha))
for line in lines_list[1:19307]:    #OTA TEI texts
    if '<tr>' in line:
        alpha = 65
    else:
        dict[chr(alpha)].append(line)
        alpha = alpha + 1

print(dict['C'])
print(len(dict['C']))


import csv

for line in dict['C']:
    with open("OTA_authors_dataset.csv", 'w', newline = '', encoding="UTF-8") as outfile_csv:
        filewriter = csv.writer(outfile_csv, delimiter=',')
        filewriter.writerow(dict['C'])

outfile_csv.close()
print("Success: file closed!")
