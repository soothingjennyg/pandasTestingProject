import pandas as pd
import numpy as np
import unittest

class TestSeriesSum(unittest.TestCase):
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
        
        
        
