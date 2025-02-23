import pygame
from card import Card


pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SpotIt!")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic

    # Drawing code
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Add your drawing code here

    pygame.display.flip()

pygame.quit()