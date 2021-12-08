import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    returns same value either with float or int
    '''
    def setUp(self):
        self.num=2

    def test_to_numeric(self):

        self.assertEqual(pd.to_numeric(self.num),(2.0))
        self.assertEqual(pd.to_numeric(-4),-4.0)
        self.assertEqual(pd.to_numeric(9.0), 9.0)

if __name__  == '__main__':
    unittest.main()