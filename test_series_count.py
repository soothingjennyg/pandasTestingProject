from numpy import NaN
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



class TestSeriesCount(unittest.TestCase):
    '''Functions for testing the count in pandas series functions. Count returns elements in a series, 
    but will leave out NaN:s. '''

    def setUp(self):
        self.sequence1 = [1, 2, 3]
        self.sequence2 = [1, 2, NaN]
        self.sequence3 = []
        self.sequence4 = [0]
        self.sequence5 = [NaN]
        self.sequence6 = [NaN]*500 + [6,7]
        self.sequence7 = [0]*1000000 + [1]
    
    def test_series_count_blackbox(self):
        #Want to test just a small ordinary case.
        counted_sequence1 = pd.Series.count(pd.Series(self.sequence1))
        self.assertEqual(counted_sequence1, 3)
        # Testing if NaN is dropped from the count.   
        counted_sequence2 = pd.Series.count(pd.Series(self.sequence2))
        self.assertEqual(counted_sequence2, 2)
        # Testing empty series.
        counted_sequence3 = pd.Series.count(pd.Series(self.sequence3))
        self.assertEqual(counted_sequence3, 0)
        # Testing series with just a 0.
        counted_sequence4 = pd.Series.count(pd.Series(self.sequence4))
        self.assertEqual(counted_sequence4, 1)
        # Testing series with just a NaN.
        counted_sequence5 = pd.Series.count(pd.Series(self.sequence5))
        self.assertEqual(counted_sequence5, 0)
        # Testing series with alot of NaN:s and a 2 other.
        counted_sequence6 = pd.Series.count(pd.Series(self.sequence6))
        self.assertEqual(counted_sequence6, 2)
        # Testing series with 1000000 of 0 and a one 1.
        counted_sequence7 = pd.Series.count(pd.Series(self.sequence7))
        self.assertEqual(counted_sequence7, 1000001)
        




if __name__ == '__main__':
    unittest.main()