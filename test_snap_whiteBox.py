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
        pass

    def test_Snap(self):
        index = pd.DatetimeIndex([0.1,0.5,0.4], freq="W")
        snap(index)




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
