import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        self.a=[True,False,True]
        '''
        This method return a boolean.
        return true if all is true
        return false if even one in false in series
        '''

    def test_all(self):
        self.assertEqual(pd.Series([True,True]).all(),(True))
        self.assertEqual(pd.Series(self.a).all(),False)

if __name__  == '__main__':
    unittest.main()