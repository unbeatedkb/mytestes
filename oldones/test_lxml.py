# coding: utf-8

from lxml import etree
import requests

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url = 'https://zhidao.baidu.com/question/331707504137775885.html'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "zh-CN,zh;q=0.9", 
    "Cache-Control": "max-age=0", 
    "Connection": "keep-alive", 
    "Host": "zhidao.baidu.com", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

r = requests.get(url, headers=headers)

from scrapy.selector import Selector

selector = Selector(r)
print selector.xpath('''//div[@class='line content']//span//@data-evaluate''').extract()

input()

content = r.content

# 字符串是不可变类型
# lxml库会识别字符集
# content = content.replace('charset=gbk', 'charset=utf-8')
content = content.replace(r'<meta http-equiv="content-type" content="text/html;charset=utf-8" />', '')

# with open('files/t1', 'w') as f:
    # f.write(content)
# tree = etree.parse('files/t1', etree.HTMLParser(encoding='utf-8'))

tree = etree.HTML(content, etree.HTMLParser(encoding='utf-8'))

path = '''//div[@class='line content']/*[contains(@id, 'answer')]/text()'''

items = tree.xpath("//title/text()")


for item in items:
    
    print item


# print list(items)
