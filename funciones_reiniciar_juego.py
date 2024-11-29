from personajes import *
from funciones_monedas import *
from configuracion import *
from ranking import *

def reiniciar_juego() -> None:
    '''
    Reinicia el estado del juego, incluyendo el protagonista, los enemigos, las monedas y sus respectivos
    rectángulos de colisión.

    Esta función restablece los atributos del protagonista, como la salud, la puntuación, la posición y otros
    parámetros relacionados con su movimiento y habilidades. Además, reinicia el estado de los enemigos, 
    incluyendo su salud, posición, tipo de arma, y el estado de los disparos. También se reinician las monedas,
    asegurando que no hayan sido recogidas aún.

    Además, se actualizan los rectángulos de colisión tanto del protagonista como de los enemigos para reflejar
    sus posiciones iniciales.

    No recibe parámetros y no devuelve ningún valor.
    '''
    # Reiniciar protagonista
    protagonista.update({
        "nombre": "Jugador",
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

   
    
    
def reiniciar_jefe(jefe: dict) -> None:
    """
    Reinicia las propiedades del jefe al inicio de la partida usando update.
    recibe el diccionario del jefe
    no retorna nada, ya que solo lo modifica
    
    """
    jefe.update({
        "vida": 200,              
        "vida maxima": 200,    
        "ataque": 30,              
        "posicion x": 900,        
        "posicion y": 650,         
        "ultimo_ataque": 0,        
        "estado": "inactivo"       
    })

def game_over(ventana: pygame.surface, fondo_game_over: pygame.surface) -> None:
    '''
    Muestra la pantalla de 'Game Over' cuando el jugador pierde y espera una acción para continuar.

    Esta función se ejecuta cuando el jugador pierde la partida. Muestra un fondo con el mensaje "¡PERDISTE!"
    y ofrece la opción de presionar Enter para regresar al menú. Durante la visualización de esta pantalla,
    la función maneja eventos de teclado y salida del juego.

    La pantalla de 'Game Over' se muestra con el fondo proporcionado como argumento, y muestra un mensaje
    con instrucciones para continuar el juego.

    Parámetros:
    ventana (pygame.Surface): La superficie de la ventana del juego donde se dibujarán los elementos de la pantalla.
    fondo_game_over (pygame.Surface): La imagen o superficie que se usará como fondo para la pantalla de 'Game Over'.

    No devuelve ningún valor. Regresa al menú principal una vez que el jugador presiona Enter.
    
    '''
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


def comprobar_victoria(monedas: list) -> True:
    '''
    Verifica si el jugador ha recogido todas las monedas en el juego.

    Esta función recorre la lista de monedas y comprueba si todas han sido recogidas por el jugador.
    Si alguna moneda no ha sido recogida, la función devuelve False, indicando que el jugador no ha ganado aún.
    Si todas las monedas han sido recogidas, la función devuelve True, indicando que el jugador ha ganado.

    Parámetros:
    monedas (list): Una lista de diccionarios, donde cada diccionario representa una moneda en el juego.
    Cada diccionario tiene la clave "recogida" que indica si la moneda ha sido recogida
    por el jugador (True) o no (False).

    Retorna:
    bool: True si el jugador ha recogido todas las monedas, False si al menos una no ha sido recogida.
    '''
    for moneda in monedas:
        if not moneda["recogida"]:  # Es false si hay alguna que no este recogida
            return False
    return True  # Es true si todas las monedas estan como recogidas"


def victoria_primer_escenario(ventana: pygame.surface, fondo_victoria: pygame.surface) -> None:
    '''
    Muestra la pantalla de victoria al completar el primer escenario del juego.

    Esta función muestra una pantalla de victoria con un mensaje que indica que el jugador ha completado el
    primer escenario. El jugador puede presionar Enter para continuar y regresar al menú principal del juego.

    La función maneja los eventos de teclado y permite que el jugador cierre la pantalla de victoria al presionar
    la tecla Enter. Durante este proceso, se muestra el fondo de victoria y los textos correspondientes en la ventana.

    '''
    reloj = pygame.time.Clock()
    mostrar_pantalla = True

    while mostrar_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  
                    mostrar_pantalla = False  

        # fondo de Game Over
        ventana.blit(fondo_victoria, (0, 0))

        # texto en pantalla
        texto_perdiste = FUENTE.render("¡GANASTE EL PRIMER ESCENARIO!", True, (ROJO))  
        texto_reiniciar = FUENTE.render("Presiona Enter para continuar", True, (ROJO))  

        # centrar los textos en la pantalla
        ventana.blit(texto_perdiste, (ANCHO // 2 - texto_perdiste.get_width() // 2, ALTO // 2 - 50))
        ventana.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 20))

        pygame.display.flip()
        reloj.tick(60)
    

def reiniciar_prota(protagonista: dict) -> None:
    '''
    modifica con update los datos del protagonista
    toma como argumento el diccionario protagonista
    tambien vuelve a colocar el rect del protagonista
    no retorna nada, lo modifica
    '''
    protagonista.update({
        "nombre": "Jugador",
        "ataque": 10,
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


def reiniciar_vida(protagonista: dict) -> None:
    '''
    modifica la vida del protagonista a 100 para reiniciarla
    toma como argumento el diccionario protagonista
    no retorna nada, lo modifica
    '''
        
    protagonista["vida"] = 100
    
def comprobar_victoria_juego(jefe: dict) -> bool:
    '''
    comprueba si el estado del jefe es "muerto"
    esto ocurre cuando la vida es 0
    retorna un booleano
    '''
    if jefe["estado"] == "muerto": #comprueba si el boss murio
        return True
        


def victoria_segundo_escenario(ventana: pygame.surface, fondo_victoria: pygame.surface, protagonista: dict) -> None:
    '''
    Muestra la pantalla de victoria al finalizar el segundo escenario y gestiona la entrada del nombre del jugador,
    así como la actualización del leaderboard.

    Esta función muestra una pantalla de victoria donde el jugador puede ingresar su nombre para ser guardado
    en un archivo JSON que contiene el leaderboard del juego. El jugador puede presionar Enter para continuar después
    de ingresar su nombre. La puntuación del jugador se guarda junto con el nombre y se actualiza el leaderboard
    manteniendo solo las 5 mejores puntuaciones.

    Si el archivo JSON con el leaderboard no existe o está corrupto, se crea uno nuevo y se guarda la información.

    Args:
    ventana (pygame.Surface): La ventana del juego donde se muestra la pantalla de victoria.
    fondo_victoria (pygame.Surface): La imagen de fondo que se muestra en la pantalla de victoria.
    protagonista (dict): El diccionario que contiene los datos del protagonista, incluyendo la puntuación final.
    
    '''

    reloj = pygame.time.Clock()
    mostrar_pantalla = True
    nombre_usuario = ""
    jugador_finalizado = False

    # Cargar o inicializar el leaderboard
    try:
        with open("leaderboard.json", "r") as archivo:
            leaderboard = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        leaderboard = []

    while mostrar_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Si presiona Enter
                    if jugador_finalizado:
                        mostrar_pantalla = False  # Sale al Menu
                    else:
                        # Guardamos el nombre del jugador y la puntuación
                        nombre_final = nombre_usuario if nombre_usuario else "Jugador Anónimo"
                        puntuacion = protagonista.get("puntuacion", 0)  
                        leaderboard.append({"nombre": nombre_final, "puntos": puntuacion})

                        # Ordenamos el leaderboard y guardamos solo el Top 5
                        leaderboard = sorted(leaderboard, key=lambda x: x["puntos"], reverse=True)[:5]
                        with open("leaderboard.json", "w") as archivo:
                            json.dump(leaderboard, archivo, indent=4)
                        jugador_finalizado = True

                elif evento.key == pygame.K_BACKSPACE:  # Borrar último carácter
                    nombre_usuario = nombre_usuario[:-1]
                elif evento.unicode.isalpha() and len(nombre_usuario) < 15:  # Letras (máximo 15 caracteres)
                    nombre_usuario += evento.unicode.upper()

        # Dibujamos el fondo
        ventana.blit(fondo_victoria, (0, 0))

        # Dibujamos los textos
        texto_victoria = FUENTE.render("¡GANASTE EL JUEGO!", True, ROJO)
        texto_ingresar_nombre = FUENTE.render("Ingresa tu nombre:", True, ROJO)
        texto_nombre = FUENTE.render(nombre_usuario, True, BLANCO)
        texto_reiniciar = FUENTE.render("Presiona Enter para continuar", True, ROJO)

        ventana.blit(texto_victoria, (ANCHO // 2 - texto_victoria.get_width() // 2, ALTO // 2 - 100))
        ventana.blit(texto_ingresar_nombre, (ANCHO // 2 - texto_ingresar_nombre.get_width() // 2, ALTO // 2 - 50))
        ventana.blit(texto_nombre, (ANCHO // 2 - texto_nombre.get_width() // 2, ALTO // 2))
        ventana.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 100))

        pygame.display.flip()
        reloj.tick(60)