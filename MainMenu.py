#File with functions to build main menu and its configurations

import pygame
import os
from Config import width, height, blue, black, selection_color, font, small_font, controls

menu_options = ["Start Game", "Keys Bindings", "Game Instructions"]
menu_image = pygame.image.load(os.path.join("Images", "menu_background.png"))
menu_image = pygame.transform.scale(menu_image, (width, height))

def draw_menu(window, selected):
    window.blit(menu_image, (0, 0))  
    title = font.render("ATARI PONG - Main Menu", True, black)
    window.blit(title, (width // 2 - title.get_width() // 2, 50))
    for i, option in enumerate(menu_options):
        color = selection_color if i == selected else black
        text = small_font.render(option, True, color)
        window.blit(text, (width // 2 - text.get_width() // 2, 150 + i * 60))

    inst_font = pygame.font.Font(None, 30)
    small_text = inst_font.render("Use the arrow keys to move and Enter to select.", True, black)
    window.blit(small_text, (width // 2 - small_text.get_width() // 2, height - small_text.get_height() - 5))

        
    pygame.display.flip()

def draw_instructions(window):
    window.blit(menu_image, (0, 0))
    title = font.render("Game Instructions", True, black)
    window.blit(title, (width // 2 - title.get_width() // 2, 50))
    lines = [
        "Use the paddle to hit the ball", 
        "and stop it from getting past your side.",
        "Move up or down to return the ball.",
        "First player to score 5 points wins",
        "Press ESC anytime to return to main menu"
    ]
    for i, line in enumerate(lines):
        text = small_font.render(line, True, black)
        window.blit(text, (width // 2 - text.get_width() // 2, 150 + i * 50))
    pygame.display.flip()

def draw_config(window):
    window.blit(menu_image, (0, 0))
    title = font.render("Keys Bindings", True, black)
    window.blit(title, (width // 2 - title.get_width() // 2, 50))
    for i, (action, key) in enumerate(controls.items()):
        key_name = pygame.key.name(key).upper()
        label = small_font.render(f"{action}: {key_name}", True, black)
        window.blit(label, (width // 2 - label.get_width() // 2, 150 + i * 50))
    back = small_font.render("Press ESC to return", True, black)
    window.blit(back, (width // 2 - back.get_width() // 2, height - 60))
    pygame.display.flip()
