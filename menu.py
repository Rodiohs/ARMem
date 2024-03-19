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
    conteo_jugadores = []
    while True:
        print (chr(27) + "[2J")
        for elemento in lista_jugadores:
            print(f"\033[1;36;40m{elemento[0]}\033[0m",end=" - ")
        print("\n\033[4m ¡Menú principal!\033[0m\n\033[33m 1\033[0m - Registrar un jugador nuevo\n\033[33m 2\033[0m - Olvidar a todos los jugadores\n\033[33m 3\033[0m - Jugar\n\033[33m 4\033[0m - Salir")
        opcion=(input("Escriba 1, 2 o 3 para seleccionar una acción: "))
        if opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4":
             input(f"\033[1;31;40m Escriba únicamente 1, 2, 3 o 4 para la selección de una acción.\033[0m\nOk: Enter")
        if opcion=="4":
            exit()
        if opcion=="3":
             if len(lista_jugadores)>0:
                 return
             else:
                 input(f"\033[1;31;40m Debe haber almenos un jugador.\033[0m\nOk: Enter")
        if opcion=="2":
             print(f"\033[1;31;40m Jugadores olvidados completamente\033[0m")
             time.sleep(2)
             lista_jugadores.clear()
             conteo_jugadores.clear()
             numero_jugador=0
        if opcion=="1":
            nombre=input("Inserta un nombre, o si no desea registrar otro jugador solamente presiona enter y deja el espacio vacío.\n")
            if nombre!="":
                if nombre in conteo_jugadores:
                    print(f"\033[1;31;40m El jugador ya existe!\033[0m")
                    time.sleep(2)
                else:
                    lista_jugadores.append([])
                    lista_jugadores[numero_jugador].append(nombre)
                    conteo_jugadores.append(nombre)
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
    print(f"\033[1;31;40m ¡Preparense para jugar de nuevo!\033[0m")
    time.sleep(1)
    print(f"\033[1;31;40m ¡3!\033[0m")
    time.sleep(1)
    print(f"\033[1;31;40m ¡2!\033[0m")
    time.sleep(1)
    print(f"\033[1;31;40m¡1!\033[0m")
    time.sleep(1)
    return(lista_jugadores)
