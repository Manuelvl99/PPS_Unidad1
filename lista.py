'''Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
cabeceras'''

usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "manuelvl": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "hola22"
    }
 }

def estaEnLista(usuarios):
    intentos=0
    while intentos<3:
        User = input("Escriba su usuario: ")
        Pass = input("Escriba su password: ")
        intentos=intentos+1
        if User in usuarios and Pass == usuarios[User]['password']:
            print(usuarios[User]['nombre'])
            print(usuarios[User]['apellido'])
            break
        else:
            print("Usuario y/o contraseña no encontrados.")
print(estaEnLista(usuarios))