import utils
import bar
import dataIngest as di


data = di.get_data("input_file.txt")
list_bars, dict_bars = di.join_bars(*di.data_parse(data))

# print(len(di.data_parse(data)[0]["COORDINATES"]))

# print(dict_bars)
# for bars in list_bars:
#     print("--------------")
#     bars.print_properties()

utils.matrixG(dict_bars,len(di.data_parse(data)[0]["COORDINATES"]))