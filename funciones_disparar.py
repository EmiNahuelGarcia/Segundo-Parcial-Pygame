import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from primer_escenario import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *

# Lista de proyectiles
proyectiles = []

# Velocidad del proyectil
velocidad_proyectil = 10

# Cargar imagen del proyectil
proyectil_img = pygame.Surface((10, 5))
proyectil_img.fill((255, 0, 0))  # Color rojo para el proyectil

# funcion para disparar
def disparar(rect_personaje, proyectiles, mirando_derecha,teclas):
    """Crear un proyectil que se mueve en la dirección del personaje."""
    
    if teclas[pygame.K_x]:
        if mirando_derecha:
            # Crear el proyectil y añadirlo a la lista de proyectiles
            proyectil_rect = proyectil_img.get_rect()
            proyectil_rect.x = rect_personaje.right  # Aparece al lado derecho del personaje
            proyectil_rect.y = rect_personaje.centery - 2  # Centrado verticalmente
            proyectiles.append({"rect": proyectil_rect, "direccion": "derecha"})
        else:
            # Crear el proyectil y añadirlo a la lista de proyectiles
            proyectil_rect = proyectil_img.get_rect()
            proyectil_rect.x = rect_personaje.left - proyectil_rect.width  # Aparece al lado izquierdo del personaje
            proyectil_rect.y = rect_personaje.centery - 2  # Centrado verticalmente
            proyectiles.append({"rect": proyectil_rect, "direccion": "izquierda"})

# Función para actualizar la posición de los proyectiles
def mover_proyectiles(proyectiles):
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
def dibujar_proyectiles(ventana, proyectiles):
    for proyectil in proyectiles:
        ventana.blit(proyectil_img, proyectil["rect"])