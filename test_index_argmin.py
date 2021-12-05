import sys
import unittest
import pandas as pd
import sys
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
        #self.seriesSequenceTest = pd.Series(1, 2, 3, 4, 5)
        #self.emptySeriesTest = pd.Series()
        self.emptyStringSeries = pd.Series({'A':'','B':'','C':''})
        #print("hello")
        #print(self.emptyStringSeries.argmin())
        self.testNoneInSeriesRepeatedMinMax = pd.Series({'A':None, 'B': 1, 'C': 5, 'D': 1, 'E': 5})
        self.testMinMax = pd.Series({'A': sys.maxsize, 'B': -sys.maxsize, 'C': 5, 'D': 1, 'E': 5})

        self.testNAN = pd.Series({'A':"NaN"})
        self.testNull = pd.Series({'A': None})
        self.testNullOnly = pd.Series(None)
        #print(self.testMinMax.argmin())
        self.cerealSeriesData = pd.Series({'Corn Flakes': 100.0, 'Almond Delight': 110.0,
                                           'Cinnamon Toast Crunch': 120.0, 'Cocoa Puff': 110.0})
        #print(self.cerealSeriesData.argmin())

    def test_argmin_blackbox(self):
        #test to see expected result from online example
        self.assertEqual(self.cerealSeriesData.argmin(), 0)
        #testwith repeated min and max values
        self.assertEqual(self.testNoneInSeriesRepeatedMinMax.argmin(), 1)
        #test with largest integers
        self.assertEqual(self.testMinMax.argmin(), 1)


        with self.assertRaises(TypeError):
            self.testNAN.argmin()
        with self.assertRaises(TypeError):
            self.emptyStringSeries.argmin()
        with self.assertRaises(TypeError):
            self.testNull.argmin()
        with self.assertRaises(ValueError):
            self.testNullOnly.argmin()

if __name__ == '__main__':
    unittest.main()
