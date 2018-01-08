# coding: utf-8

import requests

url = 'https://xueqiu.com/snowman/login'
headers = {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "zh-CN,zh;q=0.9", 
    "Connection": "keep-alive", 
    "Content-Length": "227", 
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
    "Host": "xueqiu.com", 
    "Origin": "https://xueqiu.com", 
    "Referer": "https://xueqiu.com/", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36", 
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    "captcha": "", 
    "geetest_challenge": "fb0a028636f78fac39e83bc68d73635d9i", 
    "geetest_seccode": "1667dd8775c69a05b6b726496e874d1d|jordan", 
    "geetest_validate": "1667dd8775c69a05b6b726496e874d1d", 
    "password": "wangzha111", 
    "remember_me": "true", 
    "username": "17354701694"
}

r = requests.post(url, headers=headers, data=data)
print r
print r.content.decode('utf-8')

