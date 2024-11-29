import pygame


protagonista = {
    "nombre": "Jugador",
    "vida": 100,
    "ataque": 10,
    "puntuacion": 0,
    "posicion x": 20,
    "posicion y": 50,  
    "velocidad x": 5,
    "velocidad y": 0,
    "en suelo": True,
    "fuerza salto": 14,
    "gravedad": 0.5,
    "sprite actual" : "inactivo",
    "ultimo disparo": 0,  # control de disparos
    "cooldown disparo": 500,  # 500 ms entre disparos
    
}


sprites = {
    "inactivo": pygame.transform.scale(pygame.image.load("assets/images/protagonista.png"), (120, 150)),
    "corriendo_1": pygame.transform.scale(pygame.image.load("assets/images/protagonista_camina_uno.png"), (200, 170)),
    "corriendo_2": pygame.transform.scale(pygame.image.load("assets/images/protagonista_camina_dos.png"), (200, 170)),
}

# Crear el rectángulo para el personaje, usando el sprite "inactivo" por ahora
rect_personaje = sprites["inactivo"].get_rect()
rect_personaje.topleft = (protagonista["posicion x"], protagonista["posicion y"])
rect_personaje.width = 70  # Ajustar el ancho del rectángulo
rect_personaje.height = 120  # Ajustar la altura del rectángulo


# Enemigos, usando un diccionario para cada uno
enemigos = {
    "enemigo_1": {
        "tipo": "pistola",  # Tipo de arma
        "sprite": "pistola_izquierda",  # Dirección del sprite
        "salud": 50,
        "posicion x": 200,
        "posicion y": 320,
        "direccion": "izquierda",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos  # Dirección en la que está mirando
    },
    "enemigo_2": {
        "tipo": "pistola",
        "sprite": "pistola_derecha",
        "salud": 50,
        "posicion x": 350,
        "posicion y": 220,
        "direccion": "derecha",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos
    },
    "enemigo_3": {
        "tipo": "ametralladora",
        "sprite": "ametralladora_izquierda",
        "salud": 50,
        "posicion x": 700,
        "posicion y": 650,
        "direccion": "derecha",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos
    },
    "enemigo_4": {
        "tipo": "ametralladora",
        "sprite": "ametralladora_derecha",
        "salud": 50,
        "posicion x": 620,
        "posicion y": 105,
        "direccion": "derecha",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos
    },
}

# Sprites de los enemigos (izquierda y derecha)
sprites_enemigos = {
    "pistola_izquierda": pygame.transform.scale(pygame.image.load("assets/images/enemigo_pistola.png"), (90, 90)),
    "pistola_derecha": pygame.transform.scale(pygame.image.load("assets/images/enemigo_pistola.png"), (90, 90)),
    "ametralladora_izquierda": pygame.transform.scale(pygame.image.load("assets/images/enemigo_ametralladora.png"), (100, 110)),
    "ametralladora_derecha": pygame.transform.scale(pygame.image.load("assets/images/enemigo_ametralladora.png"), (100, 110)),
}

# Crear los rectángulos para cada enemigo
rects_enemigos = {}
for enemigo_key, enemigo_data in enemigos.items():
    # Obtener el sprite y las dimensiones del enemigo
    sprite = sprites_enemigos[enemigo_data["sprite"]]
    rect = sprite.get_rect()  # Obtener el rect del sprite
    rect.topleft = (enemigo_data["posicion x"], enemigo_data["posicion y"])  # Posición del enemigo
    rects_enemigos[enemigo_key] = rect  # Guardar el rect en el diccionario





ancho_fuego = 50
alto_fuego = 50
fuego = pygame.transform.scale(pygame.image.load("assets/images/fuego_segundo_escenario.png"),(ancho_fuego, alto_fuego))




