import pandas as pd
import unittest

class TestIsLeapYear(unittest.TestCase):
    """
    Check if the given timestamp is a leap year.
    Leap years are divisible by 4. If the date is in addition divisible by 100,
    then it is no leap year. Exception: If it is also divisible by 400.
    """
    def setUp(self):
        #no leap years (not divisible by 4)
        self.d1 = pd.Timestamp(2017, 3, 2)
        self.d2 = pd.Timestamp(2002, 11, 9, 17)

        #leap years (divisible by 4)
        self.d3 = pd.Timestamp(1992, 5, 5)
        self.d4 = pd.Timestamp(2024, 7, 18, 3)

        #no leap year (divisible by 100)
        self.d5 = pd.Timestamp(1900, 12, 1)

        #leap year (divisible by 400)
        self.d6 = pd.Timestamp(2000, 9, 28, 7)

    def test_isLeapYear(self):
        self.assertFalse(self.d1.is_leap_year)
        self.assertFalse(self.d2.is_leap_year)

        self.assertTrue(self.d3.is_leap_year)
        self.assertTrue(self.d4.is_leap_year)

        self.assertFalse(self.d5.is_leap_year)

        self.assertTrue(self.d6.is_leap_year)


if __name__ == '__main__':
    unittest.main()
