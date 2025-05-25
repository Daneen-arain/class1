import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Ball Challenge")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

ball_size = 20
ball_x = WIDTH // 3
ball_y = HEIGHT - ball_size - 10
ball_speed_y = 0
gravity = 0.5
jump_power = -10
is_jumping = True

platforms = [(random.randint(50, WIDTH - 50), random.randint(100, HEIGHT - 50)) for _ in range(5)]

clock = pygame.time.Clock()

running = True
start_time = pygame.time.get_ticks()  # Get the start time
game_duration = 30000  # Game duration in milliseconds (30 seconds)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    ball_speed_y += gravity
    ball_y += ball_speed_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and is_jumping:
        ball_speed_y = jump_power
        is_jumping = True

    for plat_x, plat_y in platforms:
        if (plat_x < ball_x < plat_x + 80) and (plat_y - ball_size < ball_y < plat_y):
            ball_y = plat_y - ball_size
            ball_speed_y = 0
            is_jumping = False

    if ball_y >= HEIGHT - ball_size:
        print("Game Over!")
        running = False

    # Check if game time is over
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time >= game_duration:
        print("Time's up! Game Over!")
        running = False

    pygame.draw.circle(screen, BLUE, (ball_x, int(ball_y)), ball_size)

    for plat_x, plat_y in platforms:
        pygame.draw.rect(screen, GREEN, (plat_x, plat_y, 80, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
