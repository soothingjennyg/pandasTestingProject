
import unittest
import pandas as pd
import sys

"""
Test the pandas.Index.argmax(axis=None, skipna=True, *args, **kwargs) function.

argmax returns the integer position of the largest value in a series.  If there are more than one 
with a minimum, the first position is returned (https://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html#pandas.Index.argmax)

Their are four parameters for this function.
Axis is a dummy argument to match Series.  Skipna is a boolean value that defaults to true.  When it is true, null values
are excluded.  *args and **kwargs are arguments and keywords for use with NumPy.   


"""


class test_argmax(unittest.TestCase):

    def setUp(self):
        self.emptyStringSeries = pd.Series({'A':'','B':'','C':''})
        self.testNoneInSeriesRepeatedMinMax = pd.Series({'A':None, 'B': 1, 'C': 5, 'D': 1, 'E': 5})
        self.testMinMax = pd.Series({'A': sys.maxsize, 'B': -sys.maxsize, 'C': 5, 'D': 1, 'E': 5})
        self.testNAN = pd.Series({'A':"NaN"})
        self.testNull = pd.Series({'A': None})
        self.testNullOnly = pd.Series(None)
        self.cerealSeriesData = pd.Series({'Corn Flakes': 100.0, 'Almond Delight': 110.0,
                                           'Cinnamon Toast Crunch': 120.0, 'Cocoa Puff': 110.0})


    def test_argmin_blackbox(self):
        #test to see expected result from online example
        self.assertEqual(self.cerealSeriesData.argmax(), 2)
        #testwith repeated min and max values
        self.assertEqual(self.testNoneInSeriesRepeatedMinMax.argmax(), 2)
        #test with largest integers
        self.assertEqual(self.testMinMax.argmax(), 0)


        with self.assertRaises(TypeError):
            self.testNAN.argmax()
        with self.assertRaises(TypeError):
            self.emptyStringSeries.argmax()
        with self.assertRaises(TypeError):
            self.testNull.argmax()
        with self.assertRaises(ValueError):
            self.testNullOnly.argmax()

if __name__ == '__main__':
    unittest.main()
