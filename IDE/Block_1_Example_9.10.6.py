import numpy as np


def make_sp_arr(a):
    arr = np.arange(0, a**2, 1)
    arr.shape=(a, a)
    
    # return arr
    # return arr[1::2, ::2]
    return arr[1::2][::2]

def get_chess(a):
    arr = np.zeros((a, a))
    arr[1::2, ::2] = 1
    arr[::2, 1::2] = 1
    return arr
    

print(make_sp_arr(4))

# print(get_chess(4))