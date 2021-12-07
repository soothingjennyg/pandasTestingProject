import pandas as pd
import numpy as np
import unittest
from pandas.core.index import DatetimeIndex
from pandas._libs.tslibs import to_offset
from pandas.core.dtypes.common import DT64NS_DTYPE
from pandas.core.arrays.datetimes import DatetimeArray


class TestSnap(unittest.TestCase):
    """
    TODO: Comment
    """
    def setUp(self):
        self.index1 = pd.DatetimeIndex(["2020-09-23", "2020-09-26", "2020-09-29"])
        self.index1W = pd.DatetimeIndex(['2020-09-20', '2020-09-27', '2020-09-27'])

        self.index2 = pd.DatetimeIndex([])

        self.index3 = pd.DatetimeIndex(["2020-09-20"])

    def test_Snap(self):
        #not 100% statements:
        sn = snap(self.index1, freq="D")
        self.assertTrue(sn.equals(self.index1))


        #100 % statements:
        sn = snap(self.index1, freq="W")
        self.assertTrue(sn.equals(self.index1W))


        #edge coverage
        sn = snap(self.index1, freq="D")
        self.assertTrue(sn.equals(self.index1))
        sn = snap(self.index1, freq="W")
        self.assertTrue(sn.equals(self.index1W))


        #loop 0, 1, multiple times
        sn = snap(self.index2, freq="D")
        self.assertTrue(sn.equals(self.index2))

        sn = snap(self.index3, freq="W")
        self.assertTrue(sn.equals(self.index3))

        sn = snap(self.index1, freq="W")
        self.assertTrue(sn.equals(self.index1W))


    def test_PrimePaths(self):
        sn = snapStorePath(self.index1, freq="D")
        self.assertTrue(sn.equals(self.index1))

        sn = snapStorePath(self.index1, freq="W")
        self.assertTrue(sn.equals(self.index1W))

        sn = snapStorePath(self.index2, freq="D")
        self.assertTrue(sn.equals(self.index2))

        sn = snapStorePath(self.index3, freq="W")
        self.assertTrue(sn.equals(self.index3))

        checkComplete()



def snap(self, freq="S") -> DatetimeIndex:
    print("\nNode 0")
    print("Node 1")
    freq = to_offset(freq)

    snapped = np.empty(len(self), dtype=DT64NS_DTYPE)

    for i, v in enumerate(self):
        print("Node 2")
        s = v
        if not freq.is_on_offset(s):
            print("Node 4")
            t0 = freq.rollback(s)
            t1 = freq.rollforward(s)
            if abs(s - t0) < abs(t1 - s):
                print("Node 5")
                s = t0
            else:
                print("Node 6")
                s = t1
        print("Node 7")
        snapped[i] = s

    print("Node 3\n")
    dta = DatetimeArray(snapped, dtype=self.dtype)
    return DatetimeIndex._simple_new(dta, name=self.name)



primePaths = [[0, 1, 3],    #size 3

              [2, 7, 1, 2], [2, 7, 1, 3], [6, 7, 1, 3], [7, 1, 2, 7],   #size 4

              [0, 1, 2, 4, 5, 7], [0, 1, 2, 4, 6, 7], [1, 2, 4, 5, 7, 1],
              [1, 2, 4, 6, 7, 1], [2, 4, 5, 7, 1, 2], [2, 4, 5, 7, 1, 3],
              [2, 4, 6, 7, 1, 2], [2, 4, 6, 7, 1, 3], [4, 5, 7, 1, 2, 4],
              [4, 6, 7, 1, 2, 4], [5, 7, 1, 2, 4, 5], [5, 7, 1, 2, 4, 6],
              [6, 7, 1, 2, 4, 5], [6, 7, 1, 2, 4, 6], [7, 1, 2, 4, 5, 7], [7, 1, 2, 4, 6, 7]    #size 6
              ]


def checkComplete():
    missing = []
    fullfilled = []
    for primePath in primePaths:
        primePathStr = "".join(str(num) for num in primePath)
        found = False
        for executedPath in executedPaths:
            executedPathStr = "".join(str(num) for num in executedPath)
            if primePathStr in executedPathStr:
                found = True
                break

        if found:
            fullfilled.append(primePath)
        else:
            missing.append(primePath)

    print("\n Missing prime paths: ", missing)
    print("\n Fulfilled prime paths: ", fullfilled)
    return missing


executedPaths = []
def snapStorePath(self, freq="S") -> DatetimeIndex:
    path = []
    path.append(0)
    path.append(1)
    freq = to_offset(freq)

    snapped = np.empty(len(self), dtype=DT64NS_DTYPE)

    for i, v in enumerate(self):
        path.append(2)
        s = v
        if not freq.is_on_offset(s):
            path.append(4)
            t0 = freq.rollback(s)
            t1 = freq.rollforward(s)
            if abs(s - t0) < abs(t1 - s):
                path.append(5)
                s = t0
            else:
                path.append(6)
                s = t1
        path.append(7)
        snapped[i] = s

    path.append(3)
    executedPaths.append(path)
    dta = DatetimeArray(snapped, dtype=self.dtype)
    return DatetimeIndex._simple_new(dta, name=self.name)
