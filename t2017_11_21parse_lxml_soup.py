# coding: utf-8

import time
from bs4 import BeautifulSoup
import codecs

with codecs.open('new.html', 'r', 'utf-8') as f:
    htmlstr = f.read()


# from lxml import etree
# from lxml import html

# het = etree.HTML(htmlstr)

# print het.xpath('/html/body/div[5]/div[3]/div[1]/div[1]/div[2]/ul/li[3]/a/text()')[0]

# field_map = {
#     '姓名': 'name',
#     '性别': 'sex',  
#     work  
#     position  
#     nation 
#     native_place
#     birth  
#     college  
#     major  
#     edu_bk  
#     industry  
#     hobby  
# }

soup = BeautifulSoup(htmlstr, 'html.parser')

theblock = soup.find(class_='right')

for li in theblock.find_all('li'):
    key, value = li.get_text().split(u'：')
    print key, value
    print key.encode('utf-8').strip(), value









