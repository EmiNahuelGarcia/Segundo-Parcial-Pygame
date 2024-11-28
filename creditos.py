import pygame
import sys
from configuracion import *

def creditos(ventana):
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