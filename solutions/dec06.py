import numpy as np
import string

def get_count(group):
    flatten_group = [idx for tup in group for idx in tup]
    return len(np.unique(flatten_group))

def get_count_everybody(group):
    letter_list = []
    for letter in string.ascii_lowercase[::]:
        if all([letter in x for x in group]):
            letter_list.append(letter)

    return len(letter_list)


if __name__ == '__main__':
    day = 6
    filename = str('input' + str(day))

    file1 = open(str('../input/' + filename + '.txt'), 'r')
    raw_groups = file1.read().split('\n\n')

    clean_groups = [x.split() for x in raw_groups]

    counts_list = [get_count(x) for x in clean_groups]

    counts_everybody_list = [get_count_everybody(x) for x in clean_groups]


    print("sum of counts is : " ,sum(counts_list))

    print("sum of counts with eveyrybody is : " ,sum(counts_everybody_list))



