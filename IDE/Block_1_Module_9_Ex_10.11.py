import numpy as np


def get_unique_loto(num):
    arr = list()
    for i in range(num):
        inner_arr = np.random.choice(np.arange(1, 101), size=(5, 5), replace=False)
        arr.append(inner_arr)
    arr = np.array(arr)
    return arr


# В этой версии числа не повторяются вообще, а не только во внутренних массивах
def get_unique_loto_my_version(num):
    arr = np.random.choice(np.arange(1, 101), size=(num, 5, 5), replace=False)
    return arr


print(get_unique_loto(3))

print(get_unique_loto_my_version(3))