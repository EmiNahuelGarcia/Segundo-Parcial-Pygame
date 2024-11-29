import pygame
from configuracion import *
#carga de los sprites del boss y su ataque
bola_fuego_mickey = pygame.transform.scale(pygame.image.load("assets/images/bola_fuego_mickey.png"), (80, 80))
sprite_inactivo = pygame.transform.scale(pygame.image.load("assets/images/mickey_inactivo.png"), (120, 120))
sprite_ataque_1 = pygame.transform.scale(pygame.image.load("assets/images/mickey_ataque_uno.png"), (120, 120))
sprite_ataque_2 = pygame.transform.scale(pygame.image.load("assets/images/mickey_ataque_dos.png"), (120, 120))

# Diccionario de sprites del jefe
sprites_jefe = {
    "inactivo": sprite_inactivo,
    "ataque1": sprite_ataque_1,
    "ataque2": sprite_ataque_2
}

# Datos del jefe
jefe = {
    "vida": 200,
    "vida maxima": 200,
    "ataque": 30,
    "posicion x": 900,
    "posicion y": 650,
    "ultimo_ataque": 0,  # Tiempo del último ataque (en milisegundos)
    "estado": "inactivo"  # Estado inicial
}


# Bola de fuego del boss
proyectiles_jefe = []

# Configuración de tiempo
TIEMPO_ATAQUE = 1  # 1 ataque por segundo


def atacar_jefe(tiempo_actual: int, proyectiles_jefe: list) -> None:
    """
    Maneja el ataque del jefe, cambiando entre los sprites de ataque y disparando bolas de fuego.

    Esta función alterna entre dos tipos de ataque (`"ataque1"` y `"ataque2"`) cada vez que ha pasado 
    el tiempo suficiente desde el último ataque. Cuando el jefe está en cualquiera de estos estados de ataque, 
    dispara una bola de fuego. Después de cada ataque, se actualiza el tiempo del último ataque.

    Parámetros:
        tiempo_actual (int): El tiempo actual en milisegundos, utilizado para comprobar el tiempo transcurrido 
        desde el último ataque.
        proyectiles_jefe (list): Lista que contiene los proyectiles disparados por el jefe. Se utiliza para manejar 
        la creación de nuevos proyectiles de fuego.

    Efectos secundarios:
        - Cambia el estado del jefe entre `"inactivo"`, `"ataque1"` y `"ataque2"`.
        - Dispara una bola de fuego cuando el jefe entra en los estados `"ataque1"` o `"ataque2"`.
        - Actualiza el tiempo del último ataque del jefe.

    Notas:
        - El tiempo de ataque se define por la constante `TIEMPO_ATAQUE` (en segundos) y se convierte a milisegundos 
        para comparar con el tiempo actual.
    """
    
    # Verificar si ha pasado el tiempo suficiente para realizar un nuevo ataque
    if tiempo_actual - jefe["ultimo_ataque"] >= TIEMPO_ATAQUE * 1000:  # Convertir a milisegundos
        # Alternar entre ataque1 y ataque2
        if jefe["estado"] == "inactivo":
            jefe["estado"] = "ataque1"  # Cambiar al primer ataque
        elif jefe["estado"] == "ataque1":
            jefe["estado"] = "ataque2"  # Cambiar al segundo ataque
        else:
            jefe["estado"] = "inactivo"  # Volver al estado inactivo
        
        # Disparar una bola de fuego cuando cambia a "ataque1" o "ataque2"
        if jefe["estado"] in ["ataque1", "ataque2"]:
            disparar_bola_fuego()

        # Actualizar el tiempo del último ataque
        jefe["ultimo_ataque"] = tiempo_actual

