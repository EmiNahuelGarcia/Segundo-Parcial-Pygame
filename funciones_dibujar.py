import pygame
from configuracion import *

def dibujar_plataformas(ventana: pygame.surface, plataformas: list, sprite_plataforma: pygame.surface) -> None:
    """Dibuja las plataformas en la ventana usando un sprite.

    Esta función recorre la lista de plataformas y dibuja el sprite proporcionado
    en las posiciones correspondientes.

    Parámetros:
        ventana (pygame.Surface): La superficie donde se dibujarán las plataformas.
        plataformas (list): Una lista de rectángulos de las plataformas a dibujar.
        sprite_plataforma (pygame.Surface): El sprite de la plataforma que se dibujará.

    No retorna ningún valor.
    
    """
    for plataforma in plataformas:
        ventana.blit(sprite_plataforma, plataforma)



    

def dibujar_enemigos(ventana: pygame.surface, enemigos: dict, rects_enemigos: dict, sprites_enemigos: dict) -> None:
    '''
    Dibuja los enemigos en la ventana, volteando sus sprites si es necesario.

    Esta función recorre el diccionario de enemigos y dibuja sus sprites en la 
    ventana. Si un enemigo está mirando a la derecha, el sprite se voltea antes
    de dibujarlo.

    Parámetros:
        ventana (pygame.Surface): La superficie donde se dibujarán los enemigos.
        enemigos (dict): Un diccionario de enemigos con sus características.
        rects_enemigos (dict): Un diccionario con los rectángulos que representan
        las posiciones de los enemigos.
        sprites_enemigos (dict): Un diccionario con los sprites de los enemigos.

    No retorna ningún valor.
    '''

    for enemigo_id, enemigo_data in enemigos.items():
        sprite = sprites_enemigos[enemigo_data["sprite"]]
        
        # Si el enemigo está mirando a la izquierda, no hace falta hacer nada
        if enemigo_data["direccion"] == "izquierda":
            ventana.blit(sprite, rects_enemigos[enemigo_id])
        else:  # Si el enemigo está mirando a la derecha, se voltea el sprite
            sprite_volteado = pygame.transform.flip(sprite, True, False)
            ventana.blit(sprite_volteado, rects_enemigos[enemigo_id])


def dibujar_monedas(ventana: pygame.surface, monedas: list, sprite_moneda: pygame.surface) -> None:
    '''
    Dibuja las monedas no recogidas en la ventana.

    Esta función recorre la lista de monedas y dibuja el sprite de la moneda
    en la posición correspondiente solo si la moneda no ha sido recogida.

    Parámetros:
        ventana (pygame.Surface): La superficie donde se dibujarán las monedas.
        monedas (list): Una lista de diccionarios con las monedas en el juego.
        sprite_moneda (pygame.Surface): El sprite de la moneda que se dibujará.

    No retorna ningún valor.
    
    '''
    for moneda in monedas:
        if not moneda["recogida"]:
            ventana.blit(sprite_moneda, moneda["rect"])


def dibujar_stats(ventana: pygame.surface, protagonista: dict) -> None:
    """
    Dibuja la vida y la puntuación del protagonista en la esquina superior izquierda.

    Esta función muestra la vida y la puntuación del protagonista en la ventana,
    dibujando el texto en la parte superior izquierda de la pantalla.

    Parámetros:
        ventana (pygame.Surface): La superficie donde se dibujarán las estadísticas.
        protagonista (dict): El diccionario que contiene los datos del protagonista, 
        como su vida y puntuación.

    No retorna ningún valor."""
    # Texto para la vida
    fuente = pygame.font.Font(FONT_PATH, 36)
    texto_vida = fuente.render(f"{protagonista['vida']}", True, BLANCO)
    ventana.blit(texto_vida, (120, 40))  # Dibujar en la posición (10, 10)

    # Texto para el ranking/puntuación
    texto_puntuacion = fuente.render(f"{protagonista['puntuacion']}", True, BLANCO)
    ventana.blit(texto_puntuacion, (320, 40))  # Dibujar en la posición (10, 50)