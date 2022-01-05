'''Realiza el ejercicio 4 pero utilizando esta vez cualquier otro framework de terceros
como por ejemplo pytest.'''

# Hay que instalar pytest, con el siguiente comando si se opera en Windows: pip3 install pytest.
# Para actualizar pytest, con el siguiente comando si se opera en Windows: pip --upgrade pytest.

import pytest

from binario import esBinario, convertirBinario
from lista import estaEnRango, estaEnLista


def testEsBinario():

    assert esBinario('1010') == True

    assert esBinario('2022') == False

    assert esBinario('susto') == False

    with pytest.raises(ValueError, match=r".* valor .*"):
        esBinario()

def testConvertirBinario():

    assert convertirBinario('1010') == 5

    with pytest.raises(ValueError, match=r".* valor .*"):
        convertirBinario('Susto')

    with pytest.raises(ValueError, match=r".* valor .*"):
        convertirBinario()

def testEstaEnRango():

    assert estaEnRango(6,1,19) == True

    assert estaEnRango(11,1,6) == False

    with pytest.raises(ValueError, match=r".* valor.*"):
        estaEnRango()

def testEstaEnLista():

    listaPytest=[6,14,11,3,2,1,15,19]

    assert estaEnLista(6, listaPytest) == True

    assert estaEnLista(0, listaPytest) == False

    with pytest.raises(ValueError, match=r".* error.*"):
        estaEnLista()

    with pytest.raises(ValueError, match=r".* valor.*"):
        estaEnLista(listaPytest)

    with pytest.raises(ValueError, match=r".* lista.*"):
        estaEnLista(6)