def disparar_bola_fuego() -> None:
    """
    Crea un proyectil de bola de fuego disparado por el jefe.

    Esta función genera un proyectil de tipo bola de fuego, posicionándolo en la ubicación del jefe
    y añadiéndolo a la lista de proyectiles del jefe (`proyectiles_jefe`). Además, reproduce un sonido 
    de bola de fuego si no se está reproduciendo otro sonido en ese momento.

    Efectos secundarios:
        - Reproduce un sonido de bola de fuego (si no hay otro sonido reproduciéndose).
        - Crea un nuevo proyectil de bola de fuego y lo añade a la lista de proyectiles del jefe.
        - La posición del proyectil se ajusta a las coordenadas actuales del jefe.

    Notas:
        - El proyectil se mueve hacia la izquierda, como se especifica en el campo `"direccion"`.
        - La posición de la bola de fuego se ajusta con base en las coordenadas del jefe.
    
    """
    if not pygame.mixer.get_busy():  # Verifica si no se está reproduciendo otro sonido
                SONIDO_BOLA.play()
    bola_fuego_rect = bola_fuego_mickey.get_rect()
    bola_fuego_rect.x = jefe["posicion x"] + 40  # Ajusta según la posición del jefe
    bola_fuego_rect.y = jefe["posicion y"] + 10  # Ajusta según la altura del jefe
    proyectiles_jefe.append({"rect": bola_fuego_rect, "direccion": "izquierda"})  

# Agregar un rectángulo para el jefe basado en su posición y tamaño
rect_jefe = pygame.Rect(jefe["posicion x"], jefe["posicion y"], 60, 60)  # Tamaño del jefe: 60x60

def dibujar_jefe(ventana: pygame.surface, tiempo_actual: int) -> None:
    """
    Dibuja el sprite del jefe en la ventana y maneja su ataque.

    Esta función actualiza el estado del jefe y su posición, luego dibuja su sprite en la ventana.
    Además, se encarga de gestionar el ataque del jefe, disparando proyectiles de fuego si es necesario.

    Parámetros:
        ventana (pygame.Surface): La superficie de la ventana donde se dibujará el jefe.
        tiempo_actual (int): El tiempo actual en milisegundos, utilizado para gestionar el ataque del jefe.

    Efectos secundarios:
        - Llama a la función `atacar_jefe` para verificar y ejecutar el ataque del jefe.
        - Si el jefe no está muerto, se dibuja su sprite correspondiente en la ventana.
    
    Notas:
        - El jefe cambia entre diferentes estados (e.g., "inactivo", "ataque1", "ataque2", "muerto") y su sprite se actualiza según el estado actual.
        - El ataque del jefe dispara proyectiles de fuego cada vez que el jefe cambia de estado a "ataque1" o "ataque2".
    
    """
    
    atacar_jefe(tiempo_actual, proyectiles_jefe)
    
    if jefe["estado"] == "muerto":
        return
    # Dibujar el sprite 
    ventana.blit(sprites_jefe[jefe["estado"]], (jefe["posicion x"], jefe["posicion y"]))

    

def mover_bolas_fuego() -> None:
    """
    Mueve las bolas de fuego disparadas por el jefe y elimina las que salen de la pantalla.

    Esta función recorre la lista de proyectiles disparados por el jefe y actualiza su posición 
    en la pantalla. Si una bola de fuego se mueve fuera de la pantalla, se elimina de la lista.

    Efectos secundarios:
        - Modifica la posición de cada bola de fuego en la lista `proyectiles_jefe`.
        - Elimina las bolas de fuego que han salido de la pantalla (cuando su posición en el eje X es menor que 0)
    
    """
    for bola in proyectiles_jefe[:]:
        bola["rect"].x -= 10  # Aumentar la velocidad de la bola de fuego

        # Eliminar bolas de fuego fuera de la pantalla
        if bola["rect"].x < 0:
            proyectiles_jefe.remove(bola)

def dibujar_bolas_fuego(ventana: pygame.surface) -> None:
    """
    Dibuja las bolas de fuego en la ventana.

    Esta función recorre la lista de bolas de fuego disparadas por el jefe y dibuja cada una en
    la ventana usando su rectángulo asociado.

    Parámetros:
        ventana (pygame.Surface): La superficie de la ventana donde se dibujarán las bolas de fuego.

    Efectos secundarios:
        - Dibuja cada bola de fuego en la ventana en su posición actual.
    
    """
    for bola in proyectiles_jefe:
        ventana.blit(bola_fuego_mickey, bola["rect"])