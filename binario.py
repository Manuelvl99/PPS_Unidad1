'''Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
introduzca un número binario e imprima por pantalla el número en formato decimal.
Para desarrollar el programa, es necesario que desarrolles una función con la
siguiente cabecera:'''

def esBinario(binario):
    n = list(binario)
    n.reverse()
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 ** i
    return decimal
try:
    print(esBinario(input("Introduzca un número binario que quiera convertir a decimal: ")))
except ValueError:
    print("Ha introducido un valor incorrecto.")
