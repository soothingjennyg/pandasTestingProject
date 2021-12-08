from numpy import NaN
import pandas as pd
import unittest
import numpy as np

    
'''
The series.count function that we are testing does:

    Return number of non-NA/null observations in the Series.

    Parameters
    ----------
    level : int or level name, default None
        If the axis is a MultiIndex (hierarchical), count along a
        particular level, collapsing into a smaller Series.

    Returns
    -------
    int or Series (if level specified)
        Number of non-null values in the Series.

This means that series will count number of things in a series, except for NaN:s. 

If the series have multindex (several indexes), you have to pick a level.
A level is a thing used when you have multiple indexes. Say you have two indexes for each entry , 
then level 0 is the first index and level 1 is the second index. Given a multiindex series, count will count
how many values each value in the chosen index holds.
If you have an index [1,2,3] for values [a,b,c], it will return :
1    1
2    1
3    1

If the index for some reason is [1,1,2,3] for [a,b,c,d] it will return:
1    2
2    1
3    1 

Finally if one of the values is NaN, index [1,1,2,3] for values [a,b,c,NaN], the NaN isn't counted:

1    2
2    1
3    0

##############################################
Analysis with interface based approach:
The parameters the function takes is a series and maybe a level. 

So the input domain can be: 
"A series and no level" 
"A series with a level"


A note is that you get a warning when you add the levels parameter becaues it will be removed in a future version. 
In the futer you will have to perform a group by before you do the count, like this:
s.groupby(level=1).count()

instead of:
pandas.Series.count(s,1)

This is a good choice I think.


'''


def all_true(arr):
    '''Returns True if all items in array is True.
        Otherwise return False'''
    state = True
    for item in arr:
        if item == False:
            return False
    return True

def all_true_index(arr):
    #need to fix this one to be more general
    '''Returns True if all items in a series with index all is True.
        Otherwise return False

        input will be in the form:
        1    True
        2    True
        3    True
        dtype: bool

        This will only work if the index i is int
        '''

    state = True
    for i in range(1,len(arr)):
        #print("arr0: " + str(arr[0]))
        if arr[i] == False:
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


        self.sequence8 = pd.Series([1, 2, 3],index=[
            np.array([1,2,3]),
            np.array([15,16,16]),
        ])
    
    def test_series_count_blackbox(self):
        "A series and no level" 
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
        
    def test_series_count_multiindex(self):

        "A series with a level"
        # should count [1,1,1] becaus we have three different indexes
        counted_sequence8  = pd.Series.count(self.sequence8,0).values.tolist()
        self.assertEqual(counted_sequence8, [1,1,1])

        #this one should count index 16 twice, and give us [1,2]
        counted_sequence9  = pd.Series.count(self.sequence8,1).values.tolist()
        self.assertEqual(counted_sequence9, [1,2])

        #this one should count index 16 twice, and give us [1,2]
        counted_sequence9  = pd.Series.count(self.sequence8,1).values.tolist()
        self.assertEqual(counted_sequence9, [1,2])




if __name__ == '__main__':
    unittest.main()