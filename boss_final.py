import pygame
from configuracion import *

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


# Bola de fuego (que será disparada)
proyectiles_jefe = []

# Configuración de tiempo
TIEMPO_ATAQUE = 1  # 1 segundo entre ataques (más rápido)

# Función para manejar el ataque del jefe
def atacar_jefe(tiempo_actual, proyectiles_jefe):
    """Maneja el ataque del jefe, cambiando entre los sprites y disparando bolas de fuego."""
    
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

def disparar_bola_fuego():
    """Crear un proyectil de bola de fuego disparado por el jefe."""
    if not pygame.mixer.get_busy():  # Verifica si no se está reproduciendo otro sonido
                SONIDO_BOLA.play()
    bola_fuego_rect = bola_fuego_mickey.get_rect()
    bola_fuego_rect.x = jefe["posicion x"] + 40  # Ajusta según la posición del jefe
    bola_fuego_rect.y = jefe["posicion y"] + 10  # Ajusta según la altura del jefe
    proyectiles_jefe.append({"rect": bola_fuego_rect, "direccion": "izquierda"})  

# Agregar un rectángulo para el jefe basado en su posición y tamaño
rect_jefe = pygame.Rect(jefe["posicion x"], jefe["posicion y"], 60, 60)  # Tamaño del jefe: 60x60

def dibujar_jefe(ventana, tiempo_actual):
    """Dibuja el sprite del jefe y maneja su ataque."""
    # Llamamos a la función de ataque cada frame
    
    atacar_jefe(tiempo_actual, proyectiles_jefe)
    
    if jefe["estado"] == "muerto":
        return
    # Dibujar el sprite 
    ventana.blit(sprites_jefe[jefe["estado"]], (jefe["posicion x"], jefe["posicion y"]))

    

def mover_bolas_fuego():
    """Mover las bolas de fuego disparadas por el jefe."""
    for bola in proyectiles_jefe[:]:
        bola["rect"].x -= 10  # Aumentar la velocidad de la bola de fuego

        # Eliminar bolas de fuego fuera de la pantalla
        if bola["rect"].x < 0:
            proyectiles_jefe.remove(bola)

def dibujar_bolas_fuego(ventana):
    """Dibuja las bolas de fuego en la ventana."""
    for bola in proyectiles_jefe:
        ventana.blit(bola_fuego_mickey, bola["rect"])