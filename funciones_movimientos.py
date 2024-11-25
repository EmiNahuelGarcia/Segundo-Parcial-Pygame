from configuracion import *
from personajes import *




'''def mover_personaje(personaje, rect_personaje, teclas):
    """Mueve al personaje y actualiza su posición en el rectángulo."""
    # Movimiento horizontal
    if teclas[pygame.K_LEFT]:
        rect_personaje.x -= personaje["velocidad x"]
        personaje["sprite actual"] = "corriendo_1"
        
        
    elif teclas[pygame.K_RIGHT]:
        rect_personaje.x += personaje["velocidad x"]
        personaje["sprite actual"] = "corriendo_1"

    
    else:
        personaje["sprite actual"] = "inactivo"
    
        

    # Salto
    if teclas[pygame.K_SPACE] and personaje["en suelo"]:
        personaje["velocidad y"] = -personaje["fuerza salto"]  # Impulso hacia arriba
        personaje["en suelo"] = False
        personaje["sprite actual"] = "corriendo_1"'''


def mover_personaje(personaje, rect_personaje, teclas):
    """Mueve al personaje y actualiza su posición en el rectángulo."""
    # Movimiento horizontal
    if teclas[pygame.K_LEFT] or teclas[pygame.K_RIGHT]:
        # Cambiar entre los dos sprites de correr
        if personaje.get("ultimo_cambio", 0) + 150 < pygame.time.get_ticks():  # Cambiar cada 150ms
            personaje["ultimo_cambio"] = pygame.time.get_ticks()
            # Alternar entre los dos sprites de correr
            if personaje["sprite actual"] == "corriendo_1":
                personaje["sprite actual"] = "corriendo_2"
            else:
                personaje["sprite actual"] = "corriendo_1"

        # Movimiento a la izquierda
        if teclas[pygame.K_LEFT]:
            rect_personaje.x -= personaje["velocidad x"]

        # Movimiento a la derecha
        if teclas[pygame.K_RIGHT]:
            rect_personaje.x += personaje["velocidad x"]
    else:
        personaje["sprite actual"] = "inactivo"  # Si no se mueve, vuelve al sprite inactivo

    if teclas[pygame.K_SPACE] and personaje["en suelo"]:
        personaje["velocidad y"] = -personaje["fuerza salto"]  # Impulso hacia arriba
        personaje["en suelo"] = False
        personaje["sprite actual"] = "corriendo_1"

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