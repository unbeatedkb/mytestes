class Human:
    # 成员属性
    name = None
    sex = None
    age = None
    
    # 成员方法
    # 对象初始化
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    # 访问不存在成员时触发
    def __getattr__(self,attr):
        print('触发了__getattr__(),要访问对象的{}成员'.format(attr))
        return '访问成员不存在'
        pass
    # 访问成员的时候触发
    def __getattribute__(self,attr):
        print('触发了__getattribute__(),要访问对象的{}成员'.format(attr))
        # 一定不能使用self.__getattribute__(self,attr),否则会导致递归死循环，使用object的方法访问
        if attr in ('name','sex','age','height','test'):
            return object.__getattribute__(self,attr)
        else :
            return '返回默认值'
    # 测试方法
    def test(self):
        print('调用测试方法test')

xm = Human('小明','男',18)
print(xm.name)
print(xm.test)
print()
xm.test()
print(xm.wight)
print('\n####################################################################\n')
print(xm.height)

