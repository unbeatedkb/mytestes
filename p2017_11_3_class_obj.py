# coding: utf-8

class A:

    x = []
    y = 0

    def add(self):
        self.x.append('1')
        self.y += 1
        
        
a=A() 
print '==============='
print a.x, a.y
print A.x, A.y

print '==============='
a.add()
print a.x, a.y
print A.x, A.y

print '==============='
b=A() 
print b.x, b.y
print A.x, A.y