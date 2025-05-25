import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Custom Event")
clock = pygame.time.Clock()

color = (255, 0, 0)
sprite = pygame.Rect(150, 100, 100, 100)
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR:
            color = (0, 255, 0) if color == (255, 0, 0) else (255, 0, 0)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, sprite)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
