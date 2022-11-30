import numpy as np


np.random.seed(2021)


simple = np.random.rand()
# print(simple)

randoms = np.random.uniform(-150, 2021, size=120)
# print(randoms)

table = np.random.randint(1, 101, size=(3, 2))
# print(table)

even = np.arange(2, 17, 2)
# print(even)

# mix = even.copy()
mix = even
np.random.shuffle(mix)
# print(mix)

select = np.random.choice(even, size=3, replace=False)
# print(select)

triplet = np.random.permutation(select)
# print(triplet)
