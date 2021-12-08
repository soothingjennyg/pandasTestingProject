import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''this method returns boolean
    if one value is true in a series
    it returns true regardless if rest of values are false
    '''
    def setUp(self):
        self.b=[True,False,True]

    def test_any(self):
        self.assertEqual(pd.Series([True,True]).any(),(True))
        self.assertEqual(pd.Series(self.b).any(),True)
        self.assertEqual(pd.Series([False,False]).any(),(False))

if __name__  == '__main__':
    unittest.main()