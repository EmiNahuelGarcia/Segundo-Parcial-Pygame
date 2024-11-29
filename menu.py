import pygame
import sys
from configuracion import *
from funciones_monedas import *
from primer_escenario import *
from segundo_escenario import *
from creditos import *
from ranking import *


def menu(ventana: pygame.surface, monedas: list) -> str:
    '''
    Muestra el menú principal del juego y gestiona la navegación entre opciones.

    Esta función despliega un menú con varias opciones, como jugar, acceder a las opciones,
    ver los créditos, ver el ranking, y salir del juego. El jugador puede navegar por las
    opciones usando las teclas de flecha arriba y abajo, y seleccionar una opción con la tecla Enter.

    Args:
    ventana (pygame.Surface): La ventana del juego donde se dibuja el menú.
    monedas (list): Una lista que contiene el estado de las monedas en el juego, utilizada para verificar si el jugador
    ha ganado el juego antes de comenzar el segundo escenario.

    Returns:
    str: El nombre del escenario o pantalla que se debe cargar a continuación. Puede devolver "primer_escenario",
    "segundo_escenario", "opciones", "creditos", "ranking" o "salir".
    
    '''
    
    seleccion = 0  # Inicializa la selección
    ejecutando_menu = True
    while ejecutando_menu:
        # Dibujar el fondo
        if FONDO_MENU:
            ventana.blit(FONDO_MENU, (0, 0))
        else:
            ventana.fill((0, 0, 0))  # Fondo negro si no se carga la imagen

        # Dibujar las opciones del menú
        for i, opcion in enumerate(OPCIONES):
            etiqueta = FUENTE.render(opcion, True, VIOLETA if i == seleccion else BLANCO)
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
                    elif seleccion == 1:
                        return "opciones"
                    elif seleccion == 2:
                        return "creditos"
                    elif seleccion == 3:
                        return "ranking"
                    elif seleccion == 4:  # Salir
                        pygame.quit()
                        sys.exit()