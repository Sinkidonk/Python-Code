## Alex Parys
## Python Exercises 5.1
## 2/13/2019

##Write a program to read the rainfall.txt file and then write out a new file called rainfallfmt.txt.
##The new file should format each line so that the city is right-justified in a field that is 25 characters wide,
##and the rainfall data should be printed in a field that is 5 characters wide with 1 digit to the right of the decimal point.

from pprint import pprint

rainfile = open ("rainfall.txt","r")

outfile = open ("rainfallfmt.txt","w")

for aline in rainfile:
    values = aline.split()
    numval = float(values[1])
    outfile.write("%+25s %5.1f \n" %(values[0], numval))
rainfile.close()
outfile.close()
