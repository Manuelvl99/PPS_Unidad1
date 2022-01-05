'''Crea una suite de tests mediante UnitTest que comprueben las 3 funciones que has
desarrollado en los ejercicios anteriores. Procura que los tests unitarios cubran lo
mejor posible la aparición de comportamientos no deseados.'''

import unittest

from binario import esBinario, convertirBinario
from lista import estaEnRango, estaEnLista

class Tests(unittest.TestCase):

    def testEsBinario(self):

        self.assertEqual(esBinario('1010'), True)

        self.assertEqual(esBinario('2022'), False)

        self.assertEqual(esBinario('Susto'), False)

        self.assertRaises(ValueError, esBinario)
    
    def testConvertirBinario(self):

        self.assertEqual(convertirBinario('1010'), 5)

        self.assertRaises(ValueError, convertirBinario, '2022')

        self.assertRaises(ValueError, convertirBinario, 'Susto')

        self.assertRaises(ValueError, convertirBinario)

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