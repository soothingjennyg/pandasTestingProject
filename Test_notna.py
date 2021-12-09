import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    Checks scalar or array if there is anything missing in it
    '''
    def setUp(self):
        self.str='Hira'
        self.testNone=None
        self.testNan=' '
        self.testarray=[1,2,3]
        self.test1=[6,'h',None]

    def test_notnull(self):
        self.assertEqual(pd.notna(self.str),True)
        self.assertEqual(pd.notna(self.testNone),False)
        self.assertEqual(pd.notna(self.testNan),True)
        self.assertEqual(pd.notna(self.testarray[2]), True)
        self.assertEqual(pd.notna(self.testarray).all(),(True))
        self.assertEqual(pd.notna(self.test1).all(), (False))

if __name__  == '__main__':
    unittest.main()
