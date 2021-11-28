import unittest

import pandas as pd


class TestToTimedelta(unittest.TestCase):
    def setUp(self):
        self.td_1a = pd.to_timedelta('1 D')
        self.td_1b = pd.to_timedelta('1 days')
        self.td_1c = pd.to_timedelta('1 day')
        self.td_1d = pd.to_timedelta('1 days 00:00:00')

        self.td_2a = pd.to_timedelta('1 days 23h 45m 56s')
        self.td_2b = pd.to_timedelta('1 days, 23 hours, 45 minutes, 56 seconds, 0 milliseconds, 0 microseconds')

        self.td_3a = pd.to_timedelta('1 days, 0 hours, 2 minutes')
        self.td_3b = pd.to_timedelta('1 days, 0 hours, 2 minutes, 0 seconds, 0 milliseconds, 0 microseconds')
        self.td_3c = pd.to_timedelta('1 days, 00:02:00')

        self.td_4a = pd.to_timedelta('-12:00:00')
        self.td_4b = pd.to_timedelta('-12 hours')

        self.td_5a = pd.to_timedelta(['3 hours', '1 days'])
        self.td_5b = pd.to_timedelta(['0 d, 3 h, 0m, 0s', '1 days 00:00:00'])

    def test_to_timedelta(self):
        self.assertEqual(self.td_1a, self.td_1b)
        self.assertEqual(self.td_1a, self.td_1c)
        self.assertEqual(self.td_1a, self.td_1d)
        self.assertEqual(self.td_2a, self.td_2b)
        self.assertEqual(self.td_3a, self.td_3b)
        self.assertEqual(self.td_3a, self.td_3c)
        self.assertEqual(self.td_4a, self.td_4b)
        self.assertTrue(self.td_5a.equals(self.td_5b))

        self.assertRaises(ValueError, pd.to_timedelta, 'y7909j8yn')
        self.assertRaises(ValueError, pd.to_timedelta, 'day')
        self.assertRaises(ValueError, pd.to_timedelta, '#')
        self.assertRaises(ValueError, pd.to_timedelta, '1 days, -23 hours, 45 minutes')
        self.assertRaises(ValueError, pd.to_timedelta, '1 days 23h 45m 56s 0')
        self.assertRaises(ValueError, pd.to_timedelta, '25:12')


if __name__ == '__main__':
    unittest.main()
