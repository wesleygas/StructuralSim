#Biblioteca de funcoes uteis
import math
import numpy as np

class node():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.freeX = True
        self.freeY = True

def barLength(pointA,pointB):
    return math.sqrt((pointA.x - pointB.x)**2 + (pointA.y-pointB.y)**2)

def calcEal(E,A,l):
    return E*A/l

def angle(pointA,pointB):
    return math.atan2((pointA.y-pointB.y) , (pointA.x-pointB.x))

def matrixKe(E,A,l,pointA,pointB):
    eal = calcEal(E,A,l)

    s = math.sin(angle(pointA,pointB))
    c = math.cos(angle(pointA,pointB))

    matrix = [[c**2,c*s,-c**2,-c*s],
            [c*s,s**2,-c*s,-s**2],
            [-c**2,-c*s,c**2,c*s],
            [-c*s,-s**2,c*s,s**2]]

    return eal * matrix