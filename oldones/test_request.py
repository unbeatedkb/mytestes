# coding: utf-8

import requests
import json

'''
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
'''
headers = {
    "Cookie": "aliyungf_tc=AQAAAIP0Ul3dAgoA5ClHZYlkreXSnTMj; __utmc=1; device_id=a013aef34dfa128a538dcea705827230; __utmz=1.1525404474.6.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; s=em117q0i7e; bid=e9860521a97c9fdfcbce0ccd89528dc9_jgrh9wf5; snbim_minify=true; _ga=GA1.2.1139764910.1525327340; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=838bbf3bffddbcf18d7472efa65af950121f0923; xq_a_token.sig=iNINQOrAzKctrKQ-HqgoJazJ0Tw; xq_r_token=3e41203a7f1bafc4f9c29588ad354f615dc24d63; xq_r_token.sig=ljhaLKrumq6I5YYMKOkLw84Ei6E; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=6830377191; u.sig=XzXGYxrYRGhK4SNBuqXjIj6L8LY; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528081772,1529485209; _gid=GA1.2.990057879.1529890051; __utma=1.1139764910.1525327340.1529912010.1529996465.91; __utmb=1.1.10.1529996465; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1529997187; _gat_gtag_UA_16079156_4=1", 
    "Host": "xueqiu.com", 
    "Referer": "https://xueqiu.com/", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36", 
    "X-Requested-With": "XMLHttpRequest"
}

# url = "https://m.toutiao.com/list/?tag=news_finance&ac=wap&count=20&format=json_raw&as=A185FBE13747D1B&cp=5B17E75D31ABCE1"
# url = 'https://xueqiu.com/statuses/home_timeline/unread.json'
# url = 'https://xueqiu.com/v4/statuses/home_timeline.json'
# url = 'https://xueqiu.com/friendships/create/9097259018.json'
url = 'https://xueqiu.com/friendships/destroy/6625463998.json'


params = {
          'since_id': '109476400',
          'source': '股票微博',
          '_': '1529926200726'
        }

'''
params = {
            'source': 'user',
            # 'since_id': '109486682',
            '_': '1529990547837',
    }
'''

data = {
    "remark": "true"
}

proxies = {'http': 'http://hexin:hx300033@101.71.41.194:888', 'https': 'http://hexin:hx300033@101.71.41.194:888'}

r = requests.post(url, headers=headers, proxies=proxies)

print r

# body = r.content.decode("unicode-escape")
# print json.dumps(json.loads(body), indent=4)
# body = r.content.decode('utf-8')
body = r.content
print body
'''
with open('files/t1', 'w') as f:
    f.write(r.content)
'''

