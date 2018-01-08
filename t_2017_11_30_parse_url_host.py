# coding: utf-8


import string
from tld import get_tld
from urlparse import urlparse
import re


def parse_hosts(url):
    try:
        return get_tld(url)
    except Exception as e:
        host = urlparse(url).netloc
        if host:
            return host
        else:
            # return re.findall('', string)[0]
            return None

def parse_by_rex(url):
    topHostPostfix = (
    '.com','.la','.io','.co','.info','.net','.org','.me','.mobi',
    '.us','.biz','.xxx','.ca','.co.jp','.com.cn','.net.cn',
    '.org.cn','.mx','.tv','.ws','.ag','.com.ag','.net.ag',
    '.org.ag','.am','.asia','.at','.be','.com.br','.net.br',
    '.bz','.com.bz','.net.bz','.cc','.com.co','.net.co',
    '.nom.co','.de','.es','.com.es','.nom.es','.org.es',
    '.eu','.fm','.fr','.gs','.in','.co.in','.firm.in','.gen.in',
    '.ind.in','.net.in','.org.in','.it','.jobs','.jp','.ms',
    '.com.mx','.nl','.nu','.co.nz','.net.nz','.org.nz',
    '.se','.tc','.tk','.tw','.com.tw','.idv.tw','.org.tw',
    '.hk','.co.uk','.me.uk','.org.uk','.vg', ".com.hk")

    regx = r'[^\.]+('+'|'.join([h.replace('.',r'\.') for h in topHostPostfix])+')$'
    pattern = re.compile(regx, re.IGNORECASE)
    # parts = urlparse(url)
    # host = parts.netloc
    m = pattern.search(url)
    res = m.group() if m else url
    return res


if __name__ == "__main__":
    
    with open('files/t1', 'r') as f:
        urls = f.readlines()

    for url in urls:
        url = url.strip()
        print url
        # print parse_hosts(url)
        print parse_by_rex(url)
