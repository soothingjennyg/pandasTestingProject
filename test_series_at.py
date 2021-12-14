import pandas as pd
import numpy as np
import unittest
class TestSeriesAt(unittest.TestCase):
    def setUp(self):
        self.series1 = pd.Series([1, 2, 3, 4])
        self.series2 = pd.Series([2, 4, 6, 8], ["dog", "cat", "pig", "cow"])
        self.series3 = pd.Series([6,8,9,10,5])
    def test_series_at(self):
        self.assertEqual(self.series1.at[1], 2)
        self.assertEqual(self.series2.at["cat"], 4)
        self.assertEqual(self.series2.at["cow"], 8)
        self.assertEqual(self.series3.at[3], 10)
        self.assertEqual(self.series3.at[4], 5)


if __name__ == '__main__':
    unittest.main()
