import pygame
import sys
from configuracion import *


def menu(ventana):
    opciones = ["Jugar", "Salir"]
    opcion_seleccionada = 0  # Índice de la opción seleccionada

    ejecutando_menu = True
    while ejecutando_menu:
        ventana.fill(NEGRO)  # Fondo negro

        # Dibujar las opciones del menú
        for i, texto in enumerate(opciones):
            color = AZUL if i == opcion_seleccionada else BLANCO  # Resalta la opción seleccionada
            render_texto = FUENTE.render(texto, True, color)
            ventana.blit(render_texto, (ANCHO // 2 - render_texto.get_width() // 2, 200 + i * 60))

        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:  # Mover hacia arriba
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                if evento.key == pygame.K_DOWN:  # Mover hacia abajo
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                if evento.key == pygame.K_RETURN:  # Seleccionar opción
                    if opciones[opcion_seleccionada] == "Jugar":
                        return "primer_escenario"
                     
                    elif opciones[opcion_seleccionada] == "Salir":
                        pygame.quit()
                        sys.exit()

        # Actualizar pantalla
        pygame.display.flip()