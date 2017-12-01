# coding: utf-8

import sys  
def get_cur_info():  
    print sys._getframe().f_code.co_filename # 当前文件名，可以通过__file__获得  
    print sys._getframe().f_code.co_name # 当前函数名  
    print sys._getframe().f_lineno # 当前行号  
    print sys._getframe(1).f_code.co_name # 上一个函数名
    print sys._getframe()
    
def test():
    get_cur_info()  
   
   
test()   