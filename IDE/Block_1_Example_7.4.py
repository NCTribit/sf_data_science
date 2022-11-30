import numpy as np


mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)


nans_index = np.isnan(mystery)
# print(nans_index)

n_nan = len(mystery[nans_index])
# print(n_nan)

mystery_new = mystery.copy()
mystery_new[nans_index] = 0
# print(mystery_new)

# mystery.dtype=np.int32
mystery_int = mystery.copy()
mystery_int.dtype=np.int32
# print(type(mystery_int))

array = np.sort(mystery_new)
# print(array)

table = array.reshape((5, 3), order='F')
# print(table)

col = table[:, 1]
# print(col)
