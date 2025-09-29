import pygame
import sys

# Initialize Pygame
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My first game screen")

# Colors
GREY = (58, 58, 58)

# Load and scale image
image = pygame.image.load('Screenshot 2025-07-13 144530.png')
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)
    screen.blit(image, image_rect)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()