import numpy as np


def get_loto(num):
    arr = np.random.randint(101, size=(num, 5, 5))
    return arr

print(get_loto(3))