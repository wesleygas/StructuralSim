# Biblioteca de funcoes uteis
import math
import numpy as np


class node():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.freeX = True
        self.freeY = True
        self.loadX = 0
        self.loadY = 0
        self.deslX = 0
        self.deslY = 0

    def defineDesl(self,x,y):
        self.deslX = x
        self.deslY = y
    def setFreedomX(self, freeX):
        self.freeX = freeX

    def setFreedomY(self, freeY):
        self.freeY = freeY

    def setLoadX(self, loadX):
        self.loadX = loadX

    def setLoadY(self, loadY):
        self.loadY = loadY

    def printProperties(self):
        print(self.x)
        print(self.y)
        print(self.freeX)
        print(self.freeY)
        print(self.loadX)
        print(self.loadY)


def barLength(pointA, pointB):
    return math.sqrt((pointA.x - pointB.x)**2 + (pointA.y-pointB.y)**2)


def calcEal(E, A, l):
    return (E*A)/l


def angle(pointA, pointB):
    if(pointB.x-pointA.x == 0):
        return math.pi/2
    return math.atan((pointB.y-pointA.y) / (pointB.x-pointA.x))


def matrixKe(E, A, l, pointA, pointB):
    eal = calcEal(E, A, l)

    c = (pointB.x - pointA.x)/float(l)
    s = (pointB.y - pointA.y)/float(l)

    matrix = np.array([[c**2, c*s, -c**2, -c*s],
              [c*s, s**2, -c*s, -s**2],
              [-c**2, -c*s, c**2, c*s],
              [-c*s, -s**2, c*s, s**2]])

    return matrix*eal


def matrizGZero(n):
    matrix = []
    for _ in range(2*n):
        matrix.append([0]*(2*n))

    return matrix


def matrixG(bars, len_nodes):
    g_matrix = matrizGZero(len_nodes)
    cut_matrix = []
    free_dict = {}
    force_list = []
    for bar in bars:
        # Valor do indice impar ou seja X menor da barra
        p1_y = ((bars[bar].p1.name)*2) - 1
        p1_x = p1_y-1  # Valor do indice impar ou seja X menor da barra
        # Valor do indice impar ou seja X menor da barra
        p2_y = ((bars[bar].p2.name)*2) - 1
        p2_x = p2_y-1  # Valor do indice impar ou seja X menor da barra

        # adicionando os graus de liberdade livres na lista
        if(bars[bar].p1.freeX and (p1_x not in free_dict)):
            free_dict[p1_x] = bars[bar].p1.loadX
        if(bars[bar].p1.freeY and (p1_y not in free_dict)):
            free_dict[p1_y] = bars[bar].p1.loadY
        if(bars[bar].p2.freeX and (p2_x not in free_dict)):
            free_dict[p2_x] = bars[bar].p2.loadX
        if(bars[bar].p2.freeY and (p2_y not in free_dict)):
            free_dict[p2_y] = bars[bar].p2.loadY

        # print(p1_x,p1_y,p2_x,p2_y)
        matrix_bar = bars[bar].matrix_ke
        # if(p1_y ==3 or p2_y ==3):
        #     print(matrix_bar)
        #     print("\n\n\n")
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
    
    for i in range(2*len_nodes):
        line = []
        for j in range(2*len_nodes):
            if((i in free_dict.keys()) and (j in free_dict.keys())):
                line.append(g_matrix[i][j])

        if(i in free_dict):
            force_list.append(free_dict[i])
        
        if(len(line) > 0):
            cut_matrix.append(line)

    return g_matrix, cut_matrix, force_list, free_dict

def gauss_helps(rig,desl,loads):
    for i in range(len(desl)):
        desl[i] = loads[i]
        for j in range(len(desl)):
            if(j != i):
                desl[i] -= rig[i][j]*desl[j]
        desl[i] /= rig[i][i]
        
    return desl

##
#
# rig - Matriz de rigidez
# loads - Matriz de cargas
# i_max - Numero máximo de iteracoes
# tolerance - tolerancia... daaa
#
# Returns: desl - Matriz de deslocamento nodal (unidimensional de mesmo tamanho que a matrix de cargas)
##
def gauss_rules(rig, loads, i_max, tolerance):
    desl = np.ones(len(loads))
    if((len(rig) != len(loads)) or len(rig[0]) != len(desl)):
        return -1
    desl = gauss_helps(rig,desl,loads)
    p_desl = np.array(desl)
    
    i = 1
    while(i < i_max):
        desl = gauss_helps(rig, desl, loads)
        delta = np.zeros(len(desl))
        for e in range(len(desl)):
            if(desl[e] == 0 and p_desl[e] == 0):
                delta[e] = 0
            else:
                delta[e] = 2*(desl[e]-p_desl[e])/(np.abs(desl[e]) + np.abs(p_desl[e]))
        if(np.abs(np.max(delta)) < tolerance):
            return desl
        p_desl = np.array(desl)
        i+= 1
    return desl

def expandDisplacementMatrix(free_dict, input_matrix, size):
    output_matrix = np.zeros(size)
    i = 0
    for key in sorted(free_dict.keys()):
        output_matrix[key] = input_matrix[i]
        i+=1
    return output_matrix


def write_exit(us,nodes,forces,list_bars):
    exit = open("saida.txt","w")

    exit.write("*DISPLACEMENTS\n")
    
    counter = 1
    pointer = 0
    while counter <= len(us)/2:
        exit.write("    {0} {1} {2}\n".format(counter,us[pointer],us[pointer+1]))
        counter += 1
        pointer += 2
        
    exit.write("\n*REACTION FORCES\n")
    
    counter = 0
    for node in nodes:
        if (not nodes[node].freeX):   
            exit.write("    {0} FX = {1}\n".format(nodes[node].name,forces[counter]))
        counter += 1
        if (not nodes[node].freeY):   
            exit.write("    {0} FY = {1}\n".format(nodes[node].name,forces[counter]))
        counter += 1
    
    exit.write("\n*ELEMENT_STRAINS\n")

    counter = 1
    for bar in list_bars:
        exit.write("    {0} {1}\n".format(counter,bar.strain))
        counter += 1

    exit.write("\n*ELEMENT_STRESSES\n")

    counter = 1
    for bar in list_bars:
        exit.write(("    {0} {1} "+ bar.get_strain_stress_string() + " " +bar.String_calcIdealDimension(1.2) + "\n").format(counter,bar.stress))
        counter += 1
    exit.close()