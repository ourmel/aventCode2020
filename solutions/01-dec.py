import itertools
import math
from common.helpers import read_integers
import os


def product(iter):
    return(math.prod(iter))

def is_sum_equals_val(list_int, val, size) :
    if size == 2:
        duo_list = list(itertools.combinations(list_int, size))
        for x in duo_list:
            if (x[0] + x[1]) == val:
                return x

    if size == 3 :
        trio_list = list(itertools.combinations(list_int, size))
        for x in trio_list:
            if sum(x) == val:
                return x


if __name__ == '__main__':
    day = 1
    input_file = str('input' + str(day))
    list_integers = read_integers(input_file)

    couple = is_sum_equals_val(list_integers,2020,4)
    prod_couple = product(couple)

    trio = is_sum_equals_val(list_integers,2020,3)
    trio_couple = product(trio)

    print("first part answer is :" + str(prod_couple))
    print("second part answer is :" + str(trio_couple))


