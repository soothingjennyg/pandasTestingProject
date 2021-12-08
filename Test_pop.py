import pandas as pd
import numpy as np
import unittest

class Mytest(unittest.TestCase):
    '''
    pops and removes the item which is on the given index

    '''
    def setUp(self):
        self.ser=pd.Series([4,7,9])
    def test_pop(self):
        self.assertEqual(self.ser.pop(0),4)
        self.assertEqual(self.ser.pop(1),7)
        self.assertEqual(['hira','malik'].pop(1),('malik'))

if __name__  == '__main__':
    unittest.main()