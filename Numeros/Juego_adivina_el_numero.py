import random


def run():
    aleatorio = random.randint(1,100)
    numero = int(input("Escribe un número: "))
    while aleatorio != numero:
        if numero > aleatorio:
            print ("Elige un numero más pequeño")
        else:
            print ("Elige un numero más grande")
        numero = int(input("Elige otro numero: "))
    print ("Adivinaste el numero")
if __name__ == "__main__":
    run()