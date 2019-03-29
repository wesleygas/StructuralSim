import utils
import bar
import dataIngest as di
import numpy as np
import math

entrada = input("Nome do arquivo de entrada: ")
data = di.get_data(entrada+".txt")
node_data = di.data_parse(data)
list_bars, dict_bars = di.join_bars(*node_data)

# global matrix and degrees of freedom list
matrix_g, matrix_cut, force_list, free_dict = utils.matrixG(dict_bars,len(node_data[0]["COORDINATES"]))

dis_matrix_cut = utils.gauss_rules(matrix_cut,force_list, 10e2, 10e-32)

dis_matrix_g = utils.expandDisplacementMatrix(free_dict,dis_matrix_cut, len(matrix_g))

complete_load_list = np.dot(matrix_g, dis_matrix_g)

for barra in list_bars:
    us = []

    s = math.sin(barra.angle)
    c = math.cos(barra.angle)

    if (c < 0.00000000001):
        c = 0
    if (s < 0.00000000001):
        s = 0

    matrixCoef = [-c,-s,c,s]
    
    us = [dis_matrix_g[((barra.p1.name)*2)-2],
          dis_matrix_g[((barra.p1.name)*2)-2],
          dis_matrix_g[((barra.p2.name)*2)-2],
          dis_matrix_g[((barra.p1.name)*2)-1]]

    mult = np.dot(matrixCoef,us)
    barra.strain = (1/(barra.length))*mult
    barra.stress = (barra.E_modulus/(barra.length))*mult

nodes = node_data[0]["COORDINATES"]


utils.write_exit(dis_matrix_g,nodes,np.around(complete_load_list, decimals = 5),list_bars)

print("\n\nVerifique o arquivo de saída:\nsaida.txt")