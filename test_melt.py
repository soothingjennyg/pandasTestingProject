import unittest
import pandas as pd

"""
Test the pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True) 
(https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt) function.

Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

This function is used to change a format where one or more columns are identifier variables (id_vars), 
while all other columns, considered measured variables (value_vars), are “unpivoted” to the row axis, leaving just two non-identifier columns, ‘variable’ and ‘value’.

Parameters
id_varstuple, list, or ndarray, optional
Column(s) to use as identifier variables.

value_varstuple, list, or ndarray, optional
Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.

var_namescalar
Name to use for the ‘variable’ column. If None it uses frame.columns.name or ‘variable’.

value_namescalar, default ‘value’
Name to use for the ‘value’ column.

col_levelint or str, optional
If columns are a MultiIndex then use this level to melt.

ignore_indexbool, default True
If True, original index is ignored. If False, the original index is retained. Index labels will be repeated as necessary.

This function returns an unpivoted DataFrame.
"""

class test_melt(unittest.TestCase):
    def setUp(self):
        self.seriesTest = [1, 2, 3, 4, 5]
        self.emptyArray = []
        self.emptyString = ""
        self.testNone = None
        self.testString = 'aword is a word'
        self.testNAN = "NaN"


    def test_test_melt_blackbox(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
