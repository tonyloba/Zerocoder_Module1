import unittest
# Import from the same directory
from .main import add, subtract, multiply, divide, check, divide_zero, modulo

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)

   def test_divide(self):
       self.assertNotEqual(divide(4, 2), 3)
       self.assertEqual(divide(20, 5), 4)

class TestCheck(unittest.TestCase):
   def test_check(self):
       self.assertTrue(check(2))
       self.assertTrue(check(6))
       self.assertTrue(check(220))

       self.assertFalse(check(1))
       self.assertFalse(check(3))
       self.assertFalse(check(57))

class TestDivide(unittest.TestCase):
   def test_divide_success(self):
       self.assertEqual(divide(10, 2), 5)
       self.assertEqual(divide(6, 3), 2)
       self.assertEqual(divide(70, 2), 35)

   def test_divide_by_zero(self):
       self.assertRaises(ValueError, divide, 6, 0)

class TestModulo(unittest.TestCase):
    def test_modulo_success(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 7), 6)
        self.assertEqual(modulo(15, 14), 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)



if __name__ == '__main__':
   unittest.main()
