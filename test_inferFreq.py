import pandas as pd
import unittest

class TestInferFreq(unittest.TestCase):
    """
    Test the pandas.infer_freq function.
    For given DateTimeIndex, this function should compute the frequency (= time difference
    between two dates). If the distances are not equal ("frequency is uncertain", see official
    pandas documentation of infer_freq), then the function should return None.
    Otherwise, the returned frequency is a string according to this convention:
    https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
    """

    def setUp(self):
        #interval: 3days -> "3D"
        self.idx1 = pd.DatetimeIndex(["2020-09-23", "2020-09-26", "2020-09-29"])

        #interval: not regularly, non-fitting day added
        self.err1 = pd.DatetimeIndex(["2020-09-21", "2020-09-23", "2020-09-26", "2020-09-29"])

        #interval: 12h + 15 min = 735h -> "735T"
        self.idx2 = pd.DatetimeIndex(['2025-01-21 12:15:00',
                       '2025-01-22 00:30:00', '2025-01-22 12:45:00',
                       '2025-01-23 01:00:00'])

        #interval: not regularly (just one second changed at 12:45)
        self.err2 = pd.DatetimeIndex(['2025-01-21 12:15:00',
                       '2025-01-22 00:30:00', '2025-01-22 12:45:01',
                       '2025-01-23 01:00:00'])

        #interval: 19h + 12 min + 13 sec = 69133 sec -> "69133S"
        self.idx3 = pd.DatetimeIndex(['2018-02-17 00:00:00', '2018-02-17 19:12:13',
               '2018-02-18 14:24:26', '2018-02-19 09:36:39',
               '2018-02-20 04:48:52', '2018-02-21 00:01:05'])

        #interval: not regularly (third date removed)
        self.err3 = pd.DatetimeIndex(['2018-02-17 00:00:00', '2018-02-17 19:12:13',
               '2018-02-19 09:36:39',
               '2018-02-20 04:48:52', '2018-02-21 00:01:05'])

        #interval (timedeltaIndex) -> 27H
        self.idx4 = pd.TimedeltaIndex(data =['1 days 03:00:00', '2 days 06:00:00', '3 days 09:00:00'])

        #interval: not regularly (timedeltaIndex)
        self.err4 = pd.TimedeltaIndex(data =['1 days 03:00:00', '2 days 05:42:42', '3 days 09:00:00'])



    def test_inferFreq(self):

        freq1 = pd.infer_freq(self.idx1)
        self.assertEqual(freq1, "3D")

        freq1Err = pd.infer_freq(self.err1)
        self.assertIsNone(freq1Err)

        freq2 = pd.infer_freq(self.idx2)
        self.assertEqual(freq2, "735T")

        freq2Err = pd.infer_freq(self.err2)
        self.assertIsNone(freq2Err)

        freq3 = pd.infer_freq(self.idx3)
        self.assertEqual(freq3, "69133S")

        freq3Err = pd.infer_freq(self.err3)
        self.assertIsNone(freq3Err)

        freq4 = pd.infer_freq(self.idx4)
        self.assertEqual(freq4, "27H")
        
        freq4Err = pd.infer_freq(self.err4)
        self.assertIsNone(freq4Err)


if __name__ == '__main__':
    unittest.main()
