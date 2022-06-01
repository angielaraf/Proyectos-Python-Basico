import random
menu = """
¡Bienvenida al juego! 👊🖐✌

Elije una opción:
Piedra
Papel 
Tijera.

"""  

def run():
    opciones = ["Piedra", "Papel", "Tijera"]
    opcion_computador = random.choice(opciones)
    
    if opcion_usuario == opcion_computador:
        print ("Empate, la compu y tu eligieron: " + opcion_computador)

    elif opcion_usuario == "Piedra" and opcion_computador =="Papel":
        print("""Elegiste piedra, la compu eligió papel.
        Perdiste!
        """)
    elif opcion_usuario == "Tijera" and opcion_computador =="Papel":
        print("""Elegiste tijera, la compu eligió papel.
        Ganaste!
        """)
    elif opcion_usuario == "Papel" and opcion_computador =="Piedra":
        print("""Elegiste papel, la compu eligió piedra.
        Ganaste!
        """)
    elif opcion_usuario == "Tijera" and opcion_computador =="Piedra":
        print("""Elegiste tijera, la compu eligió piedra.
        Perdiste!
        """)
    elif opcion_usuario == "Papel" and opcion_computador =="Tijera":
        print("""Elegiste papel, la compu eligió tijera.
        Perdiste!
        """)
    elif opcion_usuario == "Piedra" and opcion_computador =="Tijera":
        print("""Elegiste piedra, la compu eligió tijera.
        Ganaste!
        """)
    else:
        print("Elige una opción correcta")
    
opcion_usuario = str(input(menu))


if __name__ == "__main__":
    run()