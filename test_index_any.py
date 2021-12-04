import pandas as pd
import unittest

class TestIndexAny(unittest.TestCase):
    def setUp(self):
        self.series1 = pd.Index([3, 4, 6])
        self.series2 = pd.Index([1, 1, 2, 0])
        self.series3 = pd.Index([0, 0, 0])
        self.series4 = pd.Index([])
        self.series5 = pd.Index([6,0,0,0])
        self.series6 = pd.Index([9,8,6,0,1,0])


    def test_Index_Any(self):
        self.assertTrue(self.series1.any() == True)
        self.assertTrue(self.series2.any() == True)
        self.assertTrue(self.series3.any() == False)
        self.assertTrue(self.series4.any() == False)
        self.assertTrue(self.series5.any() == True)
        self.assertTrue(self.series6.any() == True)


if __name__ == '__main__':
    unittest.main()









