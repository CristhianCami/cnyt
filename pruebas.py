import unittest
from numerosComplejos import *

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        a = (3,2)
        b = (8,9)
        self.assertEqual(suma(a,b), (11, 11))

    def test_resta(self):
        a = (4,5)
        b = (2,-5)
        self.assertEqual(resta(a,b), (2,10))

    def test_multiplicacion(self):
        a = (4,5)
        b = (3,8)
        self.assertEqual(multiplicacion(a,b), (-28,47))
        

    

if __name__ == '__main__':
    unittest.main()
