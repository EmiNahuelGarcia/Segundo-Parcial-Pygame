import pygame


protagonista = {
    "nombre": "Jugador",
    "vida": 100,
    "vida maxima": 100,
    "ataque": 10,
    "puntuacion": 0,
    "llaves": 0,
    "posicion x": 200,
    "posicion y": 600,  
    "velocidad x": 5,
    "velocidad y": 5,
    "en suelo": True,
    "fuerza salto": 12,
    "gravedad": 0.5
}


sprite_inactivo = pygame.image.load("assets/images/protagonista.png")
sprite_inactivo = pygame.transform.scale(sprite_inactivo, (150, 150))
rect_personaje = sprite_inactivo.get_rect()
rect_personaje.topleft = (protagonista["posicion x"], protagonista["posicion y"])

sprite_corriendo_uno = pygame.image.load("assets/images/protagonista_camina_uno.png")
sprite_corriendo_dos = pygame.image.load("assets/images/protagonista_camina_dos.png")



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