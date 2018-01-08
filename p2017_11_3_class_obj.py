# coding: utf-8

class A(object):

    x = []
    y = 0
    z = {}
    def add(self):
        self.x.append('1')
        self.y += 1
        # A.y += 1
        
def test1():
    a=A() 
    print '==============='
    print a.x, a.y
    print A.x, A.y

    print '==============='
    # a.add()
    A.y += 1
    print a.x, a.y
    print A.x, A.y

    print '==============='
    b=A() 
    print b.x, b.y
    print A.x, A.y

    print '==============='
    print a.x is b.x
    print a.y is b.y

def test2():
    a = A()
    b = A()
    print a.z, b.z
    a.z['x'] = 'xixi'
    print a.z, b.z
    
    


test1()