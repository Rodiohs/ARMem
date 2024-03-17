import time

def menu_inicio(lista_jugadores:list):
    """menu_inicio es una función que facilita al usuario la interfaz mediante la cuál puede seleccionar las acciones a
    realizar antes de jugar, las cuales son agregar a los jugadores, eliminar a los jugadores agregados, empezar el juego
    y salir del programa.

    Args:
        lista_jugadores (list): la lista de los jugadores se recibe estando vacía y en la función menú se le agregan los
        nombres de los jugadores
    
    Autor:
        Jairo González
    """
    numero_jugador = 0
    while True:
        print (chr(27) + "[2J")
        for elemento in lista_jugadores:
            print(elemento[0],end=" . ")
        print("\n¡Menú principal!\n1 - Registrar un jugador nuevo\n2 - Olvidar a todos los jugadores\n3 - Jugar\n4 - Salir")
        opcion=(input("Escriba 1, 2 o 3 para seleccionar una acción: "))
        if opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4":
             input("Escriba únicamente 1, 2, 3 o 4 para la selección de una acción.\nOk: Enter")
        if opcion=="4":
            exit()
        if opcion=="3":
             if len(lista_jugadores)>0:
                 return
             else:
                 input("Debe haber almenos un jugador.\nOk: Enter")
        if opcion=="2":
             print("Jugadores olvidados completamente")
             time.sleep(2)
             lista_jugadores.clear()
             numero_jugador=0
        if opcion=="1":
            nombre=input("Inserta un nombre, o si no desea registrar otro jugador solamente presiona enter y deja el espacio vacío.\n")
            if nombre!="":
                lista_jugadores.append([])
                lista_jugadores[numero_jugador].append(nombre)
                numero_jugador+=1

def remenu(lista_jugadores):
    """remenu da un pequeño aviso de que la partida va a comenzar en los casos en los que los jugadores repitan el juego
    con los mismos usuarios, sin tener que pasar por menu_inicio

    Args:
        lista_jugadores (_type_): la lista de los jugadores
    Autor:
        Rafael Odio
    """
    time.sleep(1)
    print("¡Preparense para jugar de nuevo!")
    time.sleep(1)
    print("¡3!")
    time.sleep(1)
    print("¡2!")
    time.sleep(1)
    print("¡1!")
    time.sleep(1)
    return(lista_jugadores)
