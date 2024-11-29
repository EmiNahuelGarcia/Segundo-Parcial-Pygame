import pygame
import sys
import json
from configuracion import *


def imprimir_ranking(ventana):
    try:
        # Intentamos abrir el archivo
        with open("leaderboard.json", "r") as archivo:
            ranking = json.load(archivo)
    except FileNotFoundError:
        # Si no existe, lo creamos vacío
        ranking = []
        with open("leaderboard.json", "w") as archivo:
            json.dump(ranking, archivo, indent=4)
    except json.JSONDecodeError:
        # Si está dañado, lo inicializamos vacío
        ranking = []
        with open("leaderboard.json", "w") as archivo:
            json.dump(ranking, archivo, indent=4)

    # Configuración de fuente
    fuente = pygame.font.Font(FONT_PATH, 40)

    # Dibujamos los 5 mejores jugadores
    for i, jugador in enumerate(ranking[:5]):  # Top 5
        nombre = jugador.get("nombre", "Anónimo")
        puntos = jugador.get("puntos", 0)
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