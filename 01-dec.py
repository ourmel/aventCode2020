import numpy as np
import itertools
from helpers import read_integers

input_file = "input1"

list_int = read_integers(input_file)

sum_list = list(itertools.combinations(list_int, 2))
for x in sum_list:
    if (x[0] + x[1]) == 2020:
        print(x[0] * x[1])


trio_list = list(itertools.combinations(list_int, 3))
for x in trio_list:
    if sum(x) == 2020:
        print(x[0]*x[1]*x[2])

