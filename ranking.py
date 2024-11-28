import pygame
import sys
import json
from configuracion import *

def imprimir_ranking(ventana):
    with open("leaderboard.json", "r") as archivo:
        ranking = json.load(archivo)["leaderboard"]

    fuente = pygame.font.Font(FONT_PATH, 40)
    for i, jugador in enumerate(ranking[-5:]):
        if(i < 5):
            nombre = jugador["nombre"]
            puntos = jugador["puntos"]
            texto = fuente.render(f"{i + 1}. {nombre} - {puntos}", True, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 225 + i * 110))

def ranking(ventana):
    while True:
        ventana.blit(FONDO_RANKING, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return "menu"

        imprimir_ranking(ventana)
        pygame.display.flip()
