# coding: utf-8

'''
exec use import in functions
'''



def thefc(thestr):
    # exec(thestr)
    exec(thestr, globals())
    print dealvalue()


funstr = '''
import time
def dealvalue():
    return int(time.time())
    # return int(111)
'''


thefc(funstr)