# coding: utf-8

import MySQLdb

class msclient(object):
    
    instance = None
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.db = 'newtest'
        self.cursor = MySQLdb.connect(self.host, self.user, self.password, self.db)
        
    @classmethod
    def getcursor(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls().cursor
            cls.instance = obj
            return obj


class Singleton(object):
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Msclient1(Singleton):
    
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.db = 'newtest'
        self.cursor = MySQLdb.connect(self.host, self.user, self.password, self.db)
    
    


if __name__ == "__main__":

    cr1 = msclient.getcursor()
    cr2 = msclient.getcursor()
    print cr1, cr2            
    
    mcr1 = Msclient1()
    mcr2 = Msclient1()
    print mcr1, mcr2
