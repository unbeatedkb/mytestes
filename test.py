from threading import local

class Test:

    def __getattribute__(self, item):

        raise AttributeError

    def __getattr__(self, item):
        return 1


t = Test()
print(t.a)
