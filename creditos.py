import pygame
import sys
from configuracion import *

def creditos(ventana: pygame.surface) -> str:
    '''
    Muestra la pantalla de créditos del juego.

    Esta función carga la imagen de fondo de los créditos, la muestra en la ventana 
    y espera que el jugador presione Enter para volver al menú principal. Si el jugador 
    cierra la ventana o presiona la tecla Esc, se termina el juego.

    Parámetros:
        ventana (pygame.Surface): La ventana en la que se dibujan los créditos.

    Retorna:
        str: "menu" si el jugador presiona Enter para regresar al menú principal.
    
    '''

    background = pygame.image.load(CREDITOS_PATH)
    while True:
        ventana.blit(background, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    return "menu"
        pygame.display.flip()