import pygame
pygame.init()
import random
from configuracion import *
from funciones_movimientos import *
from menu import *
from primer_escenario import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *
from funciones_monedas import *

ventana = pygame.display.set_mode((ANCHO, ALTO)) #creacion de la ventana



RELOJ = pygame.time.Clock()

FPS = 60


pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana


escena_actual = "menu" #controlar el flujo para entrar al menu
jugando = True
while jugando: #bucle principal del juego
    
    RELOJ.tick(FPS) # control de los fps
    
    
    if escena_actual == "menu":
        escena_actual = menu(ventana)

    elif escena_actual == "primer_escenario":
        escena_actual = primer_escenario(ventana, protagonista, sprites, rect_personaje)

    elif escena_actual == "segundo_escenario": #PLACEHOLDER DE SEGUNDO ESCENARIO
        pass
    
    elif escena_actual == "salir":
        jugando = False
        
        

    
    for evento in pygame.event.get(): #captura los eventos del juego
        
        if evento.type == pygame.QUIT: #captura si se cierra el juego
            jugando = False
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:   # Mover a la izquierda
            en_escenario = False
                        

    pygame.display.update() #updatea la pantalla dentro del bucle para notar cambios

pygame.quit()