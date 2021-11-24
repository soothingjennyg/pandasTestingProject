import pandas as pd
import inspect
import unittest


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

    
    def test_unique_blackbox(self):
        #basic uniqueness test given documentation
        sequence1_unique = pd.unique(self.sequence1) 
        self.assertTrue(all_true(sequence1_unique == [1, 2, 3]))
        sequence2_unique = pd.unique(self.sequence2) 
        self.assertTrue(all_true(sequence2_unique == [1, 2, 3]))
        sequence3_unique = pd.unique(self.sequence3) 
        self.assertTrue(all_true(sequence3_unique == []))




if __name__ == '__main__':
    unittest.main()