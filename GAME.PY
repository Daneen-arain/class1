
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Fun!")

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4, 4
ball_color = random_color()

running = True
while running:
    pygame.time.delay(30)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= 5
    if keys[pygame.K_RIGHT]:
        ball_x += 5
    if keys[pygame.K_UP]:
        ball_y -= 5
    if keys[pygame.K_DOWN]:
        ball_y += 5

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
        ball_color = random_color()
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y = -ball_speed_y
        ball_color = random_color()

    pygame.draw.rect(screen, ball_color, (ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2))
    pygame.display.update()

pygame.quit()

