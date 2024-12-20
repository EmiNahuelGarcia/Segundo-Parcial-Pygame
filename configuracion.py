import pygame

ANCHO = 1000

ALTO = 800

FONT_PATH = "assets/fuentes/REDEMPTION.TTF"

CREDITOS_PATH = "assets/images/meme_profe.jpg"
FONDO_RANKING = pygame.image.load("assets/images/menu_ranking.jpg")

FUENTE = pygame.font.Font("assets/fuentes/REDEMPTION.TTF", 50)

NOMBRE_JUEGO = "Developers Game DIV 115"

ICONO = pygame.image.load("assets/images/logo_juego.png")

pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

FONDO_UNO = pygame.image.load("assets/images/fondo_primer_escenario.jpg") #fondos
FONDO_UNO = pygame.transform.scale(FONDO_UNO, (ANCHO, ALTO))

FONDO_DOS = pygame.transform.scale(pygame.image.load("assets/images/fondo_segundo_escenario.jpg"), (ANCHO, ALTO))

FONDO_GAME_OVER = pygame.transform.scale(pygame.image.load("assets/images/fondo_game_over.jpg"), (ANCHO, ALTO))

FONDO_VICTORIA = pygame.transform.scale(pygame.image.load("assets/images/fondo_victoria_primer_escenario.jpg"), (ANCHO, ALTO))


darth_vader = pygame.image.load("assets/images/darth_vader.png") #easter egg
darth_vader = pygame.transform.scale(darth_vader, (200, 200))




pygame.display.set_icon(ICONO) #icono del juego

ROJO = (255, 0, 0) #colores varios
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VIOLETA = (128, 0, 255)
BLANCO = (255, 255, 255)

OPCIONES = ["Jugar", "Opciones", "Creditos", "Ranking", "Salir"] #opciones del menu


OFFSET_VERTICAL = ALTO // 4  # Ajustar según el tamaño de la pantalla
ESPACIADO_VERTICAL = 130  # Modificar según lo que luzca mejor

FONDO_MENU = pygame.transform.scale(pygame.image.load("assets/images/menu_fondo.jpg"), (ANCHO, ALTO))  # imagen del fondo de menu

ancho_fuego = 50
alto_fuego = 50
fuego = pygame.transform.scale(pygame.image.load("assets/images/fuego_segundo_escenario.png"),(ancho_fuego, alto_fuego))

SONIDO_DISPARO_PROTA = pygame.mixer.Sound('assets/audios/sonido_disparo.wav') # carga de sonidos

SONIDO_DISPARO_ENEMIGO = pygame.mixer.Sound('assets/audios/sonido_disparo_enemigo.wav')

SONIDO_BOLA = pygame.mixer.Sound('assets/audios/sonido_bola.mp3')

SONIDO_VICTORIA = pygame.mixer.Sound('assets/audios/sonido_victoria.wav')

SONIDO_DERROTA = pygame.mixer.Sound('assets/audios/sonido_derrota.wav')


pygame.mixer.music.load('assets/audios/sonido_fondo.wav') #bucle de musica del juego