import pandas as pd
import numpy as np
import unittest

class TestSeriesSum(unittest.TestCase):
    """
    Test the pandas.series.sum function
    sum() will be used to get the sym of the values for the requested axis
    it will return the sum of the requested series.
    parameters:
    level:int or level name or default none
    if the axis is a multiindex(hierarchical),count along a particular level collapsing into a smaller series
    returns sum of the of the values of requested axis.
    if you have an series[4,2,0,8] for names['dog','fish','cat','mouse'] it wil returns
    dog     4
    fish    2
    cat     0
    mouse   8
    sum()   14
    """
    def setUp(self):
        self.series1 = pd.Series([], dtype='int')
        self.series2 = pd.Series([1,2,3,4])
        self.series3 = pd.Series([2,4,6,8],["dog","cat","pig","cow"])
    def test_series_sum(self):
        self.assertEqual(self.series1.sum(),0)
        self.assertEqual(self.series2.sum(),10)
        self.assertEqual(self.series3.sum(),20)



if __name__ == '__main__':
    unittest.main()
