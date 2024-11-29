import pygame

# Definimos las plataformas como rectángulos
plataformas = [
    pygame.Rect(200, 400, 100, 20), 
    pygame.Rect(350, 300, 100, 20),  
    pygame.Rect(500, 500, 100, 20), 
    pygame.Rect(200, 600, 100, 20),
    pygame.Rect(800, 200, 100, 20),
    pygame.Rect(550, 200, 100, 20)
] #plataformas del primer escenario

sprite_plataforma = pygame.transform.scale(pygame.image.load("assets/images/plataforma.png"), (150, 30)) #sprite y reescalado de las plataformas

def inicializar_plataformas() -> list: #inicializar las plataformas del primer escenario para luego del clear
    '''
    Inicializa las plataformas del primer escenario.

    Esta función crea y devuelve una lista de objetos `pygame.Rect` que representan las plataformas en el primer escenario del juego.
    Cada plataforma está definida por su posición y tamaño, especificados por los parámetros (x, y, ancho, alto).

    Returns:
    list: Una lista de objetos `pygame.Rect`, donde cada uno define una plataforma con una ubicación y dimensiones específicas.
    
    '''
    return [
        pygame.Rect(200, 400, 100, 20),
        pygame.Rect(350, 300, 100, 20),
        pygame.Rect(500, 500, 100, 20),
        pygame.Rect(200, 600, 100, 20),
        pygame.Rect(800, 200, 100, 20),
        pygame.Rect(550, 200, 100, 20)
    ]
    

