import ARMem as ar
import menu
import Resultados
import time
import random

def juego():
    """Aqui se realiza el juego de memoria con AR, ocurren todos los llamados a otras funciones y se crea todo lo necesario
       para que los usuarios puedan jugar. No cuenta con interfaz grafica por lo que las instrucciones y interacciones con 
       el usuario se dan a travez de la terminal, y la camara del dispositivo.
       El juego consta de memorizar un orden aleatorio de frutas, donde el usuario tendra 5 codigos en papel estilo QR, los
       cuales con la camara de dispositivo podra identificar, la mision del jugador es ordenar estos papeles en el orden
       proporcionado en el menor tiempo posible, y asi competir con demas personas. Se hacen 3 niveles de 5 iteraciones cada
       una, en el nivel 1 se inicia con 3 papeles por ordenar, sumando uno por cada nivel, hasta llegar a 5.

       Autores:
            Jairo González, Rafael Odio
    """
    if len(lista_jugadores) == 0:
        menu.menu_inicio(lista_jugadores) #En caso de que no hubieran jugadores, se ingresarán con la función menú
    else:
        menu.remenu(lista_jugadores)#si los jugadores están repitiendo con los mismos usuarios de una partida anterior

    for jugador in lista_jugadores:
        jugador.extend([0,0,0]) #A cada jugador le agrega los campos que se usarán para ir sumando los tiempos de cada uno.
    print(lista_jugadores)

    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempo_total=0
    for n in range(0,3):
        print("Nivel",n+1)
        for r in range(0,5):
            print("Ronda",r+1)
            for jugador in lista_jugadores:
                input(f"El siguiente es el turno de {jugador[0]}\nPresiona enter cuando estés listo...")
                lista_juego_actual = random.sample(lista_juego,3+n) #Se crea una lista aleatoria con 3+n cantidad de digitos, de orden aleatorio, y se cambia cada numero por su respectivo nombre de fruta
                lista_armem = lista_juego_actual.copy()
                if 0 in lista_juego_actual:
                    index = lista_juego_actual.index(0)
                    lista_juego_actual[index] = "Piña"
                if 1 in lista_juego_actual:
                    index = lista_juego_actual.index(1)
                    lista_juego_actual[index] = "Cereza"
                if 2 in lista_juego_actual:
                    index = lista_juego_actual.index(2)
                    lista_juego_actual[index] = "Uva"
                if 3 in lista_juego_actual:
                    index = lista_juego_actual.index(3)
                    lista_juego_actual[index] = "Pera"
                if 4 in lista_juego_actual:
                    index = lista_juego_actual.index(4)
                    lista_juego_actual[index] = "Guanabana"
                print(f'Memoriza la siguiente secuencia...')
                for fruta in lista_juego_actual:
                    print(lista_juego_actual.index(fruta)+1,fruta)#Imprime la lista de frutas, enumerandolas
                time.sleep(5)
                print(f'¡Ordena las frutas tal y cómo apareció en la pantalla! ¡Lo más rápido que puedas!')
                time.sleep(3)
                
                print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows

                tiempo_partida=round(ar.start_sorting(lista_armem,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
                tiempo_total+=tiempo_partida
                print(f'Tiempo de partida: {tiempo_partida}s')

                time.sleep(1)
                print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
                jugador[n+1]+=tiempo_partida
        Resultados.resultados_nivel(lista_jugadores,n)
    Resultados.resultados_final(lista_jugadores)
    time.sleep(5)
    seguir()

def seguir():
    """Esta funcion se encarga de preguntar a los jugadores si desean volver a jugar los mismos o no, o si desean salir del
       programa. En caso de que deseen jugar las mismas personas, se mantendran los nombres pero se reiniciaran los tiempos,
       por otro lado si desean reiniciar sin los mismos nombres, lista_jugadores se borrara y se enviaran al menu inicial 
       para que ingresen de nuevo los nombres que deseen, y en caso de ya no querer jugar mas o salir del programa pueden 
       tambien hacerlo

       Autor:
            Rafael Odio
    """
    cont = 0
    seguir = int(input("Desea volver a jugar? \n Ingrese 1 para jugar con los mismos usuarios \n Ingrese 2 para reiniciar sin los nombres \n Ingrese 3 para salir del programa \n"))
    if seguir == 1:
        for jugador in lista_jugadores:
            del lista_jugadores[cont][1:]
        cont+=1
        juego()
    if seguir == 2:
        lista_jugadores.clear()
        juego()
    if seguir == 3:
        exit()

lista_jugadores=[]
lista_juego=[0,1,2,3,4]
print('\033[2J')
input("""Bienvenidos a ARMem, el juego consiste en memorizar el orden en el que aparecen los nombres de las frutas y luego ordenarlas
lo más rápido posible, ordena los marcadores frente a la cámara para poder observar cada fruta, intenta ser el que logre los tiempos
más bajos entre tus amigos en cada uno de los tres niveles, o si estás solo, desafiate a tí mismo a lograrlo lo más rápido posible :)
    \nPara jugar presiona enter""")
juego()
