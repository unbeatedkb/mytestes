# coding: utf-8

import requests
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "m.toutiao.com",
    "Cookie": '''''',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}    

url = "https://m.toutiao.com/list/?tag=news_finance&ac=wap&count=20&format=json_raw&as=A185FBE13747D1B&cp=5B17E75D31ABCE1"

params = {}

proxies = {'http': 'http://hexin:hx300033@101.71.41.194:888', 'https': 'http://hexin:hx300033@101.71.41.194:888'}

r = requests.get(url, headers=headers, proxies=proxies)

print r

body = r.content.decode("unicode-escape")
# print json.dumps(json.loads(body), indent=4)
print body


