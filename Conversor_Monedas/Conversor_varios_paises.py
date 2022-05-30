# Con windows. puedo poner emojis.
menu = """
Bienvenidos al conversor de monedas plus!!😎

¿Que tipo de moneda tienes ?, elige una opción:

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

"""

def calculos(tipo_pesos, valor_dolar):
    plata = int(input("¿Cuanto dinero" + tipo_pesos + " tienes?: "))
    dolares = plata / valor_dolar
    dolares = round(dolares,2) # Con round redondeo a 2 decimales.
    dolares = str (dolares)
    print ("Tienes $" + dolares + " dolares")
opcion = int (input (menu))

if opcion == 1:
    calculos ("colombianos", 3929)

elif opcion == 2:
    calculos ("argentinos", 65)

elif opcion == 3:
    calculos ("mexicanos", 24)

else:
    print ("Ingresa una opción correcta")