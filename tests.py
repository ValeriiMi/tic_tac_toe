import unittest
from game import mytictactoe, check_Tie, check_Victory, singlegame


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

    def test_check_Victory1(self):
        result = check_Victory({'X': [1, 2, 3], 'O': [4, 7, 9]}, 'X')
        self.assertEqual(result, True)

    def test_check_Victory2(self):
        result = check_Victory({'X': [1, 3, 5, 8], 'O': [2, 4, 6, 7, 9]}, 'O')
        self.assertEqual(result, False)

    def test_singlegame1(self):
        result = singlegame('X', [10])
        self.assertEqual(result, "Invalid Input!!! Try Again")

    def test_singlegame2(self):
        result = singlegame('X', [2, 2])
        self.assertEqual(result, "Oops! The Place is already occupied. Try again!!")

    def test_singlegame3(self):
        result = singlegame('X', [1, 4, 2, 5, 3, 9])
        self.assertEqual(result, 'X')

    def test_singlegame4(self):
        result = singlegame('O', [2, 1, 4, 3, 6, 5, 7, 8, 9])
        self.assertEqual(result, "D")