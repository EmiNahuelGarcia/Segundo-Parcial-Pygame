import pygame
pygame.init()
import random
import sys
from configuracion import (
    ANCHO,
    ALTO,
    NOMBRE_JUEGO,
    ROJO,
    AZUL,
    FUENTE
    )




ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)

pygame.display.set_caption(NOMBRE_JUEGO)

jugando = True


while jugando:
    

    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            jugando = False

        pygame.display.update()
    
    ventana.fill(ROJO)
    
    x, y = pygame.mouse.get_pos()

    texto = FUENTE.render("DEVELOPERS GAME LA GUERRA DE LAS DIVISIONES", True, AZUL)
    

    ventana.blit(texto, (20, 20))

pygame.quit()