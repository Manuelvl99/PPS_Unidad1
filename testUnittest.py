import unittest
from lista import estaEnRango, estaEnLista

class Tests(unittest.TestCase):

    def testEstaEnRango(self):

        self.assertEqual(estaEnRango(6,1,19), True)

        self.assertEqual(estaEnRango(11,1,6), False)

        self.assertRaises(ValueError, estaEnRango)

        self.assertRaises(ValueError, estaEnRango,'','b','c')

    def testEstaEnLista(self):

        listaTest=[6,14,11,3,2,1,15,19]

        self.assertEqual(estaEnLista(6, listaTest), True)

        self.assertEqual(estaEnLista(0, listaTest), False)

        self.assertRaises(ValueError, estaEnLista)

        self.assertRaises(ValueError, estaEnLista,'',listaTest)

        self.assertRaises(ValueError, estaEnLista,6,'')

if __name__ == '__main__':
    unittest.main()