## Alex Parys
## Python Exercises 4.23
## 2/7/2019

def median(alist):
    copylist = alist[:] # make a copy using slice operator
    copylist.sort()
    if len(copylist)%2 == 0:
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid]+ copylist[rightmid])/2
    else:
        mid = len(copylist)//2
        median = copylist[mid]
    return median
