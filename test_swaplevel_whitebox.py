import pandas as pd
import unittest
import numpy as np
import coverage
from pandas.core.indexes.multi import (MultiIndex)
""" Here I am testing whitebox the swaplevel function and the goal is to get 100% statement coverage.
soi looked at the source code and tried to get all lines executed.but here i get 98% statement covered.
the missing line is only one i.e 12
we get
      Name                         Stmts   Miss  Cover   Missing
      ----------------------------------------------------------
      test_swaplevel_whitebox.py      57      1    98%   12
      ----------------------------------------------------------
      TOTAL                           57      1    98%
      """


def all_true(arr):
    '''Returns True if all items in array is True.
        Otherwise return False'''
    for item in arr:
        if item == False:
            return False
    return True


def swap_level(frame, i =-2, j = -1, axis = 0):
    result = frame.copy()

    axis = frame._get_axis_number(axis)

    if not isinstance(result._get_axis(axis), MultiIndex):  # pragma: no cover
        raise TypeError("Can only swap levels on a hierarchical axis.")

    if axis == 0:
        assert isinstance(result.index, MultiIndex)
        result.index = result.index.swaplevel(i, j)
    else:
        assert isinstance(result.columns, MultiIndex)
        result.columns = result.columns.swaplevel(i, j)
    return result


class TestSwaplevelWhitebox(unittest.TestCase):
    def setUp(self):
        # Original
        self.df = pd.DataFrame({"Grade": ["A", "B", "A", "C"]},
                          index=[
                              ["Final exam", "Final exam", "Coursework", "Coursework"],
                              ["History", "Geography", "History", "Geography"],
                              ["January", "February", "March", "April"],
                          ],
                          )

        # case 1 (swaplevel no input)
        self.df_case1 = pd.DataFrame({"Grade": ["A", "B", "A", "C"]},
                                index=[["Final exam", "Final exam", "Coursework", "Coursework"],
                                       ["January", "February", "March", "April"],
                                       ["History", "Geography", "History", "Geography"],],)
        #df.case2
        self.df_case2 = pd.DataFrame({"Grade": ["A", "B", "A", "C"]},
                               index=[
                                   ["January", "February", "March", "April"],
                                   ["History", "Geography", "History", "Geography"],
                                   ["Final exam", "Final exam", "Coursework", "Coursework"],
                               ],
                               )
        #df.case3
        self.df_case3 = pd.DataFrame({"Grade": ["A", "B", "A", "C"]},
                               index=[
                                   ["History", "Geography", "History", "Geography"],
                                   ["Final exam", "Final exam", "Coursework", "Coursework"],
                                   ["January", "February", "March", "April"],
                               ],
                               )

        #column case
        arrays = [["A", "B","C"],
                  ["1", "2", "3"]]
        tuples = list(zip(*arrays))
        index = pd.MultiIndex.from_tuples(tuples,names=["first","second"])
        tmp = np.random.randn(3,3)
        self.s1 = pd.DataFrame(tmp, index=["X","Y","Z"],columns=index)

        arrays2 = [["1", "2", "3"],
                   ["A", "B", "C"]]
        tuples2 = list(zip(*arrays2))
        index2 = pd.MultiIndex.from_tuples(tuples2, names=["second", "first"])
        self.s2 = pd.DataFrame(tmp, index=["X", "Y", "Z"], columns=index2)

    def test_Swaplevel_case1_whitebox(self):
            df1_swapped = swap_level(self.df)
            # making array that is only True if all equal
            bool_arr = ((df1_swapped == self.df_case1).eq(True).all())
            self.assertTrue(all_true(bool_arr.values.tolist()))

            df2_swapped = swap_level(self.df,0)
            # making array that is only True if all equal
            bool_arr = ((df2_swapped == self.df_case2).eq(True).all())
            self.assertTrue(all_true(bool_arr.values.tolist()))

            df3_swapped = swap_level(self.df,0, 1)
            # making array that is only True if all equal
            bool_arr = ((df3_swapped == self.df_case3).eq(True).all())
            self.assertTrue(all_true(bool_arr.values.tolist()))

            df4_swapped = swap_level(self.df,0, 0)
            # making array that is only True if all equal
            bool_arr = ((df4_swapped == self.df).eq(True).all())
            self.assertTrue(all_true(bool_arr.values.tolist()))

            df5_swapped = swap_level(self.df,1, 1)
            # making array that is only True if all equal
            bool_arr = ((df5_swapped == self.df).eq(True).all())
            self.assertTrue(all_true(bool_arr.values.tolist()))

            s1_swapped = swap_level(self.s1,0,1,1)
            bool_arr = ((s1_swapped == self.s2).eq(True).all())
            self.assertTrue(all_true(bool_arr.values.tolist()))

            try:
                dfA = swap_level(self.df, 1, 1,1)
            except:
                print("Catch error swap columns")


