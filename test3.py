from functools import partial

def a():
    pass
a.args = 1

print(a.args)
