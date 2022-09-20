import curses #importa la biblioteca curses
import random #importa la biblioteca random
import time
from turtle import color   #importa la biblioteca time, para poder utilizar slep

alto=35
ancho=150
pantalla = curses.initscr() #inicializa curses para utilizar la terminal de CMD

#============================
#===inicializacion de curses=====
#============================
curses.noecho()
curses.cbreak()
curses.curs_set(0)
pantalla.keypad(True)
pantalla.nodelay(True)

#============================
#===inicializacion de snake=====
#===y de la fruta=====
#============================

x=0
y=0
snake=[[y,x]]
fruta=[random.randrange(alto),random.randrange(ancho)]
pantalla.addstr(fruta[0],fruta[1],"o")
mov_horizontal = 1
mov_vertical = 0
punto_jugador = 0

#============================
#===comienzo del juego=====
#============================

while True:    
    #leemos la tecla
    tecla = pantalla.getch()        
    #le asignamos una dirección a cada cursor
    if tecla==curses.KEY_LEFT:
        mov_horizontal = -1
        mov_vertical = 0
    elif tecla==curses.KEY_RIGHT:
        mov_horizontal = 1
        mov_vertical = 0
    elif tecla==curses.KEY_UP:
        mov_horizontal = 0
        mov_vertical = -1
    elif tecla==curses.KEY_DOWN:
        mov_horizontal = 0
        mov_vertical = 1
    elif tecla==10:
        break
    
    x = (x + mov_horizontal) % ancho
    y = (y + mov_vertical) % alto

    #hacemos que no se salga de la pantalla

    if ancho == ancho:
        x = (x - mov_horizontal) % ancho
        break
    if alto == alto:
        y = (y - mov_vertical) % alto
        break

    posicion=[y,x]

    #si nos comemos una parte de snake, el juego se enoja y se sale    
    if posicion in snake:
        break

    snake.insert(0,posicion)    
    #ponemos una pausa, probá que sucede si la comentás
    time.sleep(0.1)

    #verificamos si nos morfamos una fruta
    if fruta in snake:        
        fruta=[random.randrange(alto),random.randrange(ancho)]
        pantalla.addstr(fruta[0],fruta[1],"o")
        punto_jugador += punto_jugador
        print ("Puntos: " + punto_jugador)
    #sino, borramos la colita
    else:
        ultimaposicion = snake.pop()
        pantalla.addstr(ultimaposicion[0],ultimaposicion[1]," ")

    #dibujamos la cabeza
    pantalla.addstr(snake[0][0],snake[0][1],"#")

    #pantalla.addstr(y,x, "#")   
    
#Ponemos todo en su lugar    
curses.nocbreak()
pantalla.keypad(False)
curses.echo()
curses.endwin()