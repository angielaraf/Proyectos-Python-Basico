def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador = 0
    for i in range (1, numero + 1):
        if numero == i or i == 1:
            continue
        if numero % i == 0:
            contador += 1
        if contador == 0:
            return True
        else:
            return False

        
            

def run ():
    numero = int (input("Escribe un numero: "))
    if es_primo(numero)== True:
        numero = str(numero)
        print ("Hola. El numero " + numero + " es primo")
    else:
        print("Hola. El numero no es primo")


if __name__ == "__main__":
    run()