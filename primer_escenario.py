import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *
from funciones_disparar import *

def primer_escenario(ventana,protagonista, sprites, rect_personaje):
    reloj = pygame.time.Clock()
    jugando = True
    mirando_izquierda = False
    mirando_derecha = True 

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
        #mover_personaje(protagonista, rect_personaje, teclas, sprites)
        aplicar_gravedad(protagonista, rect_personaje, plataformas)
        dibujar_plataformas(ventana, plataformas, sprite_plataforma)

        mover_personaje(protagonista, rect_personaje, teclas, sprites)
        '''ventana.blit(sprites[protagonista["sprite actual"]], rect_personaje)  # Dibujar el sprite actual'''
        # Obtener el sprite actual
        sprite_personaje = sprites[protagonista["sprite actual"]]

        # Si el personaje se mueve a la izquierda
        if teclas[pygame.K_LEFT]:
            sprite_personaje = pygame.transform.flip(sprite_personaje, True, False)
            if not mirando_izquierda:
                # Voltea el sprite inactivo también
                sprites["inactivo"] = pygame.transform.flip(sprites["inactivo"], True, False)
                mirando_izquierda = True
                mirando_derecha = False

        # Si el personaje se mueve a la derecha
        if teclas[pygame.K_RIGHT]: 
            if not mirando_derecha:
                # Voltea el sprite inactivo también
                sprites["inactivo"] = pygame.transform.flip(sprites["inactivo"], True, False)
                mirando_izquierda = False
                mirando_derecha = True
        
        
        dibujar_enemigos(ventana, enemigos, rects_enemigos, sprites_enemigos)

        # Disparar al presionar la tecla espacio
        
        disparar(rect_personaje, proyectiles, mirando_derecha, teclas)
        # Dibujar los proyectiles
        dibujar_proyectiles(ventana, proyectiles)
        # Mover los proyectiles
        mover_proyectiles(proyectiles)
        # Dibujar el sprite en la pantalla
        ventana.blit(sprite_personaje, rect_personaje)
        pygame.display.flip()
        reloj.tick(60)