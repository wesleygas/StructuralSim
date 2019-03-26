import utils
import bar
import dataIngest as di
import numpy as np
import math


data = di.get_data("input_file.txt")
list_bars, dict_bars = di.join_bars(*di.data_parse(data))

# global matrix and degrees of freedom list
matrix_g, matrix_cut, force_list, free_dict = utils.matrixG(dict_bars,len(di.data_parse(data)[0]["COORDINATES"]))

#print('\n'.join(map(str, matrix_cut)))
#print(force_list)
dis_matrix_cut = utils.gauss_rules(matrix_cut,force_list, 10e4, 10e-16)

dis_matrix_g = utils.expandDisplacementMatrix(free_dict,dis_matrix_cut, len(matrix_g))

complete_load_list = np.dot(matrix_g, dis_matrix_g)

print(dis_matrix_g)
print("us")
for barra in list_bars:
    us = []

    s = math.sin(barra.angle)
    c = math.cos(barra.angle)
    matrixCoef = [-c,-s,c,s]

    us.append(dis_matrix_g[((barra.p1.name)*2)-2])
    us.append(dis_matrix_g[((barra.p1.name)*2)-1])
    us.append(dis_matrix_g[((barra.p2.name)*2)-2])
    us.append(dis_matrix_g[((barra.p1.name)*2)-1])
    mult = np.dot(matrixCoef,us)
    barra.strain = (1/(barra.length))*mult
    barra.stress = (barra.E_modulus/(barra.length))*mult
    

    # print(us)
##Reações de apoio 