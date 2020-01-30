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

    def test_division(self):
        a = (3,5)
        b = (-3,-5)
        self.assertEqual(division(a,b),(-1,0))

    def test_modulo(self):
        a = (3,4)
        self.assertEqual(modulo(a),5)

    def test_conjugado(self):
        a = (3,-100)
        self.assertEqual(conjugado(a),(3,100))

    def test_conversion(self):
        a = (10,5)
        self.assertEqual(polaresACartesianas(cartesianasAPolares(a)),(10,5))

    def test_fase(self):
        a = (10,0)
        self.assertEqual(fase(a),0)
        
        

    

if __name__ == '__main__':
    unittest.main()
