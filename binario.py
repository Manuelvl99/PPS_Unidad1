'''Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
introduzca un número binario e imprima por pantalla el número en formato decimal.
Para desarrollar el programa, es necesario que desarrolles una función con la
siguiente cabecera:'''

def esBinario(strbinario=''):
    comprobacion=0
    if strbinario != '':
        for digito in strbinario:
            if digito == '0' or digito == '1':
                comprobacion = True
            else:
                comprobacion = False
                break
        if comprobacion is True:
            print("El número introducido es binario")
        else:
            print("El número introducido no es binario")
        return comprobacion
    else:
        raise ValueError("No se ha introducido valor alguno.")    

def convertirBinario(binario=''):
    if esBinario(binario):
        if binario != '':    
            n = list(binario)
            n.reverse()
            decimal = 0
            for i in range(len(binario)):
                decimal += int(binario[i]) * 2 ** i
            return decimal
        else: 
            raise ValueError("No ha introducido valor alguno.")
    else:
        raise ValueError("El valor introducido al no ser binario no puede convertirse a decimal.")

if __name__ == '__main__':
    valor = input("Introduce un número en binario: ")

    if esBinario(valor):
        print(esBinario(valor))

    if convertirBinario(valor):
        print("Su conversión a decimal es:",convertirBinario(valor))
