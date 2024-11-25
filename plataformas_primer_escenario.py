import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from primer_escenario import *
from personajes import *
from funciones_dibujar import *

# Definimos las plataformas como rectángulos
plataformas = [
    pygame.Rect(200, 400, 100, 20), 
    pygame.Rect(350, 300, 100, 20),  
    pygame.Rect(500, 500, 100, 20), 
    pygame.Rect(200, 600, 100, 20),
    pygame.Rect(800, 200, 100, 20),
    pygame.Rect(550, 200, 100, 20)
]

sprite_plataforma = pygame.transform.scale(pygame.image.load("assets/images/plataforma.png"), (150, 30))