import unittest
import pandas as pd
import pytest
import numpy as np

# undefined, null, not null, 0, max, float
# array to series conversion
# series to array conversion


#Index.argmin(axis=None, skipna=True, *args, **kwargs)
# empty array, empty string
class test_argmin(unittest.TestCase):

    def setUp(self):
        self.seriesTest = [1, 2, 3, 4, 5]
        self.emptyArray = []
        self.emptyString = ""
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"

    def test_argmin_blackbox(self):
        self.assertEqual(True, False)  # add assertion here




if __name__ == '__main__':
    unittest.main()
