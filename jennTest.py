import unittest
import pandas as pd
import pytest
import numpy as np

# undefined, null, not null, 0, max, float
# array to series conversion
# series to array conversion



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.seriesTest = [1, 2, 3, 4, 5]
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"

    def test_isnull(self):
        #test simple int array
        testSeries = pd.isnull(self.testNone)
       # print(testSeries.array)
        self.assertEqual(testSeries, True)  # add assertion here
        self.assertEqual(pd.isnull(self.testString), False)
        self.assertEqual(pd.isnull(self.testNAN), False)


if __name__ == '__main__':
    unittest.main()
