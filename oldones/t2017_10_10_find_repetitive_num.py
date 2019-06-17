# coding: utf-8

'''find the number'''

def getthenum(array):
    # this method is not so well
    sum = 0
    for i in array:
        strb = str(bin(i))
        theb = int(strb[2:])
        sum += theb
    thestr = ''
    for i in str(sum):
        if int(i) % 3 == 0:
            thestr += '0'
        else:
            thestr += '1'
    thenum = int(thestr, 2)
    return thenum
    

def getthenumbysort(array):
    
    # it is not a good method
    array = sorted(array)
    for i in xrange(len(array)):
        if i == 0:
            if array[i] != array[i+1]:
                return array[i]
        elif i == len(array)-1:
            if array[i] != array[i-1]:
                return array[i]
        else:
            if array[i] != array[i-1] and array[i] != array[i+1]:
                return array[i]
    
    
if __name__ == "__main__":
        
    array = [1, 2, 1, 2, 1, 2, 12167]
    
    print getthenum(array)
    print getthenumbysort(array)