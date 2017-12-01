# coding: utf-8

import threading
import time

class Test(object):
    
    zz = None
    def __init__(self):
        
        self.count = 0
        t = threading.Thread(target=self.check, args=())
        t.start()
        if not self.zz:
            print 1
    
    def check(self):
        while True:
            if self.count == 5:
                self.release()
                self.count = 0
            time.sleep(1)
            self.count += 1
    
    def release(self):
        print 'release'
        
        
    def do(self):

        print 'oh my gad!'
        
        
t = Test()
t.do()