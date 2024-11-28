from personajes import *
from funciones_monedas import *
from configuracion import *

def reiniciar_juego():
    # Reiniciar protagonista
    protagonista.update({
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
        "sprite actual": "inactivo",
        "ultimo disparo": 0,
        "cooldown disparo": 500
    })
    rect_personaje.topleft = (protagonista["posicion x"], protagonista["posicion y"]) # Reinicia rectangulo
    # Reiniciar enemigos
    enemigos.clear()
    enemigos.update({
    "enemigo_1": {
        "tipo": "pistola",  # Tipo de arma
        "sprite": "pistola_izquierda",  # Dirección del sprite
        "salud": 100,
        "posicion x": 200,
        "posicion y": 320,
        "direccion": "izquierda",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos  # Dirección en la que está mirando
    },
    "enemigo_2": {
        "tipo": "pistola",
        "sprite": "pistola_derecha",
        "salud": 100,
        "posicion x": 350,
        "posicion y": 220,
        "direccion": "derecha",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos
    },
    "enemigo_3": {
        "tipo": "ametralladora",
        "sprite": "ametralladora_izquierda",
        "salud": 100,
        "posicion x": 700,
        "posicion y": 650,
        "direccion": "derecha",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos
    },
    "enemigo_4": {
        "tipo": "ametralladora",
        "sprite": "ametralladora_derecha",
        "salud": 100,
        "posicion x": 620,
        "posicion y": 105,
        "direccion": "derecha",
        "ultimo disparo": 0,  # Tiempo del último disparo
        "cooldown disparo": 1000  # Tiempo en milisegundos entre disparos
    },
}
    )

    # Reiniciar rectángulos de enemigos
    rects_enemigos.clear()
    for enemigo_key, enemigo_data in enemigos.items():
        sprite = sprites_enemigos[enemigo_data["sprite"]]
        rect = sprite.get_rect()
        rect.topleft = (enemigo_data["posicion x"], enemigo_data["posicion y"])
        rects_enemigos[enemigo_key] = rect

    # Reiniciar monedas
    for moneda in monedas:
        moneda["recogida"] = False
    
    


def game_over(ventana, fondo_game_over):
    reloj = pygame.time.Clock()
    mostrar_pantalla = True

    while mostrar_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Si presionan Enter
                    mostrar_pantalla = False  # Salimos de esta pantalla y volvemos al menú

        # Dibujamos el fondo de Game Over
        ventana.blit(fondo_game_over, (0, 0))

        # Agregamos texto en pantalla
        texto_perdiste = FUENTE.render("¡PERDISTE!", True, (ROJO))  
        texto_reiniciar = FUENTE.render("Presiona Enter para continuar", True, (ROJO))  

        # Centramos los textos en la pantalla
        ventana.blit(texto_perdiste, (ANCHO // 2 - texto_perdiste.get_width() // 2, ALTO // 2 - 50))
        ventana.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 20))

        pygame.display.flip()
        reloj.tick(60)


def comprobar_victoria(monedas):
    for moneda in monedas:
        if not moneda["recogida"]:  # Es false si hay alguna que no este recogida
            return False
    return True  # Es true si todas las monedas estan como recogidas"


def victoria_primer_escenario(ventana, fondo_victoria_primer_escenario):
    reloj = pygame.time.Clock()
    mostrar_pantalla = True

    while mostrar_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Si presionan Enter
                    mostrar_pantalla = False  # Salimos de esta pantalla y volvemos al menú

        # Dibujamos el fondo de Game Over
        ventana.blit(fondo_victoria_primer_escenario, (0, 0))

        # Agregamos texto en pantalla
        texto_perdiste = FUENTE.render("¡GANASTE EL PRIMER ESCENARIO!", True, (ROJO))  
        texto_reiniciar = FUENTE.render("Presiona Enter para continuar", True, (ROJO))  

        # Centramos los textos en la pantalla
        ventana.blit(texto_perdiste, (ANCHO // 2 - texto_perdiste.get_width() // 2, ALTO // 2 - 50))
        ventana.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 20))

        pygame.display.flip()
        reloj.tick(60)