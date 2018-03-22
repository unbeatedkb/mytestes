# coding: utf-8

class A(object):


    x = []
    y = 0
    z = {}

    def __init__(self):
    #     self.x = []
        self.y = 1
    #     self.z = {}

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
    a.add()
    # A.y += 1
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


'''
结论
    1. 定义的类属性，其实例对象也可以访问。对类属性的值进行修改，其对象属性的值也会随着修改。对实例对象属性进行修改，类属性的值不会变动。但是当类属性为列表或者字典时，修改实例属性的操作也会对类属性生效。
    2. 使用self前缀定义的实例属性。使用类无法访问。
    3. 当类属性和对象属性同时定义的时候，最先访问到的是对象属性。
'''