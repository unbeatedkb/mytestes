# coding: utf-8

import signal, os, time
def handler(signum, frame):
    print 'Yes , Received', signum

signal.signal(signal.SIGINT, handler)
print 'My process Id' , os.getpid()

while True:
    print 'Waiting for signal'
    try:
        time.sleep(5)
    except InterruptedError:
        pass