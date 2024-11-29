import pygame
import sys
import json
from configuracion import *


def imprimir_ranking(ventana : pygame.surface):
    """
    Carga y muestra el ranking de los mejores jugadores en la ventana del juego.

    Esta función lee el archivo `leaderboard.json` que contiene los datos del ranking, 
    los procesa y muestra en pantalla los nombres y las puntuaciones de los 5 mejores jugadores.

    Si el archivo no existe o está dañado, se inicializa un ranking vacío y se guarda en el archivo.
    
    no retorna

    """
    try:
        # try para abrir el archivo
        with open("leaderboard.json", "r") as archivo:
            ranking = json.load(archivo)
    except FileNotFoundError:
        # si no existe se inicializa vacio
        ranking = []
        with open("leaderboard.json", "w") as archivo:
            json.dump(ranking, archivo, indent=4)
    except json.JSONDecodeError:
        # si esta dañado tambien se inicializa vacio
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

def ranking(ventana: pygame.surface) -> str:
    """
    Muestra la pantalla del ranking y permite regresar al menú principal.

    Esta función gestiona la lógica de la pantalla del ranking, incluyendo la visualización
    del fondo y el ranking, así como la detección de eventos para regresar al menú.

    Returns:
    str: Devuelve "menu" cuando el jugador presiona la tecla Enter para regresar al menú principal.
    
    """
    while True:
        ventana.blit(FONDO_RANKING, (0, 0)) #imprime el fondo del ranking
        for evento in pygame.event.get(): #gestion de eventos
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return "menu"

        imprimir_ranking(ventana) #imprime el ranking
        pygame.display.flip()