import pandas as pd
import numpy as np
import unittest

class TestIsna(unittest.TestCase):
    """
    Implemented tests for the isna() function. It returns True for (NaN / None / NaT) values and
    else false. For lists or data frames as input, it returns the same
    structure containing boolean values (indicating for every value whether it is NaN/None/NaT)
    """
    def setUp(self):
        self.v1 = 'uppsala'
        self.v2 = 'NaN'
        self.v3 = ''
        self.v4 = None
        self.v5 = np.NaN
        self.v6 = np.datetime64('nat')

        self.arr1 = []
        self.arr2 = [self.v6, self.v1]
        self.arr3 = [self.v2, self.v3, self.v4, self.v5]

        self.df = pd.DataFrame({'col1': [self.v1, self.v6], 'col2': [self.v4, self.v2]})


    def test_isna(self):

        #check scalars (expect false)
        for vi in [self.v1, self.v2, self.v3]:
            self.assertFalse(pd.isna(vi))

        #check scalars (expect true)
        for vi in [self.v4, self.v5, self.v6]:
            self.assertTrue(pd.isna(vi))

        #check arrays
        self.assertEqual(len(pd.isna(self.arr1)), 0)

        arr2 = pd.isna(self.arr2)
        self.assertTrue(arr2[0])
        self.assertFalse(arr2[1])

        arr3 = pd.isna(self.arr3)
        self.assertFalse(arr3[0])
        self.assertFalse(arr3[1])
        self.assertTrue(arr3[2])
        self.assertTrue(arr3[3])

        #check data frame
        df = pd.isna(self.df)
        self.assertFalse(df['col1'][0])
        self.assertTrue(df['col1'][1])
        self.assertTrue(df['col2'][0])
        self.assertFalse(df['col2'][1])



if __name__ == '__main__':
    unittest.main()
