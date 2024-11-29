from configuracion import *
from personajes import *





def mover_personaje(personaje: dict, rect_personaje: pygame.surface, teclas: dict, sprites: list) -> None:
    '''
    Mueve al personaje según las teclas presionadas y actualiza su posición en el rectángulo.

    Esta función maneja el movimiento horizontal del personaje (izquierda y derecha) y su salto.
    También actualiza el sprite del personaje para simular la animación de correr y, cuando el personaje no se mueve,
    lo cambia a un estado inactivo.

    Parámetros:
        personaje (dict): Un diccionario que contiene las propiedades del personaje, incluyendo la velocidad de 
        movimiento (`"velocidad x"`), el estado del salto (`"en suelo"`, `"fuerza salto"`),
        el sprite actual (`"sprite actual"`) y el tiempo del último cambio de sprite (`"ultimo_cambio"`).
        rect_personaje (pygame.Rect): El objeto `Rect` que representa la posición y el tamaño del personaje en la pantalla.
        teclas (dict): Un diccionario de teclas presionadas (como las teclas direccionales y espacio), obtenido de 
        `pygame.key.get_pressed()`.
        sprites (dict): Un diccionario de sprites para el personaje, donde cada clave es un nombre de sprite y cada valor es una imagen.

    Modifica:
        personaje (dict): Actualiza las propiedades del personaje, como el sprite actual y la velocidad en el eje Y.
        rect_personaje (pygame.Rect): Actualiza la posición horizontal del personaje en la pantalla y asegura que no se 
        mueva fuera de los límites de la ventana.

    Efectos secundarios:
        - Cambia el sprite del personaje entre dos imágenes de correr, alternando cada 150 ms si el personaje se mueve horizontalmente.
        - Si el personaje se mueve a la izquierda, el sprite se voltea horizontalmente.
        - Si el personaje no se mueve, el sprite se cambia a "inactivo".
        - Si el personaje presiona la barra espaciadora y está en el suelo, se realiza un salto.
    
    '''
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
            # Voltear el sprite horizontalmente cuando va a la izquierda
            '''sprite_volteado = pygame.transform.flip(sprites[personaje["sprite actual"]], True, False)
            sprites[personaje["sprite actual"]] = sprite_volteado'''
            if rect_personaje.left < 10:
                rect_personaje.left = 10
            

        # Movimiento a la derecha
        if teclas[pygame.K_RIGHT]:
            rect_personaje.x += personaje["velocidad x"]
            if rect_personaje.right > ANCHO -10:
                rect_personaje.right = ANCHO -10
            
    else:
        personaje["sprite actual"] = "inactivo"  # Si no se mueve, vuelve al sprite inactivo
        


    if teclas[pygame.K_SPACE] and personaje["en suelo"]:
        personaje["velocidad y"] = -personaje["fuerza salto"]  # Impulso hacia arriba
        personaje["en suelo"] = False
        personaje["sprite actual"] = "corriendo_1"

    

    


def aplicar_gravedad(personaje: dict, rect_personaje: pygame.rect, plataformas: list) -> None:
    '''
    Aplica la gravedad al personaje y verifica si toca el suelo o plataformas.

    Esta función actualiza la velocidad y la posición vertical del personaje según la gravedad.
    Además, verifica si el personaje colisiona con plataformas o el suelo, y ajusta su posición y velocidad en consecuencia.

    Parámetros:
    personaje (dict): Un diccionario que contiene las propiedades del personaje, incluyendo su velocidad vertical 
    (`"velocidad y"`), su estado de colisión con el suelo (`"en suelo"`), la gravedad aplicada 
    (`"gravedad"`), entre otros.
    rect_personaje (pygame.Rect): Un objeto `Rect` que representa las coordenadas y el tamaño del personaje en la pantalla.
    plataformas (list): Una lista de objetos `pygame.Rect` que representan las plataformas en el escenario.

    Modifica:
    personaje (dict): Actualiza las propiedades del personaje relacionadas con la física, como su velocidad y posición.
    rect_personaje (pygame.Rect): Modifica la posición vertical del personaje para simular la gravedad y las colisiones.
    
    Efectos secundarios:
    Si el personaje está cayendo y colisiona con una plataforma o el suelo, su velocidad vertical se detiene y 
    su posición se ajusta para simular el impacto.
    
    '''
    
    """Aplica gravedad y verifica si el personaje toca el suelo."""
    if not personaje["en suelo"]:
        personaje["velocidad y"] += personaje["gravedad"]  # Aumenta la velocidad vertical

    rect_personaje.y += personaje["velocidad y"]  # Actualiza la posición en Y

    # Verificar colisión con las plataformas
    personaje["en suelo"] = False

    for plataforma in plataformas:
        if rect_personaje.colliderect(plataforma) and personaje["velocidad y"] > 0: # Solo si está cayendo
            if rect_personaje.bottom < plataforma.bottom : 
                # Coloca al personaje sobre la plataforma
                rect_personaje.bottom = plataforma.top
                personaje["en suelo"] = True
                personaje["velocidad y"] = 0  # Detener la caída
                break
    
    # Verifica colisión con el suelo
    if rect_personaje.bottom >= ALTO -50:  # un poco mas arriba del suelo para que quede bien esteticamente
        rect_personaje.bottom = ALTO -50
        personaje["en suelo"] = True
        personaje["velocidad y"] = 0  # Detener la caída

    # limitar caida por bugs
    if personaje["velocidad y"] > 15:
        personaje["velocidad y"] = 15