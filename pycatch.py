import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprites")
clock = pygame.time.Clock()

player = pygame.Rect(200, 150, 50, 50)
velocity = 5

running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= velocity
    if keys[pygame.K_RIGHT]:
        player.x += velocity
    if keys[pygame.K_UP]:
        player.y -= velocity
    if keys[pygame.K_DOWN]:
        player.y += velocity

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
