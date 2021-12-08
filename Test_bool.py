import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    This method reads boolean
    returns false if reads false
    true if reads true
    '''
    def test_bool(self):
        self.assertEqual(pd.Series(True).bool(),(True))
        self.assertEqual(pd.Series(False).bool(), (False))
        self.assertTrue(pd.Series([bool(True),bool(False)]).equals(pd.Series([True,False])))

if __name__  == '__main__':
    unittest.main()