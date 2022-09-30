import unittest
from game import mytictactoe


class PrimeNumbersTestCase(unittest.TestCase):

    def test_mytictactoe(self):
        result = mytictactoe([1, 2, 3, 4, 5, 6, 7, 8, 9])
        str1 = "\n\t     |     |\n\t  1  |  2  |  3\n\t_____|_____|_____\n\t     |     |\n\t  4  |  5  |  6\n" \
               "\t_____|_____|_____\n\t     |     |\n\t  7  |  8  |  9\n\t     |     |\n"
        self.assertEqual(result, str1)
