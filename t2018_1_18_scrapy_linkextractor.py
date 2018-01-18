# coding: utf-8

from scrapy.linkextractors import sgml
from scrapy.linkextractors import LinkExtractor
from pyfiles import sgml
import requests
from scrapy.http import Request, TextResponse

# se = sgml.SgmlLinkExtractor()
# se = LinkExtractor()
se = SgmlLinkProcesser()

url = 'http://www.p5w.net/news/biz/'

req = Request(url=url)
content = requests.get(url).content
content = content.decode('gbk').encode('utf-8')

res = TextResponse(url, body=content, request=req, encoding='utf8')


links = se.extract_links(res)

for link in links:
    print link.url
    print link.text