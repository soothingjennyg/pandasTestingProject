#THIS TEST NEEDS TO BE DELETED FROM GIT

import unittest
import pandas as pd
#To test: empty, 
"""
Test the DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False, sort=True) 
function (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table).

The pivot function creates a spreadsheet type pivot table based on values given. 



The parameters are the following:
Values (otional) which is a column to aggregate.
Index can be an array or list. 
Columns can be an array or list.
Aggfunc defaults to numpy.mean.
Fill_value defaults to none. It is a scalar.
Margins defaults to false.  It is a boolean.
Dropna defaults to true.  It is a boolean.
Margins)name defaults to 'All.'.  It is a string.
Observed defaults to false.  It is a boolean. 
Sort defaults to true. It is a boolean.  

The return will be an Excel style DataFrame.
"""

class test_pivot_table(unittest.TestCase):
    def setUp(self):
        self.seriesTest = [1, 2, 3, 4, 5]
        self.emptyArray = []
        self.emptyString = ""
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"

       # df = pd.read_excel('https://github.com/datagy/pivot_table_pandas/raw/master/sample_pivot.xlsx',
       #                parse_dates=['Date'])
      #  print(df.head())

    def test_pivot_table_blackbox(self):

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
