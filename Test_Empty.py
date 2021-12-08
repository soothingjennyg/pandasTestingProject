import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    If a dataframe is empty ,it checks and returns empty
    note: Nan is not considered as empty
    '''
    def setUp(self):
        self.df_empty = pd.DataFrame({'A': []})
        self.df=pd.DataFrame({'H' : [np.nan]})

    def test_Empty(self):
        self.assertEqual((self.df_empty).empty,(True))
        self.assertEqual((self.df).empty, (False))
        self.assertEqual(pd.Series([]).empty,(True))

if __name__  == '__main__':
    unittest.main()