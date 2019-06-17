# coding: utf-8

def create_multipliers1():
    return [lambda x : i * x for i in range(5)]

def create_multipliers2():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)

    return multipliers    
    

for multiplier in create_multipliers1():
    print multiplier(2)
    

for multiplier in create_multipliers2():
    print multiplier(2)    