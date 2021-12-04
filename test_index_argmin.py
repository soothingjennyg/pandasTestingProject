import unittest
import pandas as pd
import pytest
import numpy as np

# undefined, null, not null, 0, max, float
# array to series conversion
# series to array conversion
"""
Test the pandas.Index.argmin(axis=None, skipna=True, *args, **kwargs) function.

isnull returns the integer position of the smallest value in a series.  If there are more than one 
with a minimum, the first position is returned (https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html#pandas.Index.argmin)

Their are four parameters for this function.
Axis is a dummy argument to match Series.  Skipna is a boolean value that defaults to true.  When it is true, null values
are excluded.  *args and **kwargs are arguments and keywords for use with NumPy.   


"""


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
        self.assertEqual(True, True)  # add assertion here




if __name__ == '__main__':
    unittest.main()
