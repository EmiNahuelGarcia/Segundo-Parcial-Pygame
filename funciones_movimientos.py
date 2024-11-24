from configuracion import *
from personajes import *




def mover_personaje(personaje, rect_personaje, teclas):
    """Mueve al personaje y actualiza su posición en el rectángulo."""
    # Movimiento horizontal
    if teclas[pygame.K_LEFT]:
        rect_personaje.x -= personaje["velocidad x"]
    if teclas[pygame.K_RIGHT]:
        rect_personaje.x += personaje["velocidad x"]

    # Salto
    if teclas[pygame.K_SPACE] and personaje["en suelo"]:
        personaje["velocidad y"] = -personaje["fuerza salto"]  # Impulso hacia arriba
        personaje["en suelo"] = False

def aplicar_gravedad(personaje, rect_personaje):
    """Aplica gravedad y verifica si el personaje toca el suelo."""
    if not personaje["en suelo"]:
        personaje["velocidad y"] += personaje["gravedad"]  # Aumenta la velocidad vertical

    rect_personaje.y += personaje["velocidad y"]  # Actualiza la posición en Y

    # Verifica colisión con el suelo
    if rect_personaje.bottom >= ALTO:  # Asumiendo que el suelo está en el borde inferior
        rect_personaje.bottom = ALTO
        personaje["en suelo"] = True
        personaje["velocidad y"] = 0  # Detener la caída

def dibujar_personaje(ventana, personaje, sprites):
    """Dibuja el sprite actual del personaje en la ventana."""
    frame_actual = personaje["frame_actual"]
    sprite_actual = personaje["sprite_actual"]
    sprite = sprites[sprite_actual][frame_actual]
    ventana.blit(sprite, (personaje["posicion x"], personaje["posicion y"]))