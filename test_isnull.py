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
        self.indexDateTime = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,
                                  "2017-07-08"])
    def test_isnull_blackbox(self):
        # Test for None to be true
        self.assertEqual(pd.isnull(self.testNone), True)
        # Test for a string to be false
        self.assertEqual(pd.isnull(self.testString), False)
        # Test for NAN to be false
        self.assertEqual(pd.isnull(self.testNAN), False)
        #Test for an empty string to be false
        self.assertEqual(pd.isnull(self.emptyString), False)
        #Test for an array of dates with a None value to be [F,F,T,F]
        self.assertEqual(pd.isnull(self.indexDateTime[0]), False)
        self.assertEqual(pd.isnull(self.indexDateTime[1]), False)
        self.assertEqual(pd.isnull(self.indexDateTime[2]), True)
        self.assertEqual(pd.isnull(self.indexDateTime[3]), False)


if __name__ == '__main__':
    unittest.main()
