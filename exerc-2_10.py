##Alex Parys
## Exercises 2.10
## the average of the first 100 odd numbers
##1/23/2019

firstNum=1
lastNum=100
total=0
acc=0
average=0
for x in range(firstNum,lastNum+1):
    if(x % 2 != 0):
        print(x)
        acc += x
        total += 1
average = acc/total
print(average)
