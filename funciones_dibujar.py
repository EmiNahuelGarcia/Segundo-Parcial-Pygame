import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from primer_escenario import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *


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