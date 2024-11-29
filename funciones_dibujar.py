import pygame
from configuracion import *

def dibujar_plataformas(ventana, plataformas, sprite_plataforma):
    """Dibuja las plataformas con el sprite en la ventana."""
    for plataforma in plataformas:
        ventana.blit(sprite_plataforma, plataforma)



    

def dibujar_enemigos(ventana, enemigos, rects_enemigos, sprites_enemigos):
    for enemigo_id, enemigo_data in enemigos.items():
        sprite = sprites_enemigos[enemigo_data["sprite"]]
        
        # Si el enemigo está mirando a la izquierda, no hace falta hacer nada
        if enemigo_data["direccion"] == "izquierda":
            ventana.blit(sprite, rects_enemigos[enemigo_id])
        else:  # Si el enemigo está mirando a la derecha, se voltea el sprite
            sprite_volteado = pygame.transform.flip(sprite, True, False)
            ventana.blit(sprite_volteado, rects_enemigos[enemigo_id])


def dibujar_monedas(ventana, monedas, sprite_moneda):
    for moneda in monedas:
        if not moneda["recogida"]:
            ventana.blit(sprite_moneda, moneda["rect"])


def dibujar_stats(ventana, protagonista):
    """Dibuja la vida y el ranking del protagonista en la esquina superior izquierda."""
    # Texto para la vida
    fuente = pygame.font.Font(FONT_PATH, 36)
    texto_vida = fuente.render(f"{protagonista['vida']}", True, BLANCO)
    ventana.blit(texto_vida, (120, 40))  # Dibujar en la posición (10, 10)

    # Texto para el ranking/puntuación
    texto_puntuacion = fuente.render(f"{protagonista['puntuacion']}", True, BLANCO)
    ventana.blit(texto_puntuacion, (320, 40))  # Dibujar en la posición (10, 50)