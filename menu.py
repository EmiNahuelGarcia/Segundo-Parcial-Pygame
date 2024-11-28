import pygame
import sys
from primer_escenario import primer_escenario

ALTO = 600
ANCHO = 800
VIOLETA = (128, 0, 255)
BLANCO = (255, 255, 255)
OPCIONES = ["Jugar", "Opciones", "Créditos", "Ranking", "Salir"]
PATH_ICONO = "logo_developers.png"
PATH_FONDO = "menu_fondo.jpg"
TITLE = "Juego - Developers"
OFFSET_VERTICAL = 150
ESPACIADO_VERTICAL = 100

def crear_ventana():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    icono = pygame.image.load(PATH_ICONO)
    fondo = pygame.image.load(PATH_FONDO)
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(icono)
    ventana.blit(fondo, (0, 0))
    return ventana

def dibujar_menu(seleccion, ventana):
    fuente = pygame.font.Font(None, 45)
    for i, opcion in enumerate(OPCIONES):
        etiqueta = fuente.render(opcion, True, VIOLETA if i == seleccion else BLANCO)
        ventana.blit(etiqueta, (ANCHO // 2 - etiqueta.get_width() // 2, OFFSET_VERTICAL + i * ESPACIADO_VERTICAL))
    pygame.display.flip()

def handler_seleccion(seleccion, ventana):
    if seleccion == 0:
        primer_escenario(ventana)
        print("Jugar")
    elif seleccion == 1:
        print("Opciones seleccionado")
    elif seleccion == 2:
        print("Créditos seleccionado")
    elif seleccion == 3:
        print("Ranking seleccionado")
    elif seleccion == 4:
        return False
    return True

def handler_menu_eventos(ventana):
    seleccion = 0
    ejecutando = True
    while ejecutando:
        dibujar_menu(seleccion, ventana)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(OPCIONES)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(OPCIONES)
                if evento.key == pygame.K_RETURN:
                    ejecutando = handler_seleccion(seleccion, ventana)

def menu():
    ventana = crear_ventana()
    handler_menu_eventos(ventana)
    pygame.quit()

menu()