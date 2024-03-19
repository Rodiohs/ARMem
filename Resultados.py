import time

def resultados_nivel(lista_jugadores:list,n):
    """resultados_nivel muestra los resultados de cada nivel, al mostrar los tiempos que cada jugador duró y el orden
    en el que van quedando en el juego.

    Args:
        lista_jugadores (list): la lista de los jugadores, que incluye sus respectivos tiempos.
        n (_type_): para saber el nivel que se está jugando, al iniciar en cero está un número atrás del nivel.
    
    Autor:
        Jairo González
    """
    print(f"\033[1;33;40m Resultados del nivel {n+1}\033[0m ...")
    time.sleep(2)
    ordenar_lista_jugadores(lista_jugadores,n+1)
    lista_jugadores.reverse()
    for jugador in lista_jugadores:
        time.sleep(1.5)
        print(jugador[0],":",jugador[n+1])
    lista_jugadores.reverse()
    print(f"Y así es como \033[1;33;40m{lista_jugadores[0][0]}\033[0m llevó la ventaja en este nivel.")
        
def resultados_final(lista_jugadores:list):
    """resultados_final muestra los resultados al terminar el juego, al mostrar los tiempos que cada jugador duró y el orden
    definitivo en el que acaba el juego.

    Args:
        lista_jugadores (list): la lista de los jugadores, que incluye sus respectivos tiempos.

    Autor:
        Jairo González
    """
    print(f"\033[1;33;40m Resultados finales del juego...\033[0m")
    for jugador in lista_jugadores:
            jugador.append(jugador[1]+jugador[2]+jugador[3])
    time.sleep(2)
    n=4
    ordenar_lista_jugadores(lista_jugadores,n)
    lista_jugadores.reverse()
    for jugador in lista_jugadores:
        time.sleep(1.5)
        print(jugador[0],":",jugador[4])
    lista_jugadores.reverse()
    print(f"Y así es como \033[1;33;40m{lista_jugadores[0][0]}\033[0m se corona como el ganador de esta partida.")
    
def ordenar_lista_jugadores(lista_jugadores:list,n):
    """ordenar_lista_jugadores ordenará los jugadores de peores tiempos a mejores tiempos en cada "n" nivel.

    Args:
        lista_jugadores (list): la lista de los jugadores, que incluye sus respectivos tiempos.
        n (_type_): el nivel en que se está jugando, para saber cual posición de las sublistas en lista_jugadores
        tomar en cuenta para ver los tiempos. Según los niveles n va de 1 a 3. Si n es 4 entonces es porque el juego
        ha acabado y se va a calcular el resultado final.
    """
    contador=0
    while contador<(len(lista_jugadores))-1:
        if lista_jugadores[contador][n]>lista_jugadores[contador+1][n]:
            temporal=lista_jugadores[contador]
            lista_jugadores[contador]=lista_jugadores[contador+1]
            lista_jugadores[contador+1]=temporal
        contador+=1
    contador=0
    while contador<(len(lista_jugadores))-1:
        if lista_jugadores[contador][n]>lista_jugadores[contador+1][n]:
            ordenar_lista_jugadores(lista_jugadores,n)
        contador+=1