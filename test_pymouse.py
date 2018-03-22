# coding: utf-8

'''早知道这个模块，当时就不会和pywin32死磕了。。。'''

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()

# x_dim, y_dim = m.screen_size()
# m.click(x_dim/2, y_dim/2, 1)
# k.type_string('Hello, World!')

def _fix_one(url):

    # 需要当前处在52配置页面

    # 点击url框
    m.click(584, 143, 1)
    time.sleep(0.2)
    m.click(584, 143, 1)
    time.sleep(0.2)
    m.click(584, 143, 1)
    time.sleep(0.2)

    # 输入需要修改的url
    k.type_string(url)

    # 点击搜索按钮, 点击修改
    m.click(1857, 156, 1)
    time.sleep(0.5)
    m.click(1871, 294, 1)
    time.sleep(0.2)
# with open(r'C:\Users\viruser.v-desktop\Desktop\result.txt', 'r') as f:
#     print f.readlines()

k.press_key(k.alt_key)
time.sleep(0.2)
k.tap_key(k.tab_key)
time.sleep(0.2)
k.release_key(k.alt_key)
time.sleep(0.2)

_fix_one('http://changsha.pbc.gov.cn/changsha/130009/index.html')

