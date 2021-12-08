import pandas as pd
import numpy as np
import unittest
from pandas.core.index import DatetimeIndex
from pandas._libs.tslibs import to_offset
from pandas.core.dtypes.common import DT64NS_DTYPE
from pandas.core.arrays.datetimes import DatetimeArray


class TestSnap(unittest.TestCase):
    """
    Test the pandas.DatetimeIndex.snap function.
    The snap function takes a list of dates and will round each date. To do so, the user has to pass a second parameter
    that indicates how to round the dates. E.g. if the user passes "D" (=day), each passed date will be round to the
    nearest beginning of a day i.e. YY-MM-DD 00:00:00. If the user passes "W" (=week), each passed date will be round
    to the nearest beginning of a week, i.e. Monday at 00:00:00.

    We have two test methods. test_Snap should test the snap method and fullfill 100% statement coverage, edge coverage and
    also should pass test cases that execute the loop 0,1 and multiple times. The test_PrimePaths method should cover every
    prime path.

    To measure the statement coverage easily, we also copied the snap function (def snap) to this file because then the IDE
    can show the coverage (which is not possible for functions that are located in the library).

    We also created a second copy of snap (snapStorePath) for the control flow task. In this function, we added some append
    statements to save the executed path (integers that correspond to the node in the control flow graph).
    So we can call this function multiple times and it stores a list that contains every executed path.
    In the end, we can call the checkComplete() function (which we also implemented ourselves). For given prime paths (the
    primePaths variable has to be set by the user in advance), the checkComplete() function checks which of the prime paths
    was covered by our test cases and outputs the fullfilled prime paths and the missing prime paths. The prime path test
    is complete, if the list of missing prime paths is empty i.e. all prime paths are fullfilled.
    """
    def setUp(self):
        self.index1 = pd.DatetimeIndex(["2020-09-23", "2020-09-26", "2020-09-29"])
        self.index1W = pd.DatetimeIndex(['2020-09-20', '2020-09-27', '2020-09-27'])

        self.index2 = pd.DatetimeIndex([])

        self.index3 = pd.DatetimeIndex(["2020-09-20"])


        self.cfg1 = pd.DatetimeIndex([])
        self.cfg2 = pd.DatetimeIndex(['2021-12-08'])
        self.cfg3 = pd.DatetimeIndex(['2021-12-08'])
        self.cfg4 = pd.DatetimeIndex(['2021-12-04'])
        self.cfg5 = pd.DatetimeIndex(['2021-12-08', '2021-12-09'])
        self.cfg6 = pd.DatetimeIndex(['2021-12-08', '2021-12-05'])
        self.cfg7 = pd.DatetimeIndex(['2021-12-04', '2021-12-05'])
        self.cfg8 = pd.DatetimeIndex(['2021-12-05', '2021-12-08'])
        self.cfg9 = pd.DatetimeIndex(['2021-12-05', '2021-12-04'])
        self.cfg10 = pd.DatetimeIndex(['2021-12-08', '2021-12-04'])
        self.cfg11 = pd.DatetimeIndex(['2021-12-08', '2021-12-08'])
        self.cfg12 = pd.DatetimeIndex(['2021-12-04', '2021-12-08'])
        self.cfg13 = pd.DatetimeIndex(['2021-12-04', '2021-12-04'])

        self.cfg14 = pd.DatetimeIndex(['2021-12-05'])
        self.cfg15 = pd.DatetimeIndex(['2021-12-05', '2021-12-05'])


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
        sn = snapStorePath(self.cfg1, freq="D")
        self.assertTrue(sn.equals(self.cfg1))

        sn = snapStorePath(self.cfg2, freq="D")
        self.assertTrue(sn.equals(self.cfg2))

        sn = snapStorePath(self.cfg3, freq="W")
        self.assertTrue(sn.equals(self.cfg14))

        sn = snapStorePath(self.cfg4, freq="W")
        self.assertTrue(sn.equals(self.cfg14))

        sn = snapStorePath(self.cfg5, freq="D")
        self.assertTrue(sn.equals(self.cfg5))

        sn = snapStorePath(self.cfg6, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg7, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg8, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg9, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg10, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg11, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg12, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        sn = snapStorePath(self.cfg13, freq="W")
        self.assertTrue(sn.equals(self.cfg15))

        checkComplete()



def snap(self, freq="S") -> DatetimeIndex:
    freq = to_offset(freq)

    snapped = np.empty(len(self), dtype=DT64NS_DTYPE)

    for i, v in enumerate(self):
        s = v
        if not freq.is_on_offset(s):
            t0 = freq.rollback(s)
            t1 = freq.rollforward(s)
            if abs(s - t0) < abs(t1 - s):
                s = t0
            else:
                s = t1
        snapped[i] = s

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
        path.append(1)  # see CFG, node needed twice in the code

    path.append(3)
    executedPaths.append(path)
    dta = DatetimeArray(snapped, dtype=self.dtype)
    return DatetimeIndex._simple_new(dta, name=self.name)
