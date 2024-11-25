import pygame
from configuracion import *
from personajes import *
from funciones_movimientos import *
from menu import *

def primer_escenario(ventana,protagonista, sprites):
    reloj = pygame.time.Clock()
    jugando = True
    

    while jugando:

        ventana.blit(FONDO_UNO, (0, 0))  # Fondo del escenario
        

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #sale del juego
                return "salir"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Si presiona ESC, regresa al menú
                    return "menu"
                

        
        
        
        teclas = pygame.key.get_pressed()
        mover_personaje(protagonista, rect_personaje, teclas)
        aplicar_gravedad(protagonista, rect_personaje)

        ventana.blit(sprites[protagonista["sprite actual"]], rect_personaje)  # Dibujar el sprite actual

        pygame.display.flip()
        reloj.tick(60)