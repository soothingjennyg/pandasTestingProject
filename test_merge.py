import unittest
import pandas as pd


class TestMerge(unittest.TestCase):
    def setUp(self):
        # one mutual column to merge
        self.df_1a = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        self.df_1b = pd.DataFrame({'a': [1, 2, 3], 'd': [4, 5, 6], 'e': [7, 8, 9]})
        self.df_1c = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [4, 5, 6], 'e': [7, 8, 9]})
        # only mutual columns to merge
        self.df_2a = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        self.df_2b = self.df_2a.copy()
        self.df_2c = self.df_2a.copy()
        # no mutual column to merge, raise error
        self.df_3a = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        self.df_3b = pd.DataFrame({'d': [1, 2, 3], 'e': [4, 5, 6], 'f': [7, 8, 9]})
        # only mutual columns to merge, only one mutual row
        self.df_4a = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        self.df_4b = pd.DataFrame({'a': [1, 2, 3], 'b': [5, 5, 6], 'c': [7, 8, 8]})
        self.df_4c = pd.DataFrame({'a': [2], 'b': [5], 'c': [8]})



    def test_merge(self):
        self.assertTrue(self.df_1a.merge(self.df_1b).equals(self.df_1c))
        self.assertTrue(self.df_2a.merge(self.df_2b).equals(self.df_2c))
        self.assertRaises(ValueError, self.df_3a.merge, self.df_3b)
        self.assertTrue(self.df_4a.merge(self.df_4b).equals(self.df_4c))


if __name__ == '__main__':
    unittest.main()
