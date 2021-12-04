import unittest
import pandas as pd


# possible tests: undefined, null, not null, 0, max, float
"""
Test the pandas.isnull function.

isnull reads a given object and returns a bool or
array of bools that identify if the object is missing values.  This includes None, NaN in object arrays and NaT in datetimelike.
If the object is null, it will return true, or true for 
the items in the array that are null, false for non-null items.

The object can be an array or scalar. 

The only parameter for this function is the object being tested.  
"""


#Index.argmin(axis=None, skipna=True, *args, **kwargs)
# empty array, empty string
class test_isnull(unittest.TestCase):
    def setUp(self):
        self.seriesTest = [1, 2, 3, 4, 5]
        self.emptyArray = []
        self.emptyString = ""
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"

    def test_isnull_blackbox(self):

        self.assertEqual(pd.isnull(self.testNone), True)
        self.assertEqual(pd.isnull(self.testString), False)
        self.assertEqual(pd.isnull(self.testNAN), False)
        self.assertEqual(pd.isnull(self.emptyString), False)



if __name__ == '__main__':
    unittest.main()
