import unittest
import numpy as np
import pandas as pd
from pandas.core.tools.times import to_time
from datetime import time
import operator


class TestIndexerBetweenTime(unittest.TestCase):
    """
    The indexer_between_time function takes a DateTimeIndex (index) and two datetime-objects (start and end).
    It checks for every date of the index whether it is located between start and end. The function returns
    an array of integers that indicates which of the dates in the index fullfill this requirement.
    To measure the coverage, this file contains a copy of the indexer_between_time function as well as
    the _time_to_micros function that is called by indexer_between_time.
    """
    def setUp(self):
        self.index1 = pd.DatetimeIndex(["04:00", "08:42", "14:15", "17:47", "14:02"])
        self.start1 = time(8, 42) #08:42 h
        self.end1 = time(14, 15) #14:15 h


    def test_indexerBetweenTime(self):
        #include_ start and include_end, start_time <= end_time
        between = indexer_between_time(self.index1, self.start1, self.end1)
        self.assertEqual(len(between), 3)
        self.assertEqual(between[0], 1)
        self.assertEqual(between[1], 2)
        self.assertEqual(between[2], 4)

        #include_start and include_end, end_time < start_time
        between = indexer_between_time(self.index1, self.end1, self.start1)
        self.assertEqual(len(between), 4)
        self.assertEqual(between[0], 0)
        self.assertEqual(between[1], 1)
        self.assertEqual(between[2], 2)
        self.assertEqual(between[3], 3)

        #only include_start, start_time <= endTime
        between = indexer_between_time(self.index1, self.start1, self.end1, include_end=False)
        self.assertEqual(len(between), 2)
        self.assertEqual(between[0], 1)
        self.assertEqual(between[1], 4)

        #only include_end, start_time <= endTime
        between = indexer_between_time(self.index1, self.start1, self.end1, include_start=False)
        self.assertEqual(len(between), 2)
        self.assertEqual(between[0], 2)
        self.assertEqual(between[1], 4)

        #include neither start nor end, start_time <= endTime
        between = indexer_between_time(self.index1, self.start1, self.end1, include_start=False, include_end=False)
        self.assertEqual(len(between), 1)
        self.assertEqual(between[0], 4)






#copy of pd.DatetimeIndex.indexer_between_time
def indexer_between_time(
        self, start_time, end_time, include_start: bool = True, include_end: bool = True
) -> np.ndarray:
    """
    Return index locations of values between particular times of day
    (e.g., 9:00-9:30AM).

    Parameters
    ----------
    start_time, end_time : datetime.time, str
        Time passed either as object (datetime.time) or as string in
        appropriate format ("%H:%M", "%H%M", "%I:%M%p", "%I%M%p",
        "%H:%M:%S", "%H%M%S", "%I:%M:%S%p","%I%M%S%p").
    include_start : bool, default True
    include_end : bool, default True

    Returns
    -------
    np.ndarray[np.intp]

    See Also
    --------
    indexer_at_time : Get index locations of values at particular time of day.
    DataFrame.between_time : Select values between particular times of day.
    """
    start_time = to_time(start_time)
    end_time = to_time(end_time)
    time_micros = self._get_time_micros()
    start_micros = _time_to_micros(start_time)
    end_micros = _time_to_micros(end_time)

    if include_start and include_end:
        lop = rop = operator.le
    elif include_start:
        lop = operator.le
        rop = operator.lt
    elif include_end:
        lop = operator.lt
        rop = operator.le
    else:
        lop = rop = operator.lt

    if start_time <= end_time:
        join_op = operator.and_
    else:
        join_op = operator.or_

    mask = join_op(lop(start_micros, time_micros), rop(time_micros, end_micros))

    return mask.nonzero()[0]


def _time_to_micros(time_obj: time) -> int:
    seconds = time_obj.hour * 60 * 60 + 60 * time_obj.minute + time_obj.second
    return 1_000_000 * seconds + time_obj.microsecond
