import pygame
import sys
from configuracion import *


def opciones(ventana: pygame.surface) -> str:
    '''
    Esta función muestra un menú de opciones donde el jugador puede ajustar el volumen del juego.
    El jugador puede elegir entre tres opciones:
    1. Apagar sonidos.
    2. Establecer volumen máximo.
    3. Reducir volumen a la mitad.
    La función ajusta el volumen de la música y los efectos de sonido según la opción seleccionada.

    Cuando el jugador selecciona una opción, la función aplica el cambio de volumen correspondiente
    y regresa al menú principal.

    Returns:
    str: Devuelve "menu" para regresar al menú principal después de que el jugador haya hecho su selección.
    
    '''

    seleccion = 0  # Aseguramos que la variable 'seleccion' está inicializada al principio
    ejecutando_opciones = True
    while ejecutando_opciones:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Cerrar el juego
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:  # Tecla presionada
                if evento.key == pygame.K_DOWN:  # Mover hacia abajo
                    seleccion = (seleccion + 1) % 3  # Hay 3 opciones
                if evento.key == pygame.K_UP:  # Mover hacia arriba
                    seleccion = (seleccion - 1) % 3
                if evento.key == pygame.K_RETURN:  # Seleccionar opción
                    if seleccion == 0:  # Apagar sonidos
                        VOLUMEN_MUSICA = 0
                        VOLUMEN_SONIDOS = 0
                        pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
                        for sonido in [SONIDO_DISPARO_PROTA, SONIDO_BOLA, SONIDO_DISPARO_ENEMIGO]:
                            sonido.set_volume(VOLUMEN_SONIDOS)
                    elif seleccion == 1:  # Volumen máximo
                        VOLUMEN_MUSICA = 1.0
                        VOLUMEN_SONIDOS = 1.0
                        pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
                        for sonido in [SONIDO_DISPARO_PROTA, SONIDO_BOLA, SONIDO_DISPARO_ENEMIGO]:
                            sonido.set_volume(VOLUMEN_SONIDOS)
                    elif seleccion == 2:  # Reducir volumen a la mitad
                        VOLUMEN_MUSICA = 0.5
                        VOLUMEN_SONIDOS = 0.5
                        pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
                        for sonido in [SONIDO_DISPARO_PROTA, SONIDO_BOLA, SONIDO_DISPARO_ENEMIGO]:
                            sonido.set_volume(VOLUMEN_SONIDOS)
                    
                    ejecutando_opciones = False  # Salir del bucle y regresar al menú

        # Aquí dibujamos la pantalla de opciones
        ventana.fill((0, 0, 0))  # Fondo negro
        # Dibujar las opciones
        for i, opcion in enumerate(["Apagar Sonidos", "Volumen Máximo", "Volumen Mitad"]):
            color = VIOLETA if i == seleccion else BLANCO
            etiqueta = FUENTE.render(opcion, True, color)
            ventana.blit(etiqueta, (ANCHO // 2 - etiqueta.get_width() // 2, OFFSET_VERTICAL + i * ESPACIADO_VERTICAL))

        # Actualizar pantalla
        pygame.display.update()

    # Retornar al menú después de haber hecho una selección
    return "menu"