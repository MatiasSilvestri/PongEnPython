#Pong
from lib import pygame

# Inicializamos Pygame
pygame.init()

# Establecemos el tamaño de la pantalla
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Establecemos el título de la ventana
pygame.display.set_caption("Pong")

# Creamos dos paletas, una para cada jugador
player_1_pos = [20, screen_height // 2]
player_2_pos = [screen_width - 20, screen_height // 2]
player_width, player_height = 20, 100

# Creamos la pelota
ball_pos = [screen_width // 2, screen_height // 2]
ball_radius = 10
ball_vel = [4, 4]

# Creamos los colores que vamos a usar
WHITE = (255, 255, 255)

# Creamos la fuente para el marcador
font = pygame.font.Font(None, 36)

# Creamos el bucle principal del juego
while True:
    # Procesamos los eventos de entrada
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizamos la posición de la pelota
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Comprobamos si la pelota ha chocado con algún borde
    if ball_pos[1] < ball_radius or ball_pos[1] > screen_height - ball_radius:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] < ball_radius:
        ball_vel[0] = -ball_vel[0]
        player_2_score += 1
    if ball_pos[0] > screen_width - ball_radius:
        ball_vel[0] = -ball_vel[0]
        player_1_score += 1

    # Dibujamos la pantalla
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)
    pygame.draw.rect(screen, WHITE, (player_1_pos[0], player_1_pos[1], player_width, player_height))
    pygame.draw.rect(screen, WHITE, (player_2_pos[0], player_2_pos[1], player_width, player_height))

# Actualizamos el marcador