import pygame
import sys
from Config import width, height
import MainMenu
import PongGame

pygame.init()

size = width, height
screen = pygame.display.set_mode(size) #Window size
pygame.display.set_caption("ATARI PONG")

game_state = "menu"
previous_state = None #Flag for sound effect

Menu_sound = pygame.mixer.Sound("SoundEffects/MenuMusic.mp3")
Menu_sound.set_volume(0.2)
GameStart_sound = pygame.mixer.Sound("SoundEffects/GameStart.mp3")
selected_option = 0

clock = pygame.time.Clock()
FPS = 60

while True:
    # Detects change of state to menu, config or instructions to play music
    if game_state in ("menu", "config", "instructions") and previous_state not in ("menu", "config", "instructions"):
        Menu_sound.play(loops=-1)  # just one loop

    # Detects game state change to stop menu music
    if game_state == "play" and previous_state != "play":
        Menu_sound.stop()
        GameStart_sound.play()

    previous_state = game_state  # Actualiza estado anterior

    if game_state == "menu":
        MainMenu.draw_menu(screen, selected_option)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 3
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 3
                if event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        game_state = "play"
                        Menu_sound.stop()
                        GameStart_sound.play()
                    elif selected_option == 1:
                        game_state = "config"
                    elif selected_option == 2:
                        game_state = "instructions"

    elif game_state == "instructions":
        MainMenu.draw_instructions(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "menu"

    elif game_state == "config":
        MainMenu.draw_config(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "menu"

    elif game_state == "play":
        result = PongGame.run_pong(screen)
        if result == "menu":
            game_state = "menu"
        elif result == "quit":
            pygame.quit(); sys.exit()

    clock.tick(FPS)
