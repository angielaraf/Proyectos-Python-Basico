#/*
 #* Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 #* Podrás configurar generar contraseñas con los siguientes parámetros:
 #* - Longitud: Entre 8 y 16.
 #* - Con o sin letras mayúsculas.
 #* - Con o sin números.
 #* - Con o sin símbolos.
 #* (Pudiendo combinar todos estos parámetros entre ellos)
 #*/
 
#Random nos permite seleccionar aletoriamiente elementos.
import random

def constrasenagenerada(lenght = 8, capital = False, numbers = False, symbols=False):

    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "L", "M", "n", "o", "p", "q","r","s", "t", "u","v","w","x","y","z"]

    password = ""

    final_lenght = 8 if lenght < 8 else 16 if lenght > 16 else lenght

#Hacemos un while para que sea un ciclo que vaya a preguntarlo cuantos caracteres tiene la contraseña hasta llegar al tamaño definido.

    while len(password) < lenght:

        password += random.choice(characters)

    return password

print (constrasenagenerada(lenght=25))