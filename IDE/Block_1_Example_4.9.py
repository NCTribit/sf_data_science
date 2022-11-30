from collections import defaultdict
from collections import OrderedDict

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]


sp_dict = defaultdict(list)
for name, rate in ratings:
    sp_dict[rate].append(name)
    sp_dict[rate].sort()
    
rates_list = list(sp_dict.keys())
rates_list.sort(reverse=True)
# print(rates_list)

od = OrderedDict()
for el in rates_list:
    od[el] = sp_dict[el]

cafes = OrderedDict([(name, key) for key, value in od.items() for name in value])
   
# print(sp_dict)
# print(cafes)
