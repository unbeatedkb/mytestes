# coding: utf-8


from selenium import webdriver
import time
import re

driver = webdriver.Chrome('D:\code\chromedriver_win32\chromedriver.exe')

f_urls = open('files/gs_bc_urls_num', 'w')
# f_urls.close()


def parse_num(body):
    try:
        pt = u'分<b>(\d+?)</b>页'
        return re.search(pt, body).group(1)
    except:
        pt = u'分(\d+?)页'
        return re.search(pt, body).group(1)

def insanely_press_next(driver, nums=200):
    for i in range(int(nums)):
        try:
            driver.find_element_by_link_text(u'下一页').click()
        except:
            return
        

def get_one(driver, url):
    word = ''
    driver.get(url)
    time.sleep(1)
    word += url+' '
    try:
        # insanely_press_next(driver, 300)
        # word += driver.current_url+' '
        driver.find_element_by_link_text(u'下一页').click()
        time.sleep(0.5)
        driver.find_element_by_link_text(u'下一页').click()
        time.sleep(0.5)
        word += driver.current_url+' '
        nums = parse_num(driver.page_source)
        word += nums+' '
        print word
    except:
        import traceback
        traceback.print_exc()
        print 'cannot find'
    f_urls.write(word+'\n')


with open('files/t2', 'r') as f:
    for l in f.readlines():
        if l:
            url = l.strip()
            try:
                # import pdb; pdb.set_trace()
                get_one(driver, url)
            except:
                pass

f_urls.close()
driver.quit()