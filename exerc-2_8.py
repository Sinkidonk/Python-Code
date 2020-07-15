##Alex Parys
## Exercises 2.8
## the Sum of the first 100 even numbers
##1/23/2019
firstNum=1
lastNum=100
acc=0
for x in range(firstNum,lastNum+1):
    if(x % 2 == 0):
        print(x)
        acc += x
print(acc)
