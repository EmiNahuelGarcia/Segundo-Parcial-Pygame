import pygame


protagonista = {
    "nombre": "Jugador",
    "vida": 100,
    "vida maxima": 100,
    "ataque": 10,
    "puntuacion": 0,
    "llaves": 0,
    "posicion x": 20,
    "posicion y": 50,  
    "velocidad x": 5,
    "velocidad y": 5,
    "en suelo": True,
    "fuerza salto": 12,
    "gravedad": 0.5,
    "sprite actual" : "inactivo"
}


sprites = {
    "inactivo": pygame.transform.scale(pygame.image.load("assets/images/protagonista.png"), (120, 150)),
    "corriendo_1": pygame.transform.scale(pygame.image.load("assets/images/protagonista_camina_uno.png"), (200, 170)),
    "corriendo_2": pygame.transform.scale(pygame.image.load("assets/images/protagonista_camina_dos.png"), (200, 170)),
}

# Crear el rectángulo para el personaje, usando el sprite "inactivo" por ahora
rect_personaje = sprites["inactivo"].get_rect()
rect_personaje.topleft = (protagonista["posicion x"], protagonista["posicion y"])
rect_personaje.width = 80  # Ajustar el ancho del rectángulo
rect_personaje.height = 120  # Ajustar la altura del rectángulo



storm_pistola = {
        
        "vida": 30,
        "vida maxima":30,
        "ataque": 10
        }


storm_ametralladora = {

    "vida": 30,
    "vida maxima": 30,
    "ataque": 10
    
    }


mickey_mouse = {

    "vida": 200,
    "vida maxima": 200,
    "ataque": 30


}