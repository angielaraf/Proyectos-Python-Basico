
# Conversor de monedas colombianas a dolares:

plata = int(input("¿Cuanto dinero colombiano tienes?: "))
valor_dolar = 3929
dolares = plata / valor_dolar
dolares = round(dolares,2) # Con round redondeo a 2 decimales.
dolares = str (dolares)
print ("Tienes $" + dolares + " dolares")

# Conversor de dolares a monedas colombianas:

dolares = float (input("¿Cuantos dolares tienes?: "))
valor_dolar = 3929
plata = dolares * valor_dolar
plata = str (plata)
print ("Tienes " + plata + " pesos colombianos")