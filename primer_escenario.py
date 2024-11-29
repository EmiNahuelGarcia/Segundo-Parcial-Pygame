import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *
from funciones_disparar import *
from funciones_monedas import *
from funciones_reiniciar_juego import *


def primer_escenario(ventana, protagonista, sprites, rect_personaje):
    reloj = pygame.time.Clock()
    jugando = True
    mirando_izquierda = False
    mirando_derecha = True 
    plataformas = inicializar_plataformas()
    

    while jugando:
        if protagonista["vida"] == 0:
            game_over(ventana, FONDO_GAME_OVER)
            reiniciar_juego()
            reiniciar_vida(protagonista)
            return "menu"

        ventana.blit(FONDO_UNO, (0, 0))  # Fondo del escenario
        tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
        

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
        
        #Dibujar los enemigos
        dibujar_enemigos(ventana, enemigos, rects_enemigos, sprites_enemigos)
        # Dibujar las monedas
        dibujar_monedas(ventana, monedas, sprite_moneda) 
        
        disparar(rect_personaje, proyectiles, teclas, protagonista, tiempo_actual)
        # Dibujar los proyectiles
        dibujar_proyectiles(ventana, proyectiles)
        # Mover los proyectiles
        mover_proyectiles(proyectiles)
        
        # Actualizar cada enemigo
        for enemigo in enemigos.values():  # Iterar sobre todos los enemigos
            disparar_enemigo(enemigo, proyectiles_enemigos, rect_personaje, tiempo_actual)

        # Verificar colisiones con el protagonista
        verificar_colisiones_proyectiles(proyectiles, rect_personaje, enemigos, rects_enemigos, protagonista)

        verificar_colision_monedas(rect_personaje, monedas, protagonista)
        if comprobar_victoria(monedas):
            victoria_primer_escenario(ventana, FONDO_VICTORIA_PRIMER_ESCENARIO)
            plataformas.clear()
            reiniciar_prota(protagonista)
            return "segundo_escenario"

        verificar_puntaje(protagonista)
        verificar_vida(protagonista)

        
        

        # Mover proyectiles enemigos
        mover_proyectiles_enemigos(proyectiles_enemigos)

        # Dibujar los proyectiles enemigos en la pantalla
        dibujar_proyectiles_enemigos(ventana, proyectiles_enemigos)
        
        #dibujar los rects para revisar errores
        '''for proyectil in proyectiles:
            pygame.draw.rect(ventana, (ROJO), proyectil["rect"], 2)  # Color rojo

        # Dibujar los enemigos
        for enemigo_key, enemigo_data in enemigos.items():
            pygame.draw.rect(ventana, (0, 255, 0), rects_enemigos[enemigo_key], 2)  # Color verde
            # Dibujar el protagonista
            pygame.draw.rect(ventana, (0, 0, 255), rect_personaje, 2)  # Color azul
 '''

        ventana.blit(sprite_personaje, rect_personaje)
        dibujar_stats(ventana, protagonista)
        pygame.display.flip()
        reloj.tick(60)

