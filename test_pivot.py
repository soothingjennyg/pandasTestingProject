import unittest
import pandas as pd

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
        self.nameArray = ["Alex", "Bob", "Henry", "Charles", "David"]
        self.emptyArray = []
        self.emptyDataFrame = pd.DataFrame(self.emptyArray)
        self.nameArrayDataFrame = pd.DataFrame({'Name': self.nameArray})
        self.df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                                'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                                'baz': [1, 2, 3, 4, 5, 6],
                                'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

        self.pivotDataTestOne = pd.DataFrame({
            'A': [1,4],
            'B': [2,5],
            'C': [3,6]
        },index=['one', 'two'], columns=['A', 'B', 'C'])
        self.pivotDataTestTwo = pd.DataFrame({
            'A': ['x', 'q'],
            'B': ['y','w'],
            'C': ['z', 't']
        }, index=['one', 'two'], columns=['A', 'B', 'C'])


    def test_pivot_blackbox(self):

        #Test for correct data on two data columns
        testOne = self.df.pivot(index='foo', columns='bar', values='baz')
        testTwo = self.df.pivot(index='foo', columns='bar', values='zoo')

        self.assertTrue(testOne.equals(self.pivotDataTestOne))
        self.assertTrue(testTwo.equals(self.pivotDataTestTwo))

#empty DataFrame
        with self.assertRaises(TypeError):
            self.emptyDataFrame.pivot()
        with self.assertRaises(KeyError):
            self.nameArrayDataFrame.pivot(columns='names')





if __name__ == '__main__':
    unittest.main()
