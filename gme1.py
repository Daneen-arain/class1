import pygame
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
clock = pygame.time.Clock()

# Load and scale background
background_image = pygame.transform.scale(pygame.image.load("bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, name, color, height, width, speed):
        super().__init__()
        self.name = name
        self.speed = speed
        self.health = 100
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.velocity = pygame.math.Vector2(0, 0)

    def move(self, x_dir, y_dir):
        self.velocity.x = x_dir * self.speed
        self.velocity.y = y_dir * self.speed
        self.rect.x = max(min(self.rect.x + self.velocity.x, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + self.velocity.y, SCREEN_HEIGHT - self.rect.height), 0)

    def display_info(self, surface):
        label = pygame.font.SysFont("Arial", 14).render(f"{self.name}", True, pygame.Color('white'))
        surface.blit(label, (self.rect.x, self.rect.y - 15))

# Sprite group
all_sprites = pygame.sprite.Group()

# Create player sprite
player = CustomSprite("Player", pygame.Color('black'), 20, 30, MOVEMENT_SPEED)
player.rect.topleft = (random.randint(0, SCREEN_WIDTH - player.rect.width),
                       random.randint(0, SCREEN_HEIGHT - player.rect.height))
all_sprites.add(player)

# Create target sprite
target = CustomSprite("Target", pygame.Color('red'), 20, 30, 0)
target.rect.topleft = (random.randint(0, SCREEN_WIDTH - target.rect.width),
                       random.randint(0, SCREEN_HEIGHT - target.rect.height))
all_sprites.add(target)

# Game loop control
running = True
won = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_dir = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        y_dir = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        player.move(x_dir, y_dir)

        if player.rect.colliderect(target.rect):
            all_sprites.remove(target)
            won = True

    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    for sprite in all_sprites:
        sprite.display_info(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                               (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()