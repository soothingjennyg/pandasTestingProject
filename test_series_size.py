import pandas as pd
import unittest


class TestSeriesSize(unittest.TestCase):
    def setUp(self):
        self.series1 = pd.Series(1)
        self.series2 = pd.Series([1, 2, 3])
        self.series3 = pd.Series([], dtype='int')
        self.series4 = pd.Series(range(0, 100))
        self.series5 = pd.Series(range(0, 10000000))
        # higher values fails in the creation of the series, doing that would test Series() instead of series.size

    def test_series_size(self):
        self.assertEqual(self.series1.size, 1)
        self.assertEqual(self.series2.size, 3)
        self.assertEqual(self.series3.size, 0)
        self.assertEqual(self.series4.size, 100)
        self.assertEqual(self.series5.size, 10000000)


if __name__ == '__main__':
    unittest.main()
