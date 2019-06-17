# coding: utf-8

import requests
import multiprocessing
import time
from multiprocessing import Queue
from pymongo import MongoClient
import json

q = Queue(4096)


apiurl = 'http://www.gelonghui.com/api/user/get?userId=%s'
header = {
    "Host": "www.gelonghui.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}
maxid = 1000000
mg_uri = 'mongodb://127.0.0.1:27017'
# mg_uri = 'mongodb://192.168.40.162:27017'

mg_db = None
mg_coll = None


def reconnect_mg():
    global mg_db
    try:
        mg_db.close()
        del mg_db
    except:
        pass
    mg_db = MongoClient(mg_uri, maxPoolSize=200).get_database()

def get_mg_coll(coll="zh_raw"):

    global mg_db
    if not mg_db:
        reconnect_mg()
    try:
        mg_coll = mg_db[coll]
    except:
        reconnect_mg()
        mg_coll = mg_db[coll]
    return mg_coll


def genuseridss():
    userids = []
    for i in range(1, maxid+1):
        userids.append(i)
    return userids


def crawl(userid):
    url = apiurl % userid
    try:
        r = requests.get(url, headers=header, timeout=5)
        print r
        if r.status_code != 200:
            return
        print('crawl succefully, url: %s' % url)
        q.put([userid, r.content])
    except:
        pass


def mgsave(userid, content):
    mg_coll = get_mg_coll()
    try:
        content = json.loads(content)
        if content.get('statusCode') and int(content.get('statusCode')) == 200:
            mg_coll.update({'userid': userid}, {'$set': json.loads(content)}, True)
            print('save succefully, userid: %s' % userid)
    except:
        pass


def save():
    while True:
        if q.empty():
            print 'empty...'
            time.sleep(1)
            continue
        userid, content = q.get()
        if not content:
            continue
        else:
            mgsave(userid, content)


if __name__ == "__main__":
    # 生成所有url
    userids = genuseridss()
    print("get all userids, all: %s" % len(userids))
    # 将url送到下载器去下载
    pool = multiprocessing.Pool(processes=3)
    for userid in userids:
        pool.apply_async(crawl, args=(userid,))
    # 将下载的内容存入mongo
    save()

