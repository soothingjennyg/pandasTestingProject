import pandas as pd
import unittest

class TestIndexSize(unittest.TestCase):
    def setUp(self):
        self.Index1 = pd.Index(['Apple','Banana'])
        self.Index2 = pd.Index(['dog','cat','pecock'])
        self.Index3 = pd.Index([],dtype='string')
        self.Index4 = pd.Index([2,3,1])
        self.Index5 = pd.Index([4,5])
        self.Index6 = pd.Index([],dtype='int')
       

    def test_index_size(self):
        self.assertEqual(self.Index1.size,2)
        self.assertEqual(self.Index2.size,3)
        self.assertEqual(self.Index3.size,0)
        self.assertEqual(self.Index4.size,3)
        self.assertEqual(self.Index5.size,2)
        self.assertEqual(self.Index6.size,0)
        




if __name__ == '__main__':
    unittest.main()
