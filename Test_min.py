import pandas as pd
import numpy as np
import unittest
class Mytest(unittest.TestCase):
    '''
    A simple function which goes through the set of data and shows the minimum value in it
    '''
    def setUp(self):
        self.a=[4, 2, 0, 8]
    def test_min(self):
        self.assertEqual(pd.Series(self.a).min(),(0))
        self.assertEqual(pd.Series([6,8,3]).min(),(3))

if __name__  == '__main__':
    unittest.main()