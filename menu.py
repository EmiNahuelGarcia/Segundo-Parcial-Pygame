import pygame
import sys
from configuracion import *
from funciones_monedas import *
from primer_escenario import *
from segundo_escenario import *



def menu(ventana, monedas):
    seleccion = 0  # Inicializa la selección
    fuente = pygame.font.Font(None, 45)
    ejecutando_menu = True
    while ejecutando_menu:
        # Dibujar el fondo
        if FONDO_MENU:
            ventana.blit(FONDO_MENU, (0, 0))
        else:
            ventana.fill((0, 0, 0))  # Fondo negro si no se carga la imagen

        # Dibujar las opciones del menú
        for i, opcion in enumerate(OPCIONES):
            etiqueta = fuente.render(opcion, True, VIOLETA if i == seleccion else BLANCO)
            ventana.blit(etiqueta, (ANCHO // 2 - etiqueta.get_width() // 2, OFFSET_VERTICAL + i * ESPACIADO_VERTICAL))
        
        # Actualizar la pantalla
        pygame.display.update()

        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Cerrar el juego
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:  # Tecla presionada
                if evento.key == pygame.K_DOWN:  # Mover hacia abajo
                    seleccion = (seleccion + 1) % len(OPCIONES)
                if evento.key == pygame.K_UP:  # Mover hacia arriba
                    seleccion = (seleccion - 1) % len(OPCIONES)
                if evento.key == pygame.K_RETURN:  # Seleccionar opción
                    if seleccion == 0:  # Jugar
                        if comprobar_victoria(monedas):
                            return "segundo_escenario"
                        else:
                            return "primer_escenario"
                    elif seleccion == 4:  # Salir
                        pygame.quit()
                        sys.exit()