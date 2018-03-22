# coding: utf-8

import logging


class ac(object):
    
    def __init__(self):
        self.username = 'dakb'
        self.password = 'newkb'
    
    
def logdec(func):
    def wrapper(theself):
        logging.error(theself.account.username)
        logging.warn(theself.account.password)
        return func(theself)
    return wrapper
    
    
class tac(object):
    
    def __init__(self):
        self.account = ac()
    
    @logdec
    def process(self):
        
        logging.error('what a day!')
        return 1, 2
        

t = tac()
d1, d2 = t.process()        
print d1, d2