'''Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
otros programas.'''

lista=[6,14,11,3,2,1,15,19]
minimo=min(lista)
maximo=max(lista)

def estaEnRango(valor='',minimo='',maximo=''):
    if valor !='' and minimo !='' and maximo !='':
        if isinstance(valor, int) and isinstance(minimo, int) and isinstance(maximo, int):
            return valor >= minimo and valor <= maximo
        else:
            print(ValueError("No se ha introducido parámetro alguno."))
    elif valor == '':
        raise ValueError("No se ha introducido parámetro alguno.")
    elif minimo == '':
        raise ValueError("No se ha introducido parámetro mínimo alguno.")
    elif maximo == '':
        raise ValueError("No se ha introducido parámetro máximo alguno.")

def estaEnLista(valor='',lista=''):
    if valor !='' and lista !='':
        if isinstance(valor, int):
            comprobacion=valor in lista
            return comprobacion 
        else:
            raise ValueError ("Se ha introducido un valor erróneo.")
    elif valor == '' and lista == '':
        raise ValueError("No se ha introducido parámetro alguno.")
    elif valor == '' and lista != '':
        raise ValueError("No se ha introducido valor alguno.")
    elif valor != '' and lista == '':
        raise ValueError("No hay lista alguna.")

if __name__ == '__main__':
    valor=int(input("Introduzca un número del 1 al 20: "))
    if valor >=1 and valor <=20:
        if estaEnLista(valor,lista):
            print("El número se encuentra en lista.")
        else:
            print("El número no se encuentra en lista.")
    else:
        print("El número introducido se está fuera del rango solicitado.")