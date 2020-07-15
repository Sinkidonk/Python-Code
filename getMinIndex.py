## Alex Parys
## Python Exercises 4.14 to 4.15
## 2/7/2019

def getMin(alist):
    minSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] < minSoFar:
            minSoFar = alist[pos]
    return minSoFar
