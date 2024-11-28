import pygame

def dibujar_plataformas(ventana, plataformas, sprite_plataforma):
    """Dibuja las plataformas con el sprite en la ventana."""
    for plataforma in plataformas:
        ventana.blit(sprite_plataforma, plataforma)


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
    texto_vida = FUENTE.render(f"Vida: {protagonista['vida']}", True, ROJO)
    ventana.blit(texto_vida, (10, 10))  # Dibujar en la posición (10, 10)

    # Texto para el ranking/puntuación
    texto_puntuacion = FUENTE.render(f"Ranking: {protagonista['puntuacion']}", True, ROJO)
    ventana.blit(texto_puntuacion, (10, 50))  # Dibujar en la posición (10, 50)