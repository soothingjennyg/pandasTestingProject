import pandas as pd
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
        self.sequence1 = pd.Index([1, 2, 3])
        self.sequence2 = pd.Index([1, 2, 3, 3])
        self.sequence3 = pd.Index([])

    
    def test_unique_blackbox(self):
        #basic uniqueness test given documentation
        sequence1_unique = self.sequence1.unique() 
        self.assertTrue(all_true(sequence1_unique == pd.Index([1, 2, 3])))
        sequence2_unique = self.sequence2.unique() 
        self.assertTrue(all_true(sequence2_unique == pd.Index([1, 2, 3])))
        sequence3_unique = self.sequence3.unique() 
        self.assertTrue(all_true(sequence3_unique == pd.Index([])))




if __name__ == '__main__':
    unittest.main()