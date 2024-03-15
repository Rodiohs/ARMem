import time

def resultados_nivel(lista_jugadores:list,n):
    print("Nivel",n+1,"Resultados de la ronda")
    time.sleep(2)
    ordenar_lista_jugadores(lista_jugadores,n)
    for jugador in lista_jugadores:
        print("Tiempo de",jugador[0],":",jugador[n+1])
        time.sleep(1.5)
        
def resultados_final(lista_jugadores:list):
    print("Resultados finales del juego...")
    for jugador in lista_jugadores:
            jugador.append(jugador[1]+jugador[2]+jugador[3])
    time.sleep(2)
    n=4
    ordenar_lista_jugadores(lista_jugadores,n)
    for jugador in lista_jugadores:
        time.sleep(1.5)
        print(jugador[0],":",jugador[4])
    
def ordenar_lista_jugadores(lista_jugadores:list,n):
    contador=0
    while contador<(len(lista_jugadores))-1:
        if lista_jugadores[contador][n]<lista_jugadores[contador+1][n]:
            temporal=lista_jugadores[contador]
            lista_jugadores[contador]=lista_jugadores[contador+1]
            lista_jugadores[contador+1]=temporal
        contador+=1
    contador=0
    while contador<(len(lista_jugadores))-1:
        if lista_jugadores[contador][n]<lista_jugadores[contador+1][n]:
            ordenar_lista_jugadores(lista_jugadores,n)
        contador+=1
