# coding: utf-8

try:
    a = 1 / 0
except ZeroDivisionError:
    print 1
except:
    print 2

