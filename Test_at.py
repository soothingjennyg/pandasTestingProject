import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    This function search in a dataframe and returns the value which is present there
    '''
    def setUp(self):
        self.df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])

        self.df.at[4, 'B']=12
    def test_at(self):
       self.assertEqual(self.df.at[4, 'B'],2)
       self.assertEqual(self.df.at[4, 'B'], 12)

if __name__ == '__main__':
    unittest.main()