import utils
import bar
import dataIngest as di
import numpy as np


data = di.get_data("input_file.txt")
list_bars, dict_bars = di.join_bars(*di.data_parse(data))

# global matrix and degrees of freedom list
matrix_g, matrix_cut, force_list, free_dict = utils.matrixG(dict_bars,len(di.data_parse(data)[0]["COORDINATES"]))

#print('\n'.join(map(str, matrix_cut)))
#print(force_list)
dis_matrix_cut = utils.gauss_rules(matrix_cut,force_list, 10e4, 10e-16)

dis_matrix_g = utils.expandDisplacementMatrix(free_dict,dis_matrix_cut, len(matrix_g))

complete_load_list = np.dot(matrix_g, dis_matrix_g)


##Reações de apoio 