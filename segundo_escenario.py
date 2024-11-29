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
from plataformas_segundo_escenario import *
from boss_final import *




def segundo_escenario(ventana: pygame.Surface, protagonista: dict, sprites: list, rect_personaje: pygame.Rect, plataformas: list) -> str:
    """
    Lógica y renderizado del segundo escenario del juego.

    Esta función gestiona el segundo nivel del juego, incluyendo el movimiento del protagonista, 
    las interacciones con plataformas, enemigos, proyectiles y la lógica de victoria o derrota. 
    También administra los eventos clave, como el retorno al menú o la salida del juego.
    El escenario termina si la vida del protagonista o del jefe llega a 0

    Returns:
    str: Devuelve el nombre de la siguiente escena a ejecutar:
    - "menu" si el jugador regresa al menú o completa el escenario.
    - "salir" si el jugador cierra el juego. 
    
    """

    reloj = pygame.time.Clock()
    jugando = True
    mirando_izquierda = False
    mirando_derecha = True 
    fuegos_activos = [generar_fuego() for _ in range(5)]

    while jugando:
        if protagonista["vida"] == 0:
            pygame.mixer.music.stop()
            SONIDO_DERROTA.play()
            game_over(ventana, FONDO_GAME_OVER)
            reiniciar_juego()
            reiniciar_vida(protagonista)
            reiniciar_jefe(jefe)
            pygame.mixer.music.play(-1)
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
        
        aplicar_gravedad(protagonista, rect_personaje, plataformas_segundo_escenario)
        dibujar_plataformas(ventana, plataformas_segundo_escenario , sprite_plataforma)  # Asegúrate de que las plataformas estén correctas
        
        disparar(rect_personaje, proyectiles, mirando_derecha, teclas, protagonista, tiempo_actual)
        # Dibujar los proyectiles
        dibujar_proyectiles(ventana, proyectiles)
        # Mover los proyectiles
        mover_proyectiles(proyectiles)

        manejar_fuegos(fuegos_activos, ventana, protagonista, rect_personaje)

        

        

        # Dibujar al jefe
        if jefe["estado"] != "muerto":
            dibujar_jefe(ventana, tiempo_actual)
        dibujar_bolas_fuego(ventana)
        mover_bolas_fuego()
        verificar_colisiones_bolas_fuego_con_protagonista(protagonista, proyectiles_jefe, rect_personaje)
        verificar_colisiones_con_jefe(proyectiles, jefe, rect_jefe)
        
        if comprobar_victoria_juego(jefe):
            pygame.mixer.music.stop()
            SONIDO_VICTORIA.play()
            victoria_segundo_escenario(ventana, FONDO_VICTORIA, protagonista)
            plataformas.clear()
            reiniciar_prota(protagonista)
            reiniciar_juego()
            reiniciar_vida(protagonista)
            reiniciar_jefe(jefe)
            pygame.mixer.music.play(-1)
            return "menu"

            


        ventana.blit(sprite_personaje, rect_personaje)  # Asegúrate de que el sprite correcto se dibuje
        dibujar_stats(ventana, protagonista)
        pygame.display.flip()
        reloj.tick(60)