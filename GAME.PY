import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

def random_color():
    return (random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))

ball_radius = 20
ball_x = WIDTH // 3
ball_y = HEIGHT // 3
ball_speed_x = 5
ball_speed_y = 3
ball_color = random_color()

running = True
while running:
    pygame.time.delay(25)
    screen.fill((20, 20, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ball_x -= 6
    if keys[pygame.K_d]:
        ball_x += 6
    if keys[pygame.K_w]:
        ball_y -= 6
    if keys[pygame.K_s]:
        ball_y += 6

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x *= -1
        ball_color = random_color()
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y *= -1
        ball_color = random_color()

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.update()

pygame.quit()
