
def read_integers(filename) :
    file1 = open(str('../input/' + filename +'.txt'), 'r')
    l = file1.read().splitlines()
    l_int = [int(x) for x in l]

    return l_int

def read_text(filename) :
    file1 = open(str('/input/' + filename +'.txt'), 'r')
    l_str = file1.read().splitlines()

    return l_str

