'''Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
otros programas.'''
lista=(6,14,11,3,2,1,15,19)
valor=int(input("Escriba el número a buscar: "))
minimo=min(lista)
maximo=max(lista)

def estaEnLista(valor,lista):
    comprobacion=valor in lista
    return comprobacion  
print(estaEnLista(valor,lista))

def estaEnRango(valor,minimo,maximo):
    comprobacion=0
    if valor > minimo < maximo:
        comprobacion = True
    else:
        comprobacion = False
    return comprobacion
print(estaEnRango(valor,minimo,maximo))
