import pygame
from configuracion import *

def dibujar_plataformas(ventana, plataformas, sprite_plataforma):
    """Dibuja las plataformas con el sprite en la ventana."""
    for plataforma in plataformas:
        ventana.blit(sprite_plataforma, plataforma)


def handle_saltos(ciclo_saltos):
    if ciclo_saltos < 2:
        return 0
    elif ciclo_saltos < 4:
        return 1
    else:
        return 2

def dibujar_jefe(ventana, jefe, sprite_jefe, rect_jefe, tiempo):
    sprite_jefe_volteado = {
        "inactivo": pygame.transform.flip(sprite_jefe["inactivo"], True, False),
        "ataque_uno": pygame.transform.flip(sprite_jefe["ataque_uno"], True, False),
        "ataque_dos": pygame.transform.flip(sprite_jefe["ataque_dos"], True, False),
    }

    coordenadas = [(800, 580), (500, 450), (100, 580)]

    ciclo_saltos = (tiempo/1000) % 6
    ciclo_tiempo = (tiempo/1000) % 2  # 2 segundos por ciclo

    i = handle_saltos(ciclo_saltos)

    if ciclo_tiempo < 1:
        ventana.blit(sprite_jefe_volteado["inactivo"], coordenadas[i]) # 0 a 1
    else:
        if ciclo_tiempo < 1.5:
            ventana.blit(sprite_jefe_volteado["ataque_uno"], coordenadas[i]) #1 a 1.5
        else:
            ventana.blit(sprite_jefe["ataque_dos"], coordenadas[i]) #1.5 a 2
    

    
    

    # 1 segundo inactivo
    # 1 segundo rotando entre ataque uno y ataque dos
    # ir al lado contrario



    

def dibujar_enemigos(ventana, enemigos, rects_enemigos, sprites_enemigos):
    for enemigo_id, enemigo_data in enemigos.items():
        sprite = sprites_enemigos[enemigo_data["sprite"]]
        
        # Si el enemigo está mirando a la izquierda, no hace falta hacer nada
        if enemigo_data["direccion"] == "izquierda":
            ventana.blit(sprite, rects_enemigos[enemigo_id])
        else:  # Si el enemigo está mirando a la derecha, se voltea el sprite
            sprite_volteado = pygame.transform.flip(sprite, True, False)
            ventana.blit(sprite_volteado, rects_enemigos[enemigo_id])


def dibujar_monedas(ventana, monedas, sprite_moneda):
    for moneda in monedas:
        if not moneda["recogida"]:
            ventana.blit(sprite_moneda, moneda["rect"])


def dibujar_stats(ventana, protagonista):
    """Dibuja la vida y el ranking del protagonista en la esquina superior izquierda."""
    # Texto para la vida
    fuente = pygame.font.Font(FONT_PATH, 36)
    texto_vida = fuente.render(f"{protagonista['vida']}", True, BLANCO)
    ventana.blit(texto_vida, (120, 40))  # Dibujar en la posición (10, 10)

    # Texto para el ranking/puntuación
    texto_puntuacion = fuente.render(f"{protagonista['puntuacion']}", True, BLANCO)
    ventana.blit(texto_puntuacion, (320, 40))  # Dibujar en la posición (10, 50)