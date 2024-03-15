import time

listaJugadores=[]
numeroJugador=0

def menu():
    print (chr(27) + "[2J")
    print("¡Juego de ordenar!\nMenú principal\n1 - Registro de jugadores\n2 - Iniciar el juego")
    opcion=(input("Escriba 1 o 2 para seleccionar una acción: "))
    if opcion!="1" and opcion!="2":
        print("Escriba únicamente 1 o 2 para la selección de una acción.")
        time.sleep(3)
        print (chr(27) + "[2J")
        menu()
    if opcion=="1":
         registro(listaJugadores,numeroJugador)
         menu()
    if opcion=="2":
        return

def registro(listaJugadores,numeroJugador):
    while True:
        print (chr(27) + "[2J")
        for elemento in listaJugadores:
            print(elemento[0],end=" . ")
        print("\n¡Registro de jugadores!\n1 - Registrar un jugador nuevo\n2 - Olvidar a todos los jugadores\n3 - Salir al menú para jugar")
        opcion=(input("Escriba 1, 2 o 3 para seleccionar una acción: "))
        if opcion!="1" and opcion!="2" and opcion!="3":
             print("Escriba únicamente 1, 2 o 3 para la selección de una acción.")
             time.sleep(3)
        if opcion=="3":
             return
        if opcion=="2":
             print("Jugadores olvidados completamente")
             time.sleep(2)
             listaJugadores.clear()
             numeroJugador=0
        if opcion=="1":
            nombre=input("Inserte un nombre o una S para salir al menú: ")
            if nombre=="S":
                 return
            listaJugadores.append([])
            listaJugadores[numeroJugador].append(nombre)
            numeroJugador+=1

menu()
print(listaJugadores)
print("De aquí sigue el resto del juego")