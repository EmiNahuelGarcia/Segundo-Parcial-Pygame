import pygame
from configuracion import *
from funciones_movimientos import *
from menu import *
from personajes import *
from plataformas_primer_escenario import *
from funciones_dibujar import *
from funciones_disparar import *
from funciones_monedas import *
from funciones_reiniciar_juego import *
from boss_final import *


def primer_escenario(ventana: pygame.surface, protagonista: dict, sprites: list, rect_personaje: pygame.rect) -> str:
    """
    Lógica y renderizado del primer escenario del juego.

    Esta función gestiona todo lo relacionado con el primer escenario, incluyendo el manejo de eventos,
    movimiento del protagonista, dibujar los escenarios, colisiones con enemigos, proyectiles y monedas, así como la verificación de la victoria
    y el manejo de la vida y puntuación del jugador. Si el jugador pierde, se muestra la pantalla de Game Over, y si gana,
    se pasa al segundo escenario.

    Returns:
    str: Devuelve el nombre del próximo escenario si el jugador gana o pierde, o "salir" si el jugador cierra la ventana.

    """

    reloj = pygame.time.Clock() 
    jugando = True #inicializa el bucle
    mirando_izquierda = False #gestion de sprites y disparos protagonista
    mirando_derecha = True 
    plataformas = inicializar_plataformas() #creacion de plataformas del primer escenario
    

    while jugando:
        if protagonista["vida"] == 0:
            pygame.mixer.music.stop() #para la musica
            SONIDO_DERROTA.play()
            game_over(ventana, FONDO_GAME_OVER) #pantalla de derrota
            reiniciar_juego()
            reiniciar_vida(protagonista) #funciones donde reinicia el juego
            pygame.mixer.music.play(-1)
            return "menu"

        ventana.blit(FONDO_UNO, (0, 0))  # Fondo del escenario
        tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
        

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #sale del juego
                return "salir"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Si presiona ESC, regresa al menú
                    return "menu"
                
        
        teclas = pygame.key.get_pressed() #toma las teclas presionadas
        
        aplicar_gravedad(protagonista, rect_personaje, plataformas)
        dibujar_plataformas(ventana, plataformas, sprite_plataforma)

        mover_personaje(protagonista, rect_personaje, teclas, sprites)
        
        # Obtener el sprite actual
        sprite_personaje = sprites[protagonista["sprite actual"]]

        # Si el personaje se mueve a la izquierda
        if teclas[pygame.K_LEFT]:
            sprite_personaje = pygame.transform.flip(sprite_personaje, True, False)
            if not mirando_izquierda:
                # Voltea el sprite inactivo también
                sprites["inactivo"] = pygame.transform.flip(sprites["inactivo"], True, False)
                mirando_izquierda = True
                mirando_derecha = False

        # Si el personaje se mueve a la derecha
        if teclas[pygame.K_RIGHT]: 
            if not mirando_derecha:
                # Voltea el sprite inactivo también
                sprites["inactivo"] = pygame.transform.flip(sprites["inactivo"], True, False)
                mirando_izquierda = False
                mirando_derecha = True
        
        #Dibujar los enemigos
        dibujar_enemigos(ventana, enemigos, rects_enemigos, sprites_enemigos)
        # Dibujar las monedas
        dibujar_monedas(ventana, monedas, sprite_moneda) 
        
        disparar(rect_personaje, proyectiles, mirando_derecha, teclas, protagonista, tiempo_actual)
        # Dibujar los proyectiles
        dibujar_proyectiles(ventana, proyectiles)
        # Mover los proyectiles
        mover_proyectiles(proyectiles)
        
        # Actualizar cada enemigo
        for enemigo in enemigos.values():  # Iterar sobre todos los enemigos
            disparar_enemigo(enemigo, proyectiles_enemigos, rect_personaje, tiempo_actual)

        # Verificar colisiones con el protagonista
        verificar_colisiones_proyectiles(proyectiles, rect_personaje, enemigos, rects_enemigos, protagonista)

        verificar_colision_monedas(rect_personaje, monedas, protagonista) #verificacion para recolectar monedas
        if comprobar_victoria(monedas): #verificar si todas las monedas estan capturadas
            pygame.mixer.music.stop()
            SONIDO_VICTORIA.play()
            victoria_primer_escenario(ventana, FONDO_VICTORIA)
            plataformas.clear()
            pygame.mixer.music.play(-1)
            reiniciar_prota(protagonista)
            
            return "segundo_escenario" #se pasa al segundo escenario

        verificar_puntaje(protagonista) 
        verificar_vida(protagonista) #verificaciones de los stats del protagonista

        
        

        # Mover proyectiles enemigos
        mover_proyectiles_enemigos(proyectiles_enemigos)

        # Dibujar los proyectiles enemigos en la pantalla
        dibujar_proyectiles_enemigos(ventana, proyectiles_enemigos)
        

        ventana.blit(sprite_personaje, rect_personaje) #blit del protagonista y su rectangulo
        dibujar_stats(ventana, protagonista) #visualizacion de los stats del prota
        pygame.display.flip()
        reloj.tick(60)

