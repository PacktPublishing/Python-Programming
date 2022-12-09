import unittest


class TestCalc(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(5%2,0)


 
if __name__ == '__main__':
    unittest.main()
