import unittest
from game import mytictactoe, check_Tie


class PrimeNumbersTestCase(unittest.TestCase):

    def test_mytictactoe(self):
        result = mytictactoe([1, 2, 3, 4, 5, 6, 7, 8, 9])
        str1 = "\n\t     |     |\n\t  1  |  2  |  3\n\t_____|_____|_____\n\t     |     |\n\t  4  |  5  |  6\n" \
               "\t_____|_____|_____\n\t     |     |\n\t  7  |  8  |  9\n\t     |     |\n"
        self.assertEqual(result, str1)

    def test_check_Tie1(self):
        result = check_Tie({'X': [1, 3, 5, 8], 'O': [2, 4, 6, 7, 9]})
        self.assertEqual(result, True)

    def test_check_Tie2(self):
        result = check_Tie({'X': [1, 3, 5, 8], 'O': [2, 4, 6, 7]})
        self.assertEqual(result, False)
