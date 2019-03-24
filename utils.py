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

def matrixG(bars,len_nodes):
    g_matrix = [[0]*2*len_nodes]*2*len_nodes
    for bar in bars:
        p1_y = ((bars[bar].p1.name)*2) -1 #Valor do indice impar ou seja X menor da barra
        p1_x = p1_y-1 #Valor do indice impar ou seja X menor da barra
        p2_y = ((bars[bar].p2.name)*2) -1 #Valor do indice impar ou seja X menor da barra
        p2_x = p2_y-1 #Valor do indice impar ou seja X menor da barra
        
        print(p1_x,p1_y,p2_x,p2_y)

        matrix_bar = bars[bar].matrix_ke

        g_matrix[p1_x][p1_x] += matrix_bar[0][0]
        g_matrix[p1_x][p1_y] += matrix_bar[0][1]
        g_matrix[p1_x][p2_x] += matrix_bar[0][2]
        g_matrix[p1_x][p2_y] += matrix_bar[0][3]

        g_matrix[p1_y][p1_x] += matrix_bar[1][0]
        g_matrix[p1_y][p1_y] += matrix_bar[1][1]
        g_matrix[p1_y][p2_x] += matrix_bar[1][2]
        g_matrix[p1_y][p2_y] += matrix_bar[1][3]

        g_matrix[p2_x][p1_x] += matrix_bar[2][0]
        g_matrix[p2_x][p1_y] += matrix_bar[2][1]
        g_matrix[p2_x][p2_x] += matrix_bar[2][2]
        g_matrix[p2_x][p2_y] += matrix_bar[2][3]

        g_matrix[p2_y][p1_x] += matrix_bar[3][0]
        g_matrix[p2_y][p1_y] += matrix_bar[3][1]
        g_matrix[p2_y][p2_x] += matrix_bar[3][2]
        g_matrix[p2_y][p2_y] += matrix_bar[3][3]
    # print(g_matrix)
        # if (bars[bar].p1.freeX):
        #     bars[bar].matrix_ke[((bars[bar].p1.name)*2)-2]
        # if (bars[bar].p1.freeY):
        #     pass
        # if (bars[bar].p2.freeX):
        #     pass
        # if (bars[bar].p2.freeY):
        #     pass