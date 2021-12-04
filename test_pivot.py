import unittest
import pandas as pd
#Return reshaped DataFrame organized by given index / column values.

#Reshape data (produce a “pivot” table) based on column values. Uses unique values from specified index / columns
# to form axes of the resulting DataFrame. This function does not support data aggregation, multiple values will
# result in a MultiIndex in the columns. See the User Guide for more on reshaping.

#To test: empty frame

class test_pivot(unittest.TestCase):
    def setUp(self):
        self.seriesArray = [1, 2, 3, 4, 5]
        self.nameArray = ["Alex", "Bob", "Henry", "Charles", "David"]
        self.emptyArray = []
        self.emptyString = ""
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"
        self.emptyDataFrame = pd.DataFrame(self.emptyArray)


    def test_pivot_blackbox(self):
        self.assertEqual(True, True)  # add assertion here

        #self.assertEqual(self.emptyDataFrame, pd.pivot(self.emptyDataFrame))  # add assertion here


if __name__ == '__main__':
    unittest.main()
