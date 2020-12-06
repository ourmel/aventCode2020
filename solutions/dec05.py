from common.helpers import read_text
import math
import numpy as np


def get_seatid_from_row_column(row, column):
    return row * 8 + column




def get_pos_max_with_next_char(current_min_pos, current_max_pos, letter):
    if letter in ['B','R'] :
        return (current_max_pos - math.ceil((current_max_pos-current_min_pos)/2) + 1), current_max_pos
    if letter in ['F','L'] :
        return current_min_pos , (current_min_pos + math.floor((current_max_pos - current_min_pos)/2))

def get_row(seat) :
    min = 0
    max = 127
    for letter in seat[:7] :
        min,max = get_pos_max_with_next_char(min,max, letter)

    return min


def get_col(seat):
    min = 0
    max = 7
    for letter in seat[7::]:
        min, max = get_pos_max_with_next_char(min, max, letter)

    return min

def get_my_seat(seat_id) :
    sorted_seat_id = seat_id.sort()
    for i in range(1,len(seat_id)) :
        if seat_id[i] - seat_id[i-1] == 2 :
            # print(seat_id[i-1])
            return seat_id[i]-1




if __name__ == '__main__':
    day = 5
    input_file = str('input' + str(day))
    seats_list = read_text(input_file)

    seat = 'FBFBBFFRLR'

    seat_id = [get_seatid_from_row_column(get_row(x), get_col(x)) for x in seats_list]
    print("max is : ", max(seat_id))

    print("my seat is : ", get_my_seat(seat_id))




