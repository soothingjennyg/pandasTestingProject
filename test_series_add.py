import pandas as pd
import numpy as np
import unittest


class TestSeriesAdd(unittest.TestCase):
    def setUp(self):
        # regular addition
        self.series1a = pd.Series([0, 1, 2, 3])
        self.series1b = pd.Series([4, 5, 6, 7])
        self.series1c = pd.Series([4, 6, 8, 10])
        # addition with NaN
        self.series2a = pd.Series([1, 2, np.nan, np.nan])
        self.series2b = pd.Series([3, np.nan, 4, np.nan])
        self.series2c = pd.Series([4, np.nan, np.nan, np.nan])
        # addition with empty series
        self.series3 = pd.Series([], dtype='int')
        # addition with large series
        self.series4a = pd.Series(range(0, 10000000))
        self.series4b = self.series4a
        self.series4c = pd.Series(range(0, 20000000, 2))
        # addition with indices
        self.series5a = pd.Series([0, 1, 2, 3, 4], ["a", "b", "c", "d", "e"])
        self.series5b = pd.Series([5, 6, 7, np.nan, 9], ["e", "d", "c", "b", "a"])
        self.series5c = pd.Series([9, np.nan, 9, 9, 9], ["a", "b", "c", "d", "e"])
        # addition with different lengths
        self.series6a = pd.Series([4, 5, 6, 7, 8, 9, 10])
        self.series6b = self.series1a
        self.series6c = pd.Series([4, 6, 8, 10, np.nan, np.nan, np.nan])
        # addition with indices and different lengths
        self.series7a = pd.Series([0, 1, 2, 3, 4], ["b", "c", "d", "e", "f"])
        self.series7b = pd.Series([5, 6, 7, 8, 9, 10], ["a", "b", "c", "f", "g", "h"])
        self.series7c = pd.Series([np.nan, 6, 8, np.nan, np.nan, 12, np.nan, np.nan],
                                  ["a", "b", "c", "d", "e", "f", "g", "h"])

    def test_series_add_same_length(self):
        self.assertTrue(self.series1a.add(self.series1b).equals(self.series1c))
        self.assertTrue(self.series2a.add(self.series2b).equals(self.series2c))
        self.assertTrue(self.series3.add(self.series3).equals(self.series3))
        self.assertTrue(self.series4a.add(self.series4b).equals(self.series4c))
        self.assertTrue(self.series5a.add(self.series5b).equals(self.series5c))

    def test_series_add_different_lengths(self):
        self.assertTrue(self.series6a.add(self.series6b).equals(self.series6c))
        self.assertTrue(self.series7a.add(self.series7b).equals(self.series7c))


if __name__ == '__main__':
    unittest.main()
