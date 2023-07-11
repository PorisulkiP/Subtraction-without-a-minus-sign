import unittest

from subtraction import subtract_using_twos_complement  

class TestBinaryOperations(unittest.TestCase):
    def setUp(self):
        self.func = subtract_using_twos_complement

    def test_small_numbers(self):
        self.assertEqual(self.func(5, 2), 3)
        self.assertEqual(self.func(100, 50), 50)

    def test_large_numbers(self):
        self.assertEqual(self.func(1500000000, 1499999999), 1)
        self.assertEqual(self.func(10000000000000000, 9999999999999999), 1)

    def test_very_large_numbers(self):
        self.assertEqual(self.func(10**100, 10**100 - 1), 1)

    def test_subtract_zero(self):
        self.assertEqual(self.func(1500000000, 0), 1500000000)
        self.assertEqual(self.func(0, 0), 0)

    def test_subtract_itself(self):
        self.assertEqual(self.func(1500000000, 1500000000), 0)

if __name__ == '__main__':
    unittest.main()
