import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Add Elements")
font = pygame.font.SysFont(None, 40)

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (150, 100, 200, 100))
    text = font.render("Hello Game!", True, (0, 0, 0))
    screen.blit(text, (170, 130))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
