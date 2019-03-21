import utils
import bar
import dataIngest as di


data = di.get_data()
list_bars, dict_bars = di.join_bars(*di.data_parse(data))

# print(dict_bars)
# for bars in list_bars:
#     bars.print_properties()