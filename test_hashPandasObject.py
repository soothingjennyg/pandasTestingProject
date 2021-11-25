import pandas as pd
from pandas.util import hash_pandas_object as hash
from numpy import random
import unittest

class TestHashPandasObject(unittest.TestCase):
    """
    Test the function for hashing of a pandas object (e.g. index or data frames)
    All parameters (except of the hashed object) are set to their default value (perhaps
    also the usual case in practice).

    We have the following requirements on a hash (that we check in this test):
    - It should be deterministic i.e. same hash for same object
    - It should be different for different objects
    """

    def setUp(self):
        self.big1 = createRandomIdx(100000, 42)
        self.big1s = createRandomIdx(100000, 42)
        self.big2 = createRandomIdx(100000, 43)

        self.small1 = pd.Index([1,5,7,19,16,4])
        self.small1s = pd.Index([5,1,4,19,16,4,7,16])
        self.small1sd = pd.Index([-3,42,5,29,6,16])
        self.small2 = pd.Index([67,-9,3,-20,40,60,64])

        self.big1f = createRandomIdx(31241, 923).to_frame()
        self.big1fs = createRandomIdx(31241, 923).to_frame()
        self.big2f = createRandomIdx(31241, 753).to_frame()



    def test_hashPandasObject(self):

        #1. test small index containing the same numbers
        self.assertTrue(allHashEqual(hash(self.small1), hash(self.small1s)))
        self.assertTrue(someHashEqual(hash(self.small1), hash(self.small1s)))

        #2. test small index containing different numbers and also same numbers
        self.assertTrue(someHashEqual(hash(self.small1), hash(self.small1sd)))
        self.assertFalse(allHashEqual(hash(self.small1), hash(self.small1sd)))

        #3. test small index only containing different numbers
        self.assertFalse(someHashEqual(hash(self.small1), hash(self.small2)))
        self.assertFalse(allHashEqual(hash(self.small1), hash(self.small2)))

        #4. check big random index (hashes should all be same for same seeds)
        self.assertTrue(allHashEqual(hash(self.big1), hash(self.big1s)))
        self.assertTrue(someHashEqual(hash(self.big1), hash(self.big1s)))

        #5. check big random index (hashes should all be different for different seeds)
        self.assertFalse(allHashEqual(hash(self.big1), hash(self.big2)))
        self.assertFalse(someHashEqual(hash(self.big1), hash(self.big2)))

        #6. check big random frame (hashes should all be same for same seeds)
        self.assertTrue(allHashEqual(hash(self.big1f), hash(self.big1fs)))
        self.assertTrue(someHashEqual(hash(self.big1f), hash(self.big1fs)))

        #7. check big random frame (hashes should all be different for different seeds)
        self.assertFalse(allHashEqual(hash(self.big1f), hash(self.big2f)))
        self.assertFalse(someHashEqual(hash(self.big1f), hash(self.big2f)))


#HELPER FUNCTIONS FOR COMPARISON OF HASHES :

def someHashEqual(h1, h2):
    s1 = toSet(h1)
    s2 = toSet(h2)
    return len(set.intersection(s1, s2)) > 0


def allHashEqual(h1, h2):
    s1 = toSet(h1)
    s2 = toSet(h2)
    return (len(s1) == len(s2)) and (s1 == set.intersection(s1, s2))

def toSet(hashes):
    s = set()
    for val in hashes:
        s.add(val)
    return s

#HELPER FUNCTION FOR CREATION OF (BIG) INDEX:

def createRandomIdx(length, seed):
    random.seed(seed)
    arr = random.rand(length)
    return pd.Index(arr)

