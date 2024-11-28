import pygame


bola_fuego_mickey = pygame.transform.scale(pygame.image.load("ruta/a/bola_fuego_mickey.png"), (40, 40))

sprite_inactivo = pygame.transform.scale(pygame.image.load("assets/images/mickey_inactivo.png"), (80, 80))
sprite_ataque_1 = pygame.transform.scale(pygame.image.load("assets/images/mickey_ataque_uno.png") (80, 80))
sprite_ataque_2 = pygame.transform.scale(pygame.image.load("assets/images/mickey_ataque_dos.png") (80, 80))

sprites_jefe = {
    "inactivo": sprite_inactivo,
    "ataque1": sprite_ataque_1,
    "ataque2": sprite_ataque_2
}

mickey_mouse = {

    "vida": 200,
    "vida maxima": 200,
    "ataque": 30,
    "posicion x": 620,
    "posicion y": 700

}

ultimo_ataque_mickey = reloj.time()
cambiar_sprite_ataque_mickey = True

def actualizar_sprite_ataque_mickey(ultimo_ataque_mickey, cambiar_sprite_ataque_mickey, ventana):
    global ultimo_ataque, cambiar_sprite_ataque
    if reloj.time() - ultimo_ataque_mickey > 2:  # Cambiar cada 2 segundos
        ultimo_ataque_mickey = reloj.time()
        cambiar_sprite_ataque_mickey = not cambiar_sprite_ataque_mickey

    if cambiar_sprite_ataque:
        ventana.blit(sprites_jefe["ataque1"], (620, 700))  # Ataque 1
    else:
        ventana.blit(sprites_jefe["ataque2"], (620, 700))  # Ataque 2