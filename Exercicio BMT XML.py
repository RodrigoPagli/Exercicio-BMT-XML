#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

#Localização do Arquivo
file_name = 'cf79.xml'
full_file = os.path.abspath(os.path.join('data',file_name))


# In[2]:


#Processador A - DOM - Autores
from xml.etree import ElementTree as ET

dom = ET.parse(full_file)
root = dom.getroot()
record = root.findall('RECORD')
raiz = ET.Element('AUTHORS')

#Imprime os dados aqui no Python.
print('ALL AUTHORS')
for r in record:
    authors = r.find('AUTHORS')
    if authors != None:
        author = authors.findall('AUTHOR')
    for a in author:
        b = 1
        print(a.text)

print('ALL TITLES')
for r in record:
    title = r.find('TITLE')
    print('\n',title.text)

for r in record:
    authors = r.find('AUTHORS')
    if authors != None:
        author = authors.findall('AUTHOR')
    for a in author:
        autores = ET.SubElement(raiz,'AUTHOR')
        autores.text = a.text
        
b_xml = ET.tostring(raiz)
with open("autores.xml","wb") as f:
    f.write(b_xml)


# In[3]:


#Processador B - SAX - Títulos
import xml.sax

lista_titulos = []

class TitleHandler(xml.sax.ContentHandler):
    def startElement(self , name , attrs):
        self.title = ''
#        print(name)
        self.current = name
        if name == 'RECORD':
            print(f'-- Record -- ')
    def characters(self,content):
        if self.current == 'TITLE':
            self.title += content
    def endElement(self,name):
        if self.current == 'TITLE':
            print("TITLE: {}".format(self.title))
        self.current = ''
        if self.title!= '':
            lista_titulos.append("TITLE: {}".format(self.title))

handler = TitleHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(full_file)

with open('titulos.txt', 'w') as f:
    for titulo in lista_titulos:
        f.write(titulo)
        f.write('\n')

