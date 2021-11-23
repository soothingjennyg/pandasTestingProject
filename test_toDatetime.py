import pandas as pd
import numpy as np
import unittest

class TestToDateTime(unittest.TestCase):
    """
    Test the pandas.to_datetime function.
    This test focuses on the parameters 'arg', 'dayfirst' and 'format'.
    The other parameters are not changed and therefore tested with their default values.
    This decision comes from the fact that we suspect that some parameters are most often
    used with default value in practice. In addition, the to_datetime function has
    so many parameters that a test, which considers all combinations, is not feasible.
    """
    def setUp(self):
        self.d1 = 15042020
        self.f1 = "%d%m%Y"

        self.d2 = "17-02-2023"

        self.d3 = pd.DataFrame({'year': [2009, 2017],
                           'month': [4, 8],
                           'day': [10, 27]})

        self.d4 = ["16-4-1997", "08-03-2001"]

        self.d5 = 20060511.000
        self.f5 = "%Y%d%m"

        self.d6 = pd.Series(
            data={'born': "19520416", 'marry': "19751103", 'death': "20430404"})
        self.f6 = "%Y%m%d"

        #edge cases following:

        #july has 31 days -> no exception
        self.d7 = "2021-07-31"

        #leap-year -> no exception
        self.d8 = "2016-02-29"

        #non-existing dates (exception required!)
        self.d9 = "2005-14-03"
        self.d10 = "2005-09-32"
        self.d11 = "2021-06-31"
        self.d12 = "2015-02-29"

    def test_toDatetime(self):
        d1 = pd.to_datetime(self.d1, format=self.f1)
        self.assertEqual(d1, np.datetime64("2020-04-15"))

        d2 = pd.to_datetime(self.d2, dayfirst=True)
        self.assertEqual(d2, np.datetime64("2023-02-17"))

        d3 = (pd.to_datetime(self.d3))
        self.assertEqual(d3[0], np.datetime64("2009-04-10"))
        self.assertEqual(d3[1], np.datetime64("2017-08-27"))

        d4 = pd.to_datetime(self.d4, dayfirst=True)
        self.assertEqual(d4[0], np.datetime64("1997-04-16"))
        self.assertEqual(d4[1], np.datetime64("2001-03-08"))

        d5 = pd.to_datetime(self.d5, format=self.f5)
        self.assertEqual(d5, np.datetime64("2006-11-05"))

        d6 = pd.to_datetime(self.d6, format = self.f6)
        self.assertEqual(d6['born'], np.datetime64("1952-04-16"))
        self.assertEqual(d6['marry'], np.datetime64("1975-11-03"))
        self.assertEqual(d6['death'], np.datetime64("2043-04-04"))

        d7 = pd.to_datetime(self.d7)
        self.assertEqual(d7, np.datetime64("2021-07-31"))

        d8 = pd.to_datetime(self.d8)
        self.assertEqual(d8, np.datetime64("2016-02-29"))

        for date in [self.d9, self.d10, self.d11, self.d12]:
            try:
                pd.to_datetime(date)
            except:
                continue
            else:
                self.fail('Missing exception for invalid date')


if __name__ == '__main__':
    unittest.main()
