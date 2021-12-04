import unittest
import pandas as pd
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
#Return reshaped DataFrame organized by given index / column values.

#Reshape data (produce a “pivot” table) based on column values. Uses unique values from specified index / columns
# to form axes of the resulting DataFrame. This function does not support data aggregation, multiple values will
# result in a MultiIndex in the columns. See the User Guide for more on reshaping.
"""
Test the pandas.pivot(data, index=None, columns=None, values=None) 
function (https://pandas.pydata.org/docs/reference/api/pandas.pivot.html).

The pivot function createes a pivot table based on values given. The function will use
unique values from specified columns to form axes of the DataFram. 

Multiple values will result in a 'MultiIndex' which will not be tested.  
This function does not support data aggregation.

The parameters are the following:
Data (required) which is a DataFrame.
Index (optional)which can be a string or object or a list of strings.  This will be used to make the index of the new frame.
When not used, it will be the index of the current DataFrame.
Columns can be a string, object or a list of stirngs.  This is uesd to make the new frame's columns  
Values is an optional parameter. This will only be used as the default for these tests 

The return will be a pivoted DataFrame.
"""
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

        self.df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                                'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                                'baz': [1, 2, 3, 4, 5, 6],
                                'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

        self.pivotData = pd.DataFrame({
            'A': [1,4],
            'B': [2,5],
            'C': [3,6]
        },index=['one', 'two'], columns=['A', 'B', 'C'])

    def test_pivot_blackbox(self):
        self.assertEqual(True, True)  # add assertion here
        self.df
        self.pivotData

        p = self.df.pivot(index='foo', columns='bar', values='baz')
        """
        print()
        print(p.to_string())
        print()

        print(p.index)
        print()

        print(p.columns)
        print()
        print(p.values)
        print()
        """
        self.pivotData.index.name = 'foo'
        self.pivotData.columns.name = 'bar'
        """
        print(self.pivotData.to_string())
        print()

        print(self.pivotData.index)
        print()
        print(self.pivotData.columns)
        print()
        print(self.pivotData.values)
        print()
"""
        #self.assertTrue(self.t2.to_string(index=False) == p.to_string())
        self.assertTrue(p.equals(self.pivotData))



if __name__ == '__main__':
    unittest.main()
