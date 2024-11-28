import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from primer_escenario import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *
import random

# Lista de proyectiles
proyectiles = []
proyectiles_enemigos = []

# Velocidad del proyectil
velocidad_proyectil = 7

# Cargar imagen del proyectil
proyectil_img = pygame.Surface((10, 5))
proyectil_img.fill((ROJO))  # Color rojo para el proyectil


def disparar(rect_personaje, proyectiles, mirando_derecha, teclas, protagonista, tiempo_actual):
    """Crear un proyectil que se mueve en la dirección del personaje."""
    
    # Verifica si se presiona la tecla de disparo y ha pasado el cooldown
    if teclas[pygame.K_x] and tiempo_actual - protagonista["ultimo disparo"] >= protagonista["cooldown disparo"]:
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


def disparar_enemigo(enemigo, proyectiles_enemigos, rect_personaje, tiempo_actual):
    """Hace que el enemigo dispare si está alineado verticalmente con el protagonista y el cooldown ha pasado."""
    if abs(rect_personaje.top - enemigo["posicion y"]) <= 20:  # Margen de alineación en píxeles
        if tiempo_actual - enemigo["ultimo disparo"] >= enemigo["cooldown disparo"]:
            proyectil_rect = proyectil_img.get_rect()  # Crea el rectángulo del proyectil
            
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



def verificar_colisiones_proyectiles(proyectiles: list, rect_personaje, enemigos, rects_enemigos, protagonista : dict):
    """Verifica si algun proyectil golpea al protagonista o a los enemigos."""
    
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

        

def mover_proyectiles_enemigos(proyectiles_enemigos):
    for proyectil in proyectiles_enemigos[:]:
        if proyectil["direccion"] == "derecha":
            proyectil["rect"].x += velocidad_proyectil  # Mover hacia la derecha
        elif proyectil["direccion"] == "izquierda":
            proyectil["rect"].x -= velocidad_proyectil  # Mover hacia la izquierda

        # Eliminar proyectiles que se salen de la pantalla
        if proyectil["rect"].x < 0 or proyectil["rect"].x > ANCHO:
            proyectiles_enemigos.remove(proyectil)

def dibujar_proyectiles_enemigos(ventana, proyectiles_enemigos):
    for proyectil in proyectiles_enemigos:
        ventana.blit(proyectil_img, proyectil["rect"])  # Dibuja el proyectil en su posición


def generar_fuego():
    x_random = random.randint(0, ANCHO - ancho_fuego)  # Posición aleatoria en el eje X
    y_inicial = -alto_fuego  # Fuera de la pantalla (parte superior)
    velocidad = random.randint(5, 10)  # Velocidad de caída aleatoria
    return {"rect": pygame.Rect(x_random, y_inicial, ancho_fuego, alto_fuego), "velocidad": velocidad}


# Función para manejar el movimiento y las colisiones de los fuegos
def manejar_fuegos(fuegos_activos, ventana, protagonista, rect_protagonista):

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



def verificar_vida(protagonista : dict):

    if protagonista["vida"] <= 0:
        protagonista["vida"] = 0
        return protagonista