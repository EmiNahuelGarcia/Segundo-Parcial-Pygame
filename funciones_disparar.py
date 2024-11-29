import pygame
from configuracion import *
from personajes import *
import random
# Lista de proyectiles
proyectiles = []
proyectiles_enemigos = []

# Velocidad del proyectil
velocidad_proyectil = 7

# Cargar imagen del proyectil
proyectil_img = pygame.Surface((10, 5))
proyectil_img.fill((ROJO))  # Color rojo para el proyectil


def disparar(rect_personaje: pygame.rect, proyectiles: list, mirando_derecha: bool, teclas: dict, protagonista: dict, tiempo_actual: int) -> None:
    """Crea un proyectil que se mueve en la dirección del personaje y lo dispara si es posible.

    Esta función verifica si se presiona la tecla de disparo (K_x) y si ha pasado el cooldown 
    entre disparos. Luego, crea un proyectil en la dirección que el personaje está mirando y 
    lo añade a la lista de proyectiles.

    Parámetros:
        rect_personaje (pygame.Rect): El rectángulo que representa al personaje en la pantalla.
        proyectiles (list): La lista donde se almacenan los proyectiles disparados.
        mirando_derecha (bool): Indica si el personaje está mirando hacia la derecha o izquierda.
        teclas (dict): El estado actual de las teclas presionadas.
        protagonista (dict): Información del protagonista, como el cooldown y el último disparo.
        tiempo_actual (int): El tiempo actual del juego para verificar el cooldown.

    No retorna ningún valor."""
    
    # Verifica si se presiona la tecla de disparo y ha pasado el cooldown
    if teclas[pygame.K_x] and tiempo_actual - protagonista["ultimo disparo"] >= protagonista["cooldown disparo"]:
        SONIDO_DISPARO_PROTA.play()
        # Crear un proyectil en la dirección correcta
        proyectil_rect = proyectil_img.get_rect()
        
        if mirando_derecha:
            proyectil_rect.x = rect_personaje.right  # Aparece al lado derecho del personaje
        else:
            proyectil_rect.x = rect_personaje.left - proyectil_rect.width  # Aparece al lado izquierdo del personaje

        proyectil_rect.y = rect_personaje.centery + 10  # Centrado verticalmente

        direccion = "derecha" if mirando_derecha else "izquierda"
        proyectiles.append({"rect": proyectil_rect, "direccion": direccion})

        # Actualiza el tiempo del último disparo
        protagonista["ultimo disparo"] = tiempo_actual
    
    
    


# funcion para actualizar la posición de los proyectiles
def mover_proyectiles(proyectiles: list) -> None:
    '''
    Actualiza la posición de los proyectiles disparados por el protagonista.

    La función mueve los proyectiles hacia la derecha o izquierda según la dirección indicada 
    y elimina aquellos que salen de la pantalla.

    Parámetros:
        proyectiles (list): La lista de proyectiles disparados por el protagonista.

    No retorna ningún valor.
    
    '''
    for proyectil in proyectiles[:]:
        # Mover proyectiles hacia la derecha o hacia la izquierda
        if proyectil["direccion"] == "derecha":
            proyectil["rect"].x += velocidad_proyectil
        elif proyectil["direccion"] == "izquierda":
            proyectil["rect"].x -= velocidad_proyectil

        # Eliminar proyectiles que se salen de la pantalla
        if proyectil["rect"].x < 0 or proyectil["rect"].x > ANCHO:
            proyectiles.remove(proyectil)

# Función para dibujar los proyectiles
def dibujar_proyectiles(ventana: pygame.surface, proyectiles: list) -> None:
    '''
    Dibuja los proyectiles en la ventana.

    Esta función recorre la lista de proyectiles y los dibuja en la ventana en sus respectivas
    posiciones.

    Parámetros:
        ventana (pygame.Surface): La superficie en la que se dibujan los proyectiles.
        proyectiles (list): La lista de proyectiles disparados por el protagonista.

    No retorna ningún valor.
    '''
    for proyectil in proyectiles:
        ventana.blit(proyectil_img, proyectil["rect"])


