import unittest
from solutions.dec05 import get_pos_max_with_next_char, get_row, get_col,get_seatid_from_row_column


class TestsFrom5Dec(unittest.TestCase):

    def test_if_first_move_is_ok_if_B(self):
        current_max_pos = 127
        current_min_pos = 0
        letter = 'B'
        self.assertEqual(get_pos_max_with_next_char(current_min_pos, current_max_pos, letter), (64,127))

    def test_if_first_move_is_ok_if_F(self):
        current_max_pos = 127
        current_min_pos = 0
        letter = 'F'
        self.assertEqual(get_pos_max_with_next_char(current_min_pos, current_max_pos, letter), (0,63))

    def test_if_BFFFBBFRRR_567(self):
        seat_code = 'BFFFBBFRRR'
        get_seatid_from_row_column(get_row(seat_code), get_col(seat_code))

        self.assertEqual(get_seatid_from_row_column(get_row(seat_code), get_col(seat_code)) , 567)
