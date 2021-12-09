import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    checks array o scalar values for not missing values and returns boolean
    '''
    def setUp(self):
        self.str='Hira'
        self.testNone=None
        self.testNan=' '
        self.testarray=[1,2,3]
        self.test1=[None,6,'h']

    def test_notnull(self):
        self.assertEqual(pd.notnull(self.str),True)
        self.assertEqual(pd.notnull(self.testNone),False)
        self.assertEqual(pd.notnull(self.testNan),True)
        self.assertEqual(pd.notnull(self.testarray[2]),True)
        self.assertEqual(pd.notnull(self.testarray).all(), (True))
        self.assertEqual(pd.notnull(self.test1).all(), (False))

if __name__  == '__main__':
    unittest.main()
