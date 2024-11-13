import pygame


ANCHO = 1000

ALTO = 800

NOMBRE_JUEGO = "Developers Game DIV 115"

ICONO = pygame.image.load("assets/images/logo_juego.png")

FONDO = pygame.image.load("assets/images/fondo_juego.jpg")
FONDO = pygame.transform.scale(FONDO, (1000, 800))

darth_vader = pygame.image.load("assets/images/darth_vader.png")
darth_vader = pygame.transform.scale(darth_vader, (200, 200))

mickey = pygame.image.load("assets/images/mickey.png")
mickey = pygame.transform.scale(mickey, (150, 150))

pygame.display.set_icon(ICONO)

ROJO = (255, 0, 0)

AZUL = AZUL = (0, 0, 255)

FUENTE = pygame.font.Font(None, 36)

