# coding: utf-8

import time
import datetime
import threading
import thread

def doprint(thestr):
    while True:
        print(thestr + str(datetime.datetime.now()))
        time.sleep(1)



def main():

    # 使用thread模块 start_new_thread的方式 ，需要在其后面设置等待时间，不然不会运行，设置等待时间之后
    thread.start_new_thread(doprint, ('t1', ))
    time.sleep(20)

    # t = threading.Thread(target=doprint, args=('t1', ))
    # t.start()
    
    print 11111111




main()    
