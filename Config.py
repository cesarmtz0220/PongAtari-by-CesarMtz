#Configuration file of constant parameters and controls

import pygame

# Colors
blue = (240,248,255)
black = (0, 0, 0)
selection_color = (0,0,139)

# Screen
width, height = 800, 600

# Inicialize fonts
pygame.font.init()
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

# Controls (can change dynamically)
controls = {
    "P1_Up": pygame.K_w,
    "P1_Down": pygame.K_s,
    "P2_Up": pygame.K_UP,
    "P2_Down": pygame.K_DOWN
}
