import pygame


ANCHO = 800

ALTO = 600

FUENTE = pygame.font.Font(None, 50)


NOMBRE_JUEGO = "Developers Game DIV 115"

ICONO = pygame.image.load("assets/images/logo_juego.png")

pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

FONDO_UNO = pygame.image.load("assets/images/fondo_primer_escenario.jpg")

FONDO_UNO= pygame.transform.scale(FONDO_UNO, (ANCHO, ALTO))

FONDO_GAME_OVER = pygame.transform.scale(pygame.image.load("assets/images/fondo_game_over.png"), (ANCHO, ALTO))

FONDO_VICTORIA_PRIMER_ESCENARIO = pygame.transform.scale(pygame.image.load("assets/images/fondo_victoria_primer_escenario.jpg"), (ANCHO, ALTO))


darth_vader = pygame.image.load("assets/images/darth_vader.png")
darth_vader = pygame.transform.scale(darth_vader, (200, 200))
rect_darth_vader = darth_vader.get_rect()
rect_darth_vader.topleft = (100, 600)

mickey = pygame.image.load("assets/images/mickey.png")
mickey = pygame.transform.scale(mickey, (150, 150))

pygame.display.set_icon(ICONO)

ROJO = (255, 0, 0)

AZUL = (0, 0, 255)

VERDE = (0, 255, 0)

NEGRO = (0, 0, 0)

BLANCO = (255, 255, 255)

