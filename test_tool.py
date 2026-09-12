import unittest
from tool import flags
class OutlierTests(unittest.TestCase):
 def test_flags(self):self.assertEqual(flags([10,10,10,40],3),[False,False,False,True])
if __name__=='__main__':unittest.main()
