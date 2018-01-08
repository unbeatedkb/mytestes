# coding: utf-8

import threading
import datetime
import time

class Basic(object):

    check_thread = None
    
    def __init__(self):
        if not Basic.check_thread:
            print 111
            Basic.check_thread = threading.Thread(target=self.checkuse, args=())
            Basic.check_thread.start()
        else:
            print Basic.check_thread
            if not Basic.check_thread.is_alive():
                Basic.check_thread = threading.Thread(target=self.checkuse, args=())
                Basic.check_thread.start()

    # def client

    def checkuse(self):
        i = 0
        while True:
            if i > 10:
                break
            print datetime.datetime.now()
            time.sleep(10)
            i += 20

b = Basic()
c = Basic()
