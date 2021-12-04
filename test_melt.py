import unittest
import pandas as pd

class test_melt(unittest.TestCase):
    def setUp(self):
        self.seriesTest = [1, 2, 3, 4, 5]
        self.emptyArray = []
        self.emptyString = ""
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"


    def test_test_melt_blackbox(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