def disparar_enemigo(enemigo: dict, proyectiles_enemigos: list, rect_personaje: pygame.rect, tiempo_actual: int) -> None:
    """
    Hace que un enemigo dispare un proyectil hacia el protagonista si está alineado verticalmente 
    y ha pasado el cooldown.

    La función comprueba si el enemigo está alineado verticalmente con el protagonista y si 
    el cooldown ha pasado. Si es así, dispara un proyectil hacia el protagonista.

    Parámetros:
        enemigo (dict): Información del enemigo, incluyendo su posición y cooldown.
        proyectiles_enemigos (list): La lista donde se almacenan los proyectiles disparados por los enemigos.
        rect_personaje (pygame.Rect): El rectángulo que representa al protagonista en la pantalla.
        tiempo_actual (int): El tiempo actual del juego para verificar el cooldown.

    No retorna ningún valor.
    """
    if abs(rect_personaje.top - enemigo["posicion y"]) <= 200:  # Margen de alineación en píxeles
        if tiempo_actual - enemigo["ultimo disparo"] >= enemigo["cooldown disparo"]:
            SONIDO_DISPARO_ENEMIGO.play()
            proyectil_rect = proyectil_img.get_rect()  # Crea el rectángulo del proyectil
            print("Enemigo dispara")
            
            if enemigo["direccion"] == "izquierda":
                # El enemigo está mirando a la derecha, el proyectil va a la derecha
                proyectil_rect.x = enemigo["posicion x"] + 40  # Aparece al lado derecho del enemigo
                proyectiles_enemigos.append({"rect": proyectil_rect, "direccion": "derecha"})
            else:
                # El enemigo está mirando a la izquierda, el proyectil va a la izquierda
                proyectil_rect.x = enemigo["posicion x"] - proyectil_rect.width  # Aparece al lado izquierdo del enemigo
                proyectiles_enemigos.append({"rect": proyectil_rect, "direccion": "izquierda"})
            
            proyectil_rect.y = enemigo["posicion y"] + 15  # Centrado verticalmente

            enemigo["ultimo disparo"] = tiempo_actual  # Actualiza el tiempo del último disparo
            #print("ENEMIGO DISPARÓ")

def verificar_colisiones_proyectiles(proyectiles: list, rect_personaje: pygame.rect, enemigos: dict, rects_enemigos: dict, protagonista : dict) -> None:
    """
    Verifica si algún proyectil golpea al protagonista o a los enemigos.

    La función revisa si algún proyectil ha colisionado con el protagonista o con los enemigos.
    Si un proyectil golpea al protagonista, se reduce su vida y puntuación. Si golpea a un enemigo, 
    se reduce su salud y se elimina si la salud llega a cero.

    Parámetros:
        proyectiles (list): La lista de proyectiles disparados por el protagonista.
        rect_personaje (pygame.Rect): El rectángulo que representa al protagonista en la pantalla.
        enemigos (dict): Los enemigos en el juego.
        rects_enemigos (dict): Los rectángulos que representan las posiciones de los enemigos.
        protagonista (dict): Información del protagonista, como su vida y puntuación.

    No retorna ningún valor.
    """
    
    for proyectil in proyectiles_enemigos[:]:  # itera sobre una copia
        # Verificar colisión con el personaje
        if proyectil["rect"].colliderect(rect_personaje):
            protagonista["vida"] = max(protagonista["vida"] - 10, 0)  # Reducir vida del protagonista
            print(protagonista["vida"])
            protagonista["puntuacion"] = max(protagonista["puntuacion"] - 5, 0)
            print(f"{protagonista["puntuacion"]} puntos")
            print("GOLPE AL PROTAGONISTA POR ENEMIGO")
            proyectiles_enemigos.remove(proyectil)  # Eliminar el proyectil tras la colisión
    
    for proyectil in proyectiles[:]:  # itera sobre una copia 
        # Verificar colisión con el personaje
        if proyectil["rect"].colliderect(rect_personaje):           
            proyectiles.remove(proyectil)  # Eliminar el proyectil tras la colisión
            

        # Verificar colision con los enemigos
        for enemigo_key, enemigo_data in enemigos.items():
                # Obtener el rectangulo del enemigo
                enemigo_rect = rects_enemigos[enemigo_key]
                if proyectil["rect"].colliderect(enemigo_rect):
                    # Reducir la salud del enemigo
                    enemigo_data["salud"] -= 10  #10 de daño
                    protagonista["puntuacion"] += 10
                    print(f"{enemigo_key} recibió daño, salud restante: {enemigo_data['salud']}")

                    # Eliminar el proyectil tras la colisión
                    proyectiles.remove(proyectil)

                    # Si el enemigo muere (salud <= 0), eliminarlo
                    if enemigo_data["salud"] <= 0:
                        print(f"{enemigo_key} ha sido destruido.")
                        enemigos.pop(enemigo_key)  # Eliminar el enemigo de la lista
                        rects_enemigos.pop(enemigo_key)  # Eliminar su rectángulo de la lista
                    break  # Romper el ciclo de enemigos, ya que el proyectil 

        

def mover_proyectiles_enemigos(proyectiles_enemigos: list) -> None:
    '''
    Actualiza la posición de los proyectiles disparados por los enemigos.

    La función mueve los proyectiles hacia la derecha o hacia la izquierda según la dirección indicada 
    y elimina aquellos que salen de la pantalla.

    Parámetros:
        proyectiles_enemigos (list): La lista de proyectiles disparados por los enemigos.

    No retorna ningún valor.
    '''
    for proyectil in proyectiles_enemigos[:]:
        if proyectil["direccion"] == "derecha":
            proyectil["rect"].x += velocidad_proyectil  # Mover hacia la derecha
        elif proyectil["direccion"] == "izquierda":
            proyectil["rect"].x -= velocidad_proyectil  # Mover hacia la izquierda

        # Eliminar proyectiles que se salen de la pantalla
        if proyectil["rect"].x < 0 or proyectil["rect"].x > ANCHO:
            proyectiles_enemigos.remove(proyectil)

def dibujar_proyectiles_enemigos(ventana: pygame.surface, proyectiles_enemigos: list) -> None:
    '''
    Dibuja los proyectiles disparados por los enemigos en la ventana.

    La función recorre la lista de proyectiles disparados por los enemigos y los dibuja en la ventana 
    en sus respectivas posiciones.

    Parámetros:
        ventana (pygame.Surface): La superficie en la que se dibujan los proyectiles enemigos.
        proyectiles_enemigos (list): La lista de proyectiles disparados por los enemigos.

    No retorna ningún valor.
    '''
    for proyectil in proyectiles_enemigos:
        ventana.blit(proyectil_img, proyectil["rect"])  # Dibuja el proyectil en su posición



def verificar_vida(protagonista : dict) -> dict:
    """
    Verifica si la vida del protagonista es menor o igual a cero y ajusta el valor.

    Si la vida del protagonista es menor o igual a cero, se ajusta su vida a cero.

    Parámetros:
        protagonista (dict): Información del protagonista, incluyendo su vida.

    Retorna:
        dict: El diccionario actualizado del protagonista.
    """

    if protagonista["vida"] <= 0:
        protagonista["vida"] = 0
        return protagonista

def generar_fuego() -> dict:
    """
    Genera un fuego aleatorio que caerá desde la parte superior de la pantalla.

    Esta función genera un nuevo fuego con una posición aleatoria en el eje X, fuera de la pantalla 
    en el eje Y, y con una velocidad de caída aleatoria.

    Retorna:
        dict: Un diccionario que contiene la posición y velocidad del fuego generado.
    """
    x_random = random.randint(0, ANCHO - ancho_fuego)  # Posición aleatoria en el eje X
    y_inicial = -alto_fuego  # Fuera de la pantalla (parte superior)
    velocidad = random.randint(5, 10)  # Velocidad de caída aleatoria
    return {"rect": pygame.Rect(x_random, y_inicial, ancho_fuego, alto_fuego), "velocidad": velocidad}


