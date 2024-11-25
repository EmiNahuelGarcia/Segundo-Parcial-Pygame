import pygame
from configuracion import *
from personajes import *
from funciones_movimientos import *
from menu import *
from plataformas_primer_escenario import *


def dibujar_plataformas(ventana, plataformas):
    """Dibuja las plataformas en la ventana."""
    for plataforma in plataformas:
        pygame.draw.rect(ventana, (0, 255, 0), plataforma)  # Color verde para las plataformas


