##Chapter 1
##Listing 1.5
##C1 Activity 5 - Polygons
##Alex Parys
##1/8/2019

def drawPolygon(myTurtle,sideLength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)
