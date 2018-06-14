# coding: utf-8

class Singleton(object):
 
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
                                                                               
                                                                               
class URL(Singleton):

    def __init__(self, url):
        self.url = url
        
    def show(self):
        print(self.url)
        
        

au = URL('http')
iu = URL('https')
au.show()
iu.show()
print(id(au))
print(id(iu))
