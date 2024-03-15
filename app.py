import ARMem as ar
import menu
import Resultados
import time
import random

def juego():
    menu.menu_inicio(lista_jugadores)

    for jugador in lista_jugadores:
        jugador.extend([0,0,0])
    print(lista_jugadores)

    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempo_total=0
    for n in range(0,3):
        for r in range(0,2):
            for jugador in lista_jugadores:
                lista_juego_actual = random.sample(lista_juego,3+n)
                print(f'Memorice la siguiente secuencia...')
                print(lista_juego_actual)
                time.sleep(1)
                print(f'Ordene los marcadores en el orden que se le indicó!')
                time.sleep(1)
                
                print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows

                tiempo_partida=round(ar.start_sorting(lista_juego_actual,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
                tiempo_total+=tiempo_partida
                print(f'Tiempo de partida: {tiempo_partida}s')

                time.sleep(1)
                print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
                jugador[n+1]+=tiempo_partida

        Resultados.resultados_nivel(lista_jugadores,n)
    Resultados.resultados_final(lista_jugadores)

lista_jugadores=[]
lista_juego=[0,1,2,3,4]
juego()
