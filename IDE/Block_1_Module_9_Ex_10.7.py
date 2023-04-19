import numpy as np

# array = np.array([1, 2, 3, 4, 5])
def shuffle_seed(array):
    array_ = np.array(array)
    s = np.random.randint(2**32, dtype=np.int64)
    # s = np.random.randint(2**32)
    np.random.seed(s)
    np.random.shuffle(array_)
    return (array_, s)


print(shuffle_seed([1, 2, 3, 4, 5]))