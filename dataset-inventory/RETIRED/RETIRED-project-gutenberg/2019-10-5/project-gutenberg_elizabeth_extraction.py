
# coding: utf-8

# In[75]:

from lxml import etree


# In[76]:

with open('project-gutenberg_catalog_sample.rdf', 'rb') as xmlin:
    text = xmlin.read()


# In[77]:

root = etree.fromstring(text)


# In[78]:

def clean(l):
    return " ".join(" ".join(l).split())

for creator in root.xpath('//dc:creator', namespaces = root.nsmap):
    print("Title:", end = "")
    print(clean(creator.xpath('../dc:title/text()', namespaces = root.nsmap)))
    if len(creator) == 0:
        print("Author", clean(creator.xpath('./text()', namespaces = root.nsmap)))
    else:
        for each in creator.xpath('rdf:Bag/rdf:li', namespaces = root.nsmap):
            print("Author:", clean(each.xpath('./text()')))
#         print(clean(creator.xpath('rdf:Bag/rdf:li/text()', namespaces = root.nsmap)))


# In[80]:

root.xpath('//dc:creator', namespaces = root.nsmap)


# In[ ]:



