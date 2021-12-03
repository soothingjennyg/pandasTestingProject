import pandas as pd
import numpy as np
import unittest

class TestSeriesSub(unittest.TestCase):
    def setUp(self):
        # regular subtraction
        self.series1a = pd.Series([4,1,2,3])
        self.series1b = pd.Series([6,9,4,8])
        self.series1c = pd.Series([-2,-8,-2,-5])
        # subtraction with NaN
        self.series2a = pd.Series([1,np.nan,2,3])
        self.series2b = pd.Series([4,np.nan,np.nan,6])
        self.series2c = pd.Series([-3,np.nan,np.nan,-3])
        # subtraction with large series
        self.series3b = pd.Series(range(0,300000))
        self.series3a = pd.Series(range(0,600000,2))
        self.series3c = self.series3b
        # subtraction with empty series
        self.series4 = pd.Series([],dtype='int')
        # subtraction with different lengths
        self.series5a = pd.Series([2,4,5,6,8,9,10])
        self.series5b = self.series1b
        self.series5c = pd.Series([-4,-5,1,-2,np.nan,np.nan,np.nan])
        # Subtraction with indices
        self.series6a = pd.Series([6,1,2,3,4],["a","b","c","d","e"])
        self.series6b = pd.Series([5,6,7,1,8],["c","e","d","a","b"])
        self.series6c = pd.Series([5,-7,-3,-4,-2],["a","b","c","d","e"])
        # subtraction with indices and different lengths
        self.series7a = pd.Series([1,2,3,5],["f","g","a","b"])
        self.series7b = pd.Series([6,7,8,4,9,10],["c","d","e","f","g","h"])
        self.series7c = pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,-3,-7,np.nan],["a","b","c","d","e","f","g","h"])
    def test_series_sub_same_length(self):
        self.assertTrue(self.series1a.sub(self.series1b).equals(self.series1c))
        self.assertTrue(self.series2a.sub(self.series2b).equals(self.series2c))
        self.assertTrue(self.series3a.sub(self.series3b).equals(self.series3c))
        self.assertTrue(self.series4.sub(self.series4).equals(self.series4))
        self.assertTrue(self.series6a.sub(self.series6b).equals(self.series6c))
    def test_series_sub_different_length(self):
        self.assertTrue(self.series5a.sub(self.series5b).equals(self.series5c))
        self.assertTrue(self.series7a.sub(self.series7b).equals(self.series7c)





