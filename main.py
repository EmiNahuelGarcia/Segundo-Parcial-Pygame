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
    '''
    Función principal del juego.

    Configura la ventana principal del juego, inicializa los recursos necesarios 
    y gestiona el bucle principal mediante un while true para cambiar entre diferentes escenas del juego, 
    como el menú, los escenarios, y otras secciones como opciones, créditos y ranking

    no retorna nada
    '''

    ventana = pygame.display.set_mode((ANCHO, ALTO)) #creacion de la ventana



    RELOJ = pygame.time.Clock()

    FPS = 60


    pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

    escena_actual = "menu" #controlar el flujo para entrar al menu
    jugando = True
    while jugando: #bucle principal del juego
        
        RELOJ.tick(FPS) # control de los fpsclea 
        
        
        if escena_actual == "menu":
            escena_actual = menu(ventana, monedas) #ejecuta el menu

        elif escena_actual == "primer_escenario":
            escena_actual = primer_escenario(ventana, protagonista, sprites, rect_personaje) #ejecuta el primer escenario

        elif escena_actual == "segundo_escenario":
            escena_actual = segundo_escenario(ventana,protagonista, sprites, rect_personaje, plataformas) #ejecuta el segundo escenario
        
        elif escena_actual == "opciones":
            escena_actual = opciones(ventana) #ejecuta opciones
            print("opciones")
        
        elif escena_actual == "creditos":
            escena_actual = creditos(ventana) #ejecuta creditos
        
        elif escena_actual == "ranking":
            escena_actual = ranking(ventana) #ejecuta rankings

        elif escena_actual == "salir":
            jugando = False #finaliza el bucle
            
            

        
        for evento in pygame.event.get(): #captura los eventos del juego
            
            if evento.type == pygame.QUIT: #captura si se cierra el juego
                jugando = False #finaliza el bucle
            
                            

        pygame.display.update() #updatea la pantalla dentro del bucle para notar cambios

    pygame.quit()

if __name__ == "__main__":
    main()