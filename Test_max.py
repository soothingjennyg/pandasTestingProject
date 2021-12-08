import pandas as pd
import numpy as np
import unittest
class Mytest(unittest.TestCase):
    '''
    A simple function which goes through the set of data and shows the maximum value in it
    '''
    def setUp(self):
        self.a=[4, 2, 0, 8]
    def test_max(self):
        self.assertEqual(pd.Series(self.a).max(),(8))
        self.assertEqual(pd.Series([6,10,3]).max(),(10))

if __name__  == '__main__':
    unittest.main()