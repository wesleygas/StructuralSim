from utils import node
from bar import Barra
import pprint
#Codigo para o parseamento dos dados de input
with open("input_file.txt") as file: # Use file to refer to the file object
	data = file.readlines()

data = [item.strip('\n') for item in data]
def join_bars(input_dict, group_to_bar):
	list_bars = []
	for bar in group_to_bar:
		# group_to_bar[bar]
		nome = group_to_bar[bar]
		p1 = input_dict["COORDINATES"][input_dict["INCIDENCES"][nome][0]]
		p2 = input_dict["COORDINATES"][input_dict["INCIDENCES"][nome][1]]
		E_modulus = input_dict["ELEMENT_GROUPS"][nome]["E_MODULUS"]
		strain = input_dict["ELEMENT_GROUPS"][nome]["TR_ADM"]
		stress = input_dict["ELEMENT_GROUPS"][nome]["COM_ADM"]
		cs_area = input_dict["ELEMENT_GROUPS"][nome]["AREA"]
		list_bars.append(Barra(nome, p1, p2, E_modulus, strain, stress, cs_area))


	return list_bars


x = 0
qnt = 0
total_bars = 0
input_dict = {}
group_to_bar = {}



while x < len(data):
	# print(data[x])
	if(data[x][0] =="*"):
		command = data[x][1:]
		
		if(command == "COORDINATES" ):
			input_dict["COORDINATES"] = {}
			qnt = int(data[x+1])
			for cord in (data[(x+2):(x+2+qnt)]):
				cord_split = cord.split(" ")
				input_dict["COORDINATES"][int(cord_split[0])] = node(float(cord_split[1]),float(cord_split[2]))


		elif(command == "ELEMENT_GROUPS" ):
			input_dict["ELEMENT_GROUPS"] = {}
			qnt = int(data[x+1])
			number_bar = 1
			
			for group in (data[(x+2):(x+2+qnt)]):
				group_split = group.split(" ")
				group_num = int(group_split[0])
				amount_bars = int(group_split[1])
				total_bars += amount_bars
				input_dict["ELEMENT_GROUPS"][group_num] = {}
				input_dict["ELEMENT_GROUPS"][group_num]["N_BARS"] = amount_bars
				input_dict["ELEMENT_GROUPS"][group_num]["TYPE"] = group_split[2]

				for i in range(amount_bars):
					group_to_bar[number_bar] = group_num
					number_bar+=1
		
		
		elif(command == "INCIDENCES" ):
			input_dict["INCIDENCES"] = {}
			for bar in (data[(x+1):(x+1+total_bars)]):
				bar_split = bar.split(" ")
				input_dict["INCIDENCES"][int(bar_split[0])] = []
				input_dict["INCIDENCES"][int(bar_split[0])].append(int(bar_split[1]))
				input_dict["INCIDENCES"][int(bar_split[0])].append(int(bar_split[2]))


		elif(command == "MATERIALS" ):
			qnt = int(data[x+1])
			group_num = 1
			for material in (data[(x+2):(x+2+qnt)]):
				material_split = material.split(" ")
				input_dict["ELEMENT_GROUPS"][group_num]["E_MODULUS"] = material_split[0] #Módulo de Elasticidade
				input_dict["ELEMENT_GROUPS"][group_num]["TR_ADM"] = material_split[1] # Tração máxima admissivel
				input_dict["ELEMENT_GROUPS"][group_num]["COM_ADM"] = material_split[2] # Compresão máxima admissivel
				group_num +=1

		elif(command == "GEOMETRIC_PROPERTIES" ):
			qnt = int(data[x+1])
			group_num = 1
			for material in (data[(x+2):(x+2+qnt)]):
				material_split = material.split(" ")
				input_dict["ELEMENT_GROUPS"][group_num]["AREA"] = material_split[0] 
				group_num +=1

		elif(command == "BCNODES" ):
			qnt = int(data[x+1])
			
			for constrain in (data[(x+2):(x+2+qnt)]):
				constrain_split = constrain.split(" ")
				cord_num = int(constrain_split[0])
				if(constrain_split[1] == '1'):
					(input_dict["COORDINATES"][cord_num]).setFreedomX(False)
					
				elif(constrain_split[1] == '2'):
					(input_dict["COORDINATES"][cord_num]).setFreedomY(False)

		elif(command == "LOADS"):
			qnt = int(data[x+1])
			for constrain in (data[(x+2):(x+2+qnt)]):
				constrain_split = constrain.split(" ")
				cord_num = int(constrain_split[0])

				if(constrain_split[1] == '1'):
					(input_dict["COORDINATES"][cord_num]).setLoadX(int(constrain_split[2]))
					
				elif(constrain_split[1] == '2'):
					(input_dict["COORDINATES"][cord_num]).setLoadY(int(constrain_split[2]))
				
	x+=1
# print(input_dict)
# for cord in input_dict["COORDINATES"]:
# 	input_dict["COORDINATES"][cord].printProperties()
# 	print("----------")
# pprint.pprint(input_dict, width=1)
# pprint.pprint(group_to_bar, width=1)
bars = join_bars(input_dict, group_to_bar)
print(bars)