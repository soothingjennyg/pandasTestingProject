import pandas as pd
import unittest
import numpy as np



'''
Index.unique will take an index (a list of values, used as index) and return the the unique values, in order of apperance.

Fromm documentation:

Parameters
    levelint or hashable, optional
    Only return values from specified level (for MultiIndex). If int, gets the level by integer position, else by level name.

Returns
    Index



You can specify the level if multiindex. So the cases that I see are:
- simple index, all values uniq or simple index, some or all values same
- MultiIndex, all values uniq or MultiIndex, some or all values same

I will do empty, a small and a large index for these cases.

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
        self.sequence1 = pd.Index([1, 2, 3])
        self.sequence1 = pd.Index([1, 2, 3, 3]) # two values same
        self.sequence2 = pd.Index([])
        self.sequence3 = pd.Index(list(range(0, 10000)))
        self.sequence4 = pd.Index(list(range(0, 10000)) + [4,5,6]) # 3 values same
        self.sequence5 = pd.Index(list(range(0, 10000)) + list(range(0, 5000))) # 5000 values same

        arrays = [
                ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
                ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]

        tuples = list(zip(*arrays))

        self.multiindex1  = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])



    
    def test_unique_simpleindex(self):
        sequence1_unique = self.sequence1.unique() 
        self.assertTrue(all_true(sequence1_unique == pd.Index([1, 2, 3])))
        sequence2_unique = self.sequence2.unique() 
        self.assertTrue(all_true(sequence2_unique == pd.Index([])))
        sequence3_unique = self.sequence3.unique() 
        self.assertTrue(all_true(sequence3_unique == pd.Index(list(range(0, 10000) ))))
        sequence4_unique = self.sequence4.unique() 
        self.assertTrue(all_true(sequence4_unique == pd.Index(list(range(0, 10000) ))))
        sequence5_unique = self.sequence5.unique() 
        self.assertTrue(all_true(sequence5_unique == pd.Index(list(range(0, 10000) ))))

    def test_unique_multiindex(self):
        #pick first index
        sequence6_unique = self.multiindex1.unique('first').values.tolist() 
        self.assertTrue(sequence6_unique == ['bar', 'baz', 'foo', 'qux'])

        #pick second index
        sequence6_unique = self.multiindex1.unique('second').values.tolist() 
        self.assertTrue(sequence6_unique == ["one", "two"])

        





if __name__ == '__main__':
    unittest.main()