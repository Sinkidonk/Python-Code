##Chapter 1
##drawSpiral
##Alex Parys
##1/9/2019

def drawSpiral(myTurtle,maxSide):
    for sideLength in range(1,maxSide +1 ,5):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
