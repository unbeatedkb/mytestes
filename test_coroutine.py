def calaver():
    average = 0
    count = 1
    total = 0
    while True:
        num = yield average
        total += num
        average = total/count
        count += 1
        
        
t = calaver()
next(t)
print t.send(10)
print t.send(20)
print t.send(300)
print t.send(20)
