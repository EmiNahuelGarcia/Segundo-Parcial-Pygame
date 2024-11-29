import pygame
pygame.init()
pygame.mixer.init()
import random
from configuracion import *
from funciones_movimientos import *
from menu import *
from primer_escenario import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *
from funciones_monedas import *
from segundo_escenario import *
from ranking import *
from boss_final import *
from opciones import *
from ranking import *

pygame.mixer.music.play(-1)
def main():

    ventana = pygame.display.set_mode((ANCHO, ALTO)) #creacion de la ventana



    RELOJ = pygame.time.Clock()

    FPS = 60


    pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

    escena_actual = "menu" #controlar el flujo para entrar al menu
    jugando = True
    while jugando: #bucle principal del juego
        
        RELOJ.tick(FPS) # control de los fpsclea 
        
        
        if escena_actual == "menu":
            escena_actual = menu(ventana, monedas)

        elif escena_actual == "primer_escenario":
            escena_actual = primer_escenario(ventana, protagonista, sprites, rect_personaje)

        elif escena_actual == "segundo_escenario":
            escena_actual = segundo_escenario(ventana,protagonista, sprites, rect_personaje, plataformas)
        
        elif escena_actual == "opciones":
            escena_actual = opciones(ventana)
            print("opciones")
        
        elif escena_actual == "creditos":
            escena_actual = creditos(ventana)
        
        elif escena_actual == "ranking":
            escena_actual = ranking(ventana)

        elif escena_actual == "salir":
            jugando = False
            
            

        
        for evento in pygame.event.get(): #captura los eventos del juego
            
            if evento.type == pygame.QUIT: #captura si se cierra el juego
                jugando = False
            
                            

        pygame.display.update() #updatea la pantalla dentro del bucle para notar cambios

    pygame.quit()

if __name__ == "__main__":
    main()