import grequests
import requests
import time

urls = ["http://www.baidu.com"] * 100

def async_t():
    start = time.time()
    def handler(request, exception):
        print(exception)

    rs = (grequests.get(u) for u in urls)
    res = grequests.map(rs)
    print(res)
    print("%.7f" % (time.time() - start))

session = requests.session()
def sync_t():
    start = time.time()
    res = []
    for u in urls:
        res.append(session.get(u))
    #res = (requests.get(u) for u in urls)
    print(res)
    print("%.7f" % (time.time() - start))

async_t()
sync_t()