# Función para manejar el movimiento y las colisiones de los fuegos
def manejar_fuegos(fuegos_activos: list, ventana: pygame.surface, protagonista: dict, rect_protagonista: pygame.rect) -> None:
    """
    Maneja el movimiento y las colisiones de los fuegos activos.

    La función actualiza la posición de los fuegos activos, los dibuja en la pantalla, y verifica si 
    alguno colisiona con el protagonista. Si colisiona, se reduce la vida del protagonista y el fuego 
    se elimina.

    Parámetros:
        fuegos_activos (list): La lista de fuegos que están en la pantalla.
        ventana (pygame.Surface): La superficie donde se dibujan los fuegos.
        protagonista (dict): Información del protagonista, como su vida.
        rect_protagonista (pygame.Rect): El rectángulo que representa al protagonista en la pantalla.

    No retorna ningún valor.
    """

    for fuego_item in fuegos_activos[:]:  # Hacemos una copia para evitar problemas al eliminar elementos
        fuego_item["rect"].y += fuego_item["velocidad"]  # Actualizar la posición del fuego
        ventana.blit(fuego, fuego_item["rect"])  # Dibujar el sprite del fuego

        # Comprobar colisión con el protagonista
        if rect_protagonista.colliderect(fuego_item["rect"]):
            protagonista["vida"] -= 10  # Reducir vida
            fuegos_activos.remove(fuego_item)  # Eliminar el fuego que colisionó

        # Eliminar el fuego si sale de la pantalla
        elif fuego_item["rect"].y > ALTO:
            fuegos_activos.remove(fuego_item)

    # Generar nuevos fuegos si hay menos de 3
    while len(fuegos_activos) < 4:
        fuegos_activos.append(generar_fuego())

def verificar_colisiones_bolas_fuego_con_protagonista(protagonista: dict, proyectiles_jefe: list, rect_personaje: pygame.rect) -> None:
    """
    Verifica si las bolas de fuego del jefe golpean al protagonista.

    La función revisa si alguna bola de fuego disparada por el jefe ha colisionado con el protagonista.
    Si es así, se reduce la vida y puntuación del protagonista.

    Parámetros:
        protagonista (dict): Información del protagonista, como su vida y puntuación.
        proyectiles_jefe (list): La lista de proyectiles disparados por el jefe.
        rect_personaje (pygame.Rect): El rectángulo que representa al protagonista en la pantalla.

    No retorna ningún valor.
    """
    for bola in proyectiles_jefe[:]:

        if bola["rect"].colliderect(rect_personaje):
            protagonista["vida"] = max(protagonista["vida"] - 10, 0) 
            protagonista["puntuacion"] = max(protagonista["puntuacion"] - 5, 0)
            proyectiles_jefe.remove(bola)
        
        

def verificar_colisiones_con_jefe(proyectiles: list, jefe: dict, rect_jefe: pygame.rect):
    """
    Verifica si los proyectiles disparados por el jugador golpean al jefe y le reducen la vida.

    La función revisa si algún proyectil disparado por el protagonista ha colisionado con el jefe.
    Si es así, se reduce la vida del jefe y se aumenta la puntuación del protagonista.

    Parámetros:
        proyectiles (list): La lista de proyectiles disparados por el protagonista.
        jefe (dict): Información del jefe, como su vida y estado.
        rect_jefe (pygame.Rect): El rectángulo que representa al jefe en la pantalla.

    No retorna ningún valor.
    """
    
    for proyectil in proyectiles[:]:  # Itera sobre una copia de la lista de proyectiles
        # Verificar colisión con el rectángulo del jefe 
        if proyectil["rect"].colliderect(rect_jefe):  # Si el proyectil colide con el jefe
            jefe["vida"] = max(jefe["vida"] - 10, 0)  # Reducir vida del jefe
            protagonista["puntuacion"] += 10
            print(f"El jefe recibió daño, vida restante: {jefe['vida']}")

            # Eliminar el proyectil tras la colisión
            proyectiles.remove(proyectil)
            
            if jefe["vida"] <= 0:
                print("El jefe ha sido derrotado.")
                jefe["estado"] = "muerto"  # Cambiar el estado del jefe a "muerto"
                break