import pygame
from personajes import *

# Lista de monedas
monedas = [
    {"rect": pygame.Rect(220, 500, 30, 30), "recogida": False},  
    {"rect": pygame.Rect(220, 300, 30, 30), "recogida": False} ,
    {"rect": pygame.Rect(370, 200, 30, 30), "recogida": False},  
    {"rect": pygame.Rect(820, 100, 30, 30), "recogida": False}
] # las monedas del primer escenario

# Cargar el sprite de la moneda
sprite_moneda = pygame.transform.scale(pygame.image.load("assets/images/cristal_escenario_uno.png"), (100, 90))

def verificar_colision_monedas(rect_personaje: pygame.rect, monedas: list, protagonista : dict) -> dict:
    '''
    Verifica las colisiones entre el personaje y las monedas en el juego.

    Si el personaje recoge una moneda (es decir, colisiona con ella), la moneda se marca como recogida, 
    se incrementa la puntuación del protagonista y se muestra un mensaje en la consola.

    Parámetros:
        rect_personaje (pygame.Rect): El objeto `Rect` que representa la posición y el tamaño del personaje en la pantalla.
        monedas (list): Una lista de diccionarios que representan las monedas en el juego. Cada moneda tiene un 
        `rect` (objeto `Rect` que representa su posición) y un valor booleano `recogida` que indica si la moneda ha sido recogida.
        protagonista (dict): Un diccionario que contiene las propiedades del protagonista, incluyendo su puntuación (`"puntuacion"`).

    Retorna:
        dict: El diccionario actualizado del protagonista, con la nueva puntuación si se recogió una moneda.

    Efectos secundarios:
        - Marca la moneda como recogida al colisionar con el personaje.
        - Incrementa la puntuación del protagonista en 50 puntos por cada moneda recogida.
        - Imprime en la consola la puntuación actual del protagonista y un mensaje indicando que la moneda fue recogida.
    
    '''

    for moneda in monedas:
        if not moneda["recogida"] and moneda["rect"].colliderect(rect_personaje):
            moneda["recogida"] = True
            protagonista["puntuacion"] += 50
            print(protagonista["puntuacion"])
            print("¡Moneda recogida!")
            return protagonista
        
def verificar_puntaje(protagonista : dict) -> dict:
    '''
    Verifica y ajusta la puntuación del protagonista.

    Si la puntuación del protagonista es menor o igual a 0, la ajusta a 0 para evitar valores negativos.

    Parámetros:
        protagonista (dict): Un diccionario que contiene las propiedades del protagonista, incluyendo su puntuación (`"puntuacion"`).

    Retorna:
        dict: El diccionario actualizado del protagonista con la puntuación ajustada a 0 si era negativa o igual a 0.

    Efectos secundarios:
        - Si la puntuación del protagonista es menor o igual a 0, se establece en 0.
    
    
    '''
    if protagonista["puntuacion"] <= 0:
        
        protagonista["puntuacion"] = 0
        return protagonista
