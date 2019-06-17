# coding: utf-8

# python中单例模式的若干实现方法

# 使用模块来实现单例
# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
from test_mysingleton import my_singleton


# 使用__new__来实现单例
class Singleton(object):
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# def test1():
#     class MyClass(Singleton):
#         a = 1

#     one = MyClass()
#     two = MyClass()
#     print one == two
#     print one is two
#     print id(one), id(two)

# test1()


# 使用装饰器来实现单例
from functools import wraps

def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance

# @singleton
# class MyClass2(object):
#     a = 1

# def test2():
#     one = MyClass2()
#     two = MyClass2()
#     print one == two
#     print one is two
#     print id(one), id(two)

# test2()


# 使用metaclass 元类来实现

class MSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass3(object):
    
    __metaclass__ == MSingleton
    a = 1


def test3():
    one = MyClass3()
    two = MyClass3()
    print one == two
    print one is two
    print id(one), id(two)

test3()



















