import unittest
import numpy as np
import pandas as pd

from pandas._typing import (
    ArrayLike,
)
from typing import (
    Hashable,
)
from pandas.core.dtypes.common import (
    is_datetime64_dtype,
)
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.indexes.base import Index


class Mytest(unittest.TestCase):
    '''
    TODO: Comment
    '''
    def setUp(self):
        self.a = np.arange(np.datetime64('2005-09-03'), np.datetime64('2005-09-05'))
        self.b = np.array([1,2,3], dtype=complex)

    def test_box(self):
        output = _box_as_indexlike(self.a, True)
        self.assertTrue(output.equals(pd.DatetimeIndex(self.a, tz="utc")))

        output = _box_as_indexlike(self.b, True)
        self.assertTrue(output.equals(pd.Index(self.b, dtype= complex)))


def _box_as_indexlike(
    dt_array: ArrayLike, utc: bool, name: Hashable = None
) -> Index:
    """
    Properly boxes the ndarray of datetimes to DatetimeIndex
    if it is possible or to generic Index instead
    Parameters
    ----------
    dt_array: 1-d array
        Array of datetimes to be wrapped in an Index.
    tz : object
        None or 'utc'
    name : string, default None
        Name for a resulting index
    Returns
    -------
    result : datetime of converted dates
        - DatetimeIndex if convertible to sole datetime64 type
        - general Index otherwise
    """

    if is_datetime64_dtype(dt_array):
        tz = "utc" if utc else None
        return DatetimeIndex(dt_array, tz=tz, name=name)
    return Index(dt_array, name=name, dtype=dt_array.dtype)