import pandas as pd
import inspect
import unittest
import numpy as np

'''
The general.unique take a array-like object and return the unique values in it. To test this we simply pass in different lists where some 
of the values are not unique, and check if general.unique returns the right values. 


From documentation:

Parameters: values1d: array-like

Returns:
numpy.ndarray or ExtensionArray
The return can be:
    Index : when the input is an Index
    Categorical : when the input is a Categorical dtype
    ndarray : when the input is a Series/ndarray
    Return numpy.ndarray or ExtensionArray.
    
    '''




def all_true(arr):
    '''Returns True if all items in array is True.
        Otherwise return False'''
    state = True
    for item in arr:
        if item == False:
            return False
    return True



class TestUnique(unittest.TestCase):
    '''Functions for testing the unique in pandas general functions'''

    def setUp(self):
        self.sequence1 = [1, 2, 3]
        self.sequence2 = [1, 2, 3, 3]
        self.sequence3 = []
        self.sequence4 = [0]*1000000 + [1]
    
    def test_unique_blackbox(self):
        #basic uniqueness test given documentation
        sequence1_unique = pd.unique(self.sequence1) 
        
        # unique list, should stay the same
        self.assertTrue(all_true(sequence1_unique == [1, 2, 3]))
        sequence2_unique = pd.unique(self.sequence2) 
        # not unique list, should become unique
        self.assertTrue(all_true(sequence2_unique == [1, 2, 3]))
        sequence3_unique = pd.unique(self.sequence3) 
        # empty list, should stay empty
        self.assertTrue(all_true(sequence3_unique == []))
        # bigger list with alot of 0 and one 1. Should become just the 0 and the 1.
        sequence3_unique = pd.unique(self.sequence4) 
        self.assertTrue(all_true(sequence3_unique == [0,1]))




if __name__ == '__main__':
    unittest.main()