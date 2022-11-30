import numpy as np


mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)


elem_5_3 = mystery[4, 2]
# print(elem_5_3)
last = mystery[-1, -1]
# print(last)
line_4 = mystery[3]
# print(line_4)
col_2 = mystery[:, -2]
# print(col_2)
part = mystery[1:4, 2:5]
# print(part)
rev = mystery[::-1,-1]
# print(rev)
trans = mystery.transpose()
# print(trans)