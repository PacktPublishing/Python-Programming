import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(2, -1), 1)
        self.assertEqual(calc.add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(calc.subtract(2, 1), 1)
        self.assertEqual(calc.subtract(2, 2), 0)
        self.assertEqual(calc.subtract(10, 5), 5)

 
if __name__ == '__main__':
    unittest.main()