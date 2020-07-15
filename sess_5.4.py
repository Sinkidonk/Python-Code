## Alex Parys
## Python C5 Activity 3 - Session 5.4
## 2/13/2019

infile = open("rainfall.txt","r")
aline = infile.readline()
print(aline)

infile = open("rainfall.txt","r")

linelist = infile.readlines()

print(linelist)



infile = open("rainfall.txt","r")

filestring = infile.read()

print(filestring)