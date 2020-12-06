from solutions.dec06 import *
import unittest


class TestsFrom6Dec(unittest.TestCase):

    def test_if_abc_returns_3(self):
        input = ['abc']
        self.assertEqual(get_count(input), 3)

    def test_if_cccbb_returns_2(self):
        input = ['cccbb']
        self.assertEqual(get_count(input), 2)

    def test_if_cccbb_returns_2_part2(self):
        input = ['cccbb']
        self.assertEqual(get_count_everybody(input), 2)

    def test_if_abc_returns_3_part2(self):
        input = ['abc']
        self.assertEqual(get_count_everybody(input), 3)