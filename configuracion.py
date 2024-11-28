import pygame


ANCHO = 800

ALTO = 600

#FUENTE = pygame.font.Font(None, 36)

NOMBRE_JUEGO = "Developers Game DIV 115"

ICONO = pygame.image.load("assets/images/logo_juego.png")

pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

FONDO_UNO = pygame.image.load("assets/images/fondo_primer_escenario.jpg")
FONDO_UNO= pygame.transform.scale(FONDO_UNO, (800, 600))


darth_vader = pygame.image.load("assets/images/darth_vader.png")
darth_vader = pygame.transform.scale(darth_vader, (200, 200))
rect_darth_vader = darth_vader.get_rect()
rect_darth_vader.topleft = (100, 600)

mickey = pygame.image.load("assets/images/mickey.png")
mickey = pygame.transform.scale(mickey, (150, 150))

pygame.display.set_icon(ICONO)

ROJO = (255, 0, 0)

AZUL = AZUL = (0, 0, 255)

NEGRO = (0, 0, 0)

BLANCO = (0, 0, 0)

