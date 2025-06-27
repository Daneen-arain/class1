import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game")

running = True
while running:
    screen.fill((50, 150, 255))  # Blue background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
