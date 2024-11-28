import pygame

ANCHO = 1000

ALTO = 800

FUENTE = pygame.font.Font(None, 50)

NOMBRE_JUEGO = "Developers Game DIV 115"

ICONO = pygame.image.load("assets/images/logo_juego.png")

pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

FONDO_UNO = pygame.image.load("assets/images/fondo_primer_escenario.jpg")
FONDO_UNO = pygame.transform.scale(FONDO_UNO, (ANCHO, ALTO))

FONDO_DOS = pygame.transform.scale(pygame.image.load("assets/images/fondo_segundo_escenario.jpg"), (ANCHO, ALTO))

FONDO_GAME_OVER = pygame.transform.scale(pygame.image.load("assets/images/fondo_game_over.png"), (ANCHO, ALTO))

FONDO_VICTORIA_PRIMER_ESCENARIO = pygame.transform.scale(pygame.image.load("assets/images/fondo_victoria_primer_escenario.jpg"), (ANCHO, ALTO))


darth_vader = pygame.image.load("assets/images/darth_vader.png")
darth_vader = pygame.transform.scale(darth_vader, (200, 200))


'''mickey = pygame.image.load("assets/images/mickey.png")
mickey = pygame.transform.scale(mickey, (150, 150))'''

pygame.display.set_icon(ICONO)

ROJO = (255, 0, 0)

AZUL = (0, 0, 255)

VERDE = (0, 255, 0)

NEGRO = (0, 0, 0)

BLANCO = (255, 255, 255)

VIOLETA = (128, 0, 255)
BLANCO = (255, 255, 255)
OPCIONES = ["Jugar", "Opciones", "Créditos", "Ranking", "Salir"]


OFFSET_VERTICAL = ALTO // 4  # Ajustar según el tamaño de la pantalla
ESPACIADO_VERTICAL = 140  # Modificar según lo que luzca mejor

FONDO_MENU = pygame.transform.scale(pygame.image.load("assets/images/menu_fondo.jpg"), (ANCHO, ALTO))  