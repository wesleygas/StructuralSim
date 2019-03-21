import utils
import bar
import dataIngest as di


data = di.get_data("input_file_test.txt")
list_bars, dict_bars = di.join_bars(*di.data_parse(data))

# print(dict_bars)
# for bars in list_bars:
#     print("--------------")
#     bars.print_properties()