from utils import *

pontoA = node(1,0,0)
pontoB = node(2,0,0.4)
pontoC = node(3,0.3,0.4)


c1 = barLength(pontoA,pontoB)
c2 = barLength(pontoA,pontoC)
c3 = barLength(pontoB,pontoC)

# print("c1: {0}\nc2: {1}\nc3: {2}".format(c1,c2,c3))

cc1 = calcEal(210*10**9,2*10**(-4),c1)
cc2 = calcEal(210*10**9,2*10**(-4),c2)
cc3 = calcEal(210*10**9,2*10**(-4),c3)

# print("c1: {0}\nc2: {1}\nc3: {2}".format(cc1,cc2,cc3))

matriz1 = matrixKe(210*10**9,2*10**(-4),c1,pontoA,pontoB)
matriz2 = matrixKe(210*10**9,2*10**(-4),c3,pontoB,pontoC)

print("matriz1:\n{0}\n\nmatriz2:\n{1}".format(matriz1,matriz2))