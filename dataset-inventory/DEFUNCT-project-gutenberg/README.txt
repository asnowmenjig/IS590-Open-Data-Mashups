NAME: Project Gutenberg
AUTHORSHIP: Project Gutenberg
ACCESS: https://www.gutenberg.org



SCRAPING NOTES:

https://www.gutenberg.org/wiki/Gutenberg:Information_About_Robot_Access_to_our_Pages#How_To_Get_Catalog_Data



XPATH COMMANDS:

AUTHORS (https://www.gutenberg.org/browse/authors/*)

/html/body/div[@class='contents']/div[@class='body']/div[@class='pgdbbyauthor']/h2[*]/a[1]




2019-9-18 folder:
- pulled data on 2019-9-18, but did not save original author HTML files (paper trail)


2019-9-26
- started pulling original author HTML files, but cannot use XPATH to pull author data (will need to write Python script to pull data)


2019-10-3:
- downloaded catalog.rdf.zip from http://gutenberg.readingroo.ms/cache/generated/feeds/

2019-10-8:
- downloaded rdf-files.tar.zip from http://gutenberg.readingroo.ms/cache/generated/feeds/