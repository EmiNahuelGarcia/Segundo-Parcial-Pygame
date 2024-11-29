import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from personajes import *
from personajes import mickey_mouse
from plataformas_primer_escenario import *
from funciones_dibujar import *
from funciones_disparar import *
from funciones_monedas import *
from funciones_reiniciar_juego import *
from plataformas_segundo_escenario import *

def victoria_segundo_escenario():
    return True if mickey_mouse["vida"] <= 0 and protagonista["vida"] > 0 else False

def segundo_escenario(ventana, protagonista, sprites, rect_personaje, plataformas):
    reloj = pygame.time.Clock()
    jugando = True
    mirando_izquierda = False
    mirando_derecha = True 
    fuegos_activos = [generar_fuego() for _ in range(5)]

    while jugando:
        if protagonista["vida"] == 0:
            game_over(ventana, FONDO_GAME_OVER)
            reiniciar_juego()
            reiniciar_vida(protagonista)
            return "menu"
        
        ventana.blit(FONDO_DOS, (0, 0))  # Fondo del segundo escenario
        tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos

        teclas = pygame.key.get_pressed()

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si se cierra la ventana
                return "salir"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Si presiona ESC, regresa al menú
                    return "menu"

        mover_personaje(protagonista, rect_personaje, teclas, sprites)
        
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

        # Lógica de movimiento y otras acciones
        dibujar_jefe(ventana, mickey_mouse, sprites_mickey_mouse, rect_mickey_mouse, pygame.time.get_ticks())
        aplicar_gravedad(protagonista, rect_personaje, plataformas_segundo_escenario)
        dibujar_plataformas(ventana, plataformas_segundo_escenario , sprite_plataforma)  # Asegúrate de que las plataformas estén correctas
        
        disparar(rect_personaje, proyectiles, teclas, protagonista, tiempo_actual)
        # Dibujar los proyectiles
        dibujar_proyectiles(ventana, proyectiles)
        # Mover los proyectiles
        mover_proyectiles(proyectiles)

        manejar_fuegos(fuegos_activos, ventana, protagonista, rect_personaje)


        ventana.blit(sprite_personaje, rect_personaje)  # Asegúrate de que el sprite correcto se dibuje
        dibujar_stats(ventana, protagonista)
        pygame.display.flip()
        reloj.tick(60)