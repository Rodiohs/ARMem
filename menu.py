import time

numero_jugador = 0
lista_jugadores = []

def menu_inicio(lista_jugadores):
    print (chr(27) + "[2J")
    print("¡Juego de ordenar!\nMenú principal\n1 - Registro de jugadores\n2 - Iniciar el juego")
    opcion=(input("Escriba 1 o 2 para seleccionar una acción: "))
    if opcion!="1" and opcion!="2":
        print("Escriba únicamente 1 o 2 para la selección de una acción.")
        time.sleep(3)
        print (chr(27) + "[2J")
        menu_inicio()
    if opcion=="1":
         registro(lista_jugadores,numero_jugador)
    if opcion=="2":
        return(lista_jugadores)

def registro(lista_jugadores,numero_jugador):
    while True:
        print (chr(27) + "[2J")
        for elemento in lista_jugadores:
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
             lista_jugadores.clear()
             numero_jugador=0
        if opcion=="1":
            nombre=input("Inserte un nombre o una S para salir al menú: ")
            if nombre=="S":
                 return
            lista_jugadores.append([])
            lista_jugadores[numero_jugador].append(nombre)
            numero_jugador+=1

def remenu(lista_jugadores):
    time.sleep(1)
    print("Preparense para jugar de nuevo!")
    time.sleep(1)
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(1)
    return(lista_jugadores)
