import pandas as pd
import unittest

''' Interchange axes and swap values axes appropriately.

    What we are testing here is if the swap of columns and rows in a dataframe is correct. Rows become columns and columns become rows.

    For testcases we are doing three (empty table doesn't work). The testcases are:
    Table with one entry, a small symmetric table and a bigger not symmetric table.

'''
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

        #case 1
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
                                 "A5":[5, 6, 9, 6]},   
                   index =["A", "B", "C", "D"])

        #case 2
        self.df3 = pd.DataFrame({"A":[0]}, 
                        index =["A"])


        #case 3
        self.df4 = pd.DataFrame({"A":[0,1],
                                 "B":[2,3]}, 
                        index =["A1","A2"])

        #swapped
        self.df5 = pd.DataFrame({"A1":[0,2],
                                 "A2":[1,3]}, 
                        index =["A","B"])


    def test_unique_blackbox(self):
        #case 1
        #bigger not symmetric table
        df1_swapped = self.df1.swapaxes(axis1="index", axis2="columns")
        # making array that is only True if all equal
        bool_arr = ((df1_swapped == self.df2).eq(True).all())
        self.assertTrue(all_true(bool_arr.values.tolist()))

        #case 2
        # Table with one entry
        df3_swapped = self.df3.swapaxes(axis1="index", axis2="columns")
        # making array that is only True if all equal
        bool_arr = ((df3_swapped == self.df3).eq(True).all())
        self.assertTrue(all_true(bool_arr.values.tolist()))

        #case 3
        # small symmetric table
        df4_swapped = self.df4.swapaxes(axis1="index", axis2="columns")
        # making array that is only True if all equal
        bool_arr = ((df4_swapped == self.df5).eq(True).all())
        self.assertTrue(all_true(bool_arr.values.tolist()))



if __name__ == '__main__':
    unittest.main()



    