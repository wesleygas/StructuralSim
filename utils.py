#Biblioteca de funcoes uteis
import math
# import numpy as np

class node():
    def __init__(self,name, x,y):
        self.name = name
        self.x = x
        self.y = y
        self.freeX = True
        self.freeY = True
        self.loadX = 0
        self.loadY = 0
    
    def setFreedomX(self,freeX):
        self.freeX = freeX

    def setFreedomY(self,freeY):
        self.freeY = freeY

    def setLoadX(self,loadX):
        self.loadX = loadX

    def setLoadY(self,loadY):
        self.loadY = loadY
    
    def printProperties(self):
        print(self.x)
        print(self.y )
        print(self.freeX)
        print(self.freeY)
        print(self.loadX)
        print(self.loadY)


def barLength(pointA,pointB):
    return math.sqrt((pointA.x - pointB.x)**2 + (pointA.y-pointB.y)**2)

def calcEal(E,A,l):
    return E*A/l

def angle(pointA,pointB):
    if(pointB.x-pointA.x == 0):
        return math.pi/2
    return math.atan((pointB.y-pointA.y) / (pointB.x-pointA.x))

def matrixKe(E,A,l,pointA,pointB):
    eal = calcEal(E,A,l)

    s = math.sin(angle(pointA,pointB))
    c = math.cos(angle(pointA,pointB))

    if (c < 0.00000000001):
        c = 0
    if (s < 0.00000000001):
        s = 0

    matrix = [[eal*c**2,eal*c*s,-eal*c**2,-eal*c*s],
            [eal*c*s,eal*s**2,-eal*c*s,-eal*s**2],
            [-eal*c**2,-eal*c*s,eal*c**2,eal*c*s],
            [-eal*c*s,-eal*s**2,eal*c*s,eal*s**2]]

    return matrix