import pandas as pd
import numpy as np
import unittest




def all_true(arr):
    '''Returns True if all items in array is True.
        Otherwise return False'''
    for item in arr:
        if item == False:
            return False
    return True



class TestUnique(unittest.TestCase):
    '''Functions for testing the unique in pandas index'''

    def setUp(self):
        #original
        self.df1 = pd.DataFrame({"A":[10, 11, 7, 8, 5],
                   "B":[21, 5, 32, 4, 6],
                   "C":[11, 21, 23, 7, 9],
                   "D":[1, 5, 3, 8, 6]}, 
                   index =["A1", "A2", "A3", "A4", "A5"])

        #swapped
        self.df2 = pd.DataFrame({"A1":[10, 21, 11, 1], 
                                 "A2":[11, 5, 21, 5], 
                                 "A3":[7, 32, 23, 3], 
                                 "A4":[8, 4, 7, 8], 
                                 "A5":[5, 6, 9, 5]},   
                   index =["A", "B", "C", "D"])


    def test_unique_blackbox(self):
        #swapping axes
        df1_swapped = self.df1.swapaxes(axis1="index", axis2="columns")
        # making array that is only True if all equal
        bool_arr = ((df1_swapped == self.df2).eq(True).all())
        print(bool_arr)

        self.assertTrue(all_true(bool_arr.values.tolist()))




if __name__ == '__main__':
    unittest.main()