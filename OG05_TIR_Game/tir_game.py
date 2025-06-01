import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hit the Target !")

target_image = pygame.image.load("target.png")
target_rect = target_image.get_rect()

def get_random_position():
    x = random.randint(0, SCREEN_WIDTH - target_rect.width)
    y = random.randint(0, SCREEN_HEIGHT - target_rect.height)
    return x, y

target_rect.topleft = get_random_position()

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if target_rect.collidepoint(event.pos):
                target_rect.topleft = get_random_position()

    screen.blit(target_image, target_rect)

    pygame.display.flip()

pygame.quit()