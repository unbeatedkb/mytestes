# coding: utf-8


from pydoc import locate


thet = 'int'

c = '1212121'

print locate(thet)(c)


try:

    print int(thet)
except ValueError:
    print 'xixi'