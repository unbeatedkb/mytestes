# coding: utf-8

from selenium import webdriver
import traceback

def initdriver():
    phantomjs_path = "D:/code/newsina/phantomjs-2.1.1-windows/bin/phantomjs.exe"
    proxy = '101.71.41.166'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Connection': 'keep-alive'
    }
    for key, value in headers.iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
    webdriver.DesiredCapabilities.PHANTOMJS[
        'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    service_args = [
        '--proxy={proxy}:888'.format(proxy=proxy),
        '--proxy-type=socks5/http',
        '--proxy-auth=hexin:hx300033',
    ]
    try:
        driver = webdriver.PhantomJS(service_args=service_args, executable_path=phantomjs_path)
    except:
        traceback.print_exc()
    driver.set_window_size(1400, 1000)
    return driver
    

driver = initdriver()    

    