## Alex Parys
## Python C4 Activity 4 - Session 4.15 
## 2/7/2019
##Extra Credit
##modelist.py

def mode(alist):
    countdict = {}
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
            
    countlist = countdict.values()
    maxcount = max(countlist)
    modelist = []
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    return modelist
