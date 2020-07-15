## Alex Parys
## Python Exercises 4.14 to 4.15
## 2/7/2019

def getMin3(alist):
    minSoFar = alist[0]
    for item in alist[1:]:
        if item < minSoFar:
            minSoFar = item
    return minSoFar
