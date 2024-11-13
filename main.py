import pygame
pygame.init()
import random
import sys
from configuracion import *




ventana = pygame.display.set_mode((ANCHO, ALTO)) #creacion de la ventana

pygame.display.set_caption(NOMBRE_JUEGO) #nombre del juego en la ventana

cuadrado = pygame.Surface((200, 200)) # crea la superficie
cuadrado.fill(ROJO)



texto = FUENTE.render("DEVELOPERS GAME LA GUERRA DE LAS DIVISIONES", True, AZUL) #dibuja un texto en la ventana

#sonido_disparo = pygame.mixer.Sound(disparo.waw) PARA LOS TIROS WACHO





jugando = True
while jugando: #bucle principal del juego
    
    
    for evento in pygame.event.get(): #captura los eventos del juego
        
        if evento.type == pygame.QUIT:
            jugando = False
        
        if evento.type == pygame.KEYDOWN:
            print(f"tecla {evento.key}")
            #if evento.key == pygame.K_SPACE:
                #sonido_disparo.play()
            
                

     
    ventana.blit(FONDO, (0,0)) #pega el fondo
    ventana.blit(darth_vader, (250, 600)) #pega el sprite
    ventana.blit(mickey, (350, 600))
    x, y = pygame.mouse.get_pos() #captura el mouse

    
    

    ventana.blit(texto, (20, 20)) #pega el texto 
    
    pygame.display.update() #updatea la pantalla dentro del bucle para notar cambios

pygame.quit()