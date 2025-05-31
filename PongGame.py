import pygame
import random
from Config import width, height, blue, black, selection_color, font, small_font, controls

def run_pong(screen):
    #Elements settings
    paddle_Width, paddle_Height, paddle_Speed = 10, 100, 7
    ball_Size = 15
    target_score = 5
    score_font = pygame.font.Font(None, 74)
    win_font = pygame.font.Font(None, 64)

    player1_score = 0
    player2_score = 0
    game_over = False
    winner = ""

    # Entities
    player1 = pygame.Rect(50, height // 2 - paddle_Height // 2, paddle_Width, paddle_Height) #Place player 1 on left center
    player2 = pygame.Rect(width - 60, height // 2 - paddle_Height // 2, paddle_Width, paddle_Height) #Place player 2 on right center
    ball = pygame.Rect(width // 2 - ball_Size // 2, height // 2 - ball_Size // 2, ball_Size, ball_Size) #Create ball  
    ball_Speed_X = 5 * random.choice((1, -1))
    ball_Speed_Y  = 5 * random.choice((1, -1))

    clock = pygame.time.Clock() #Control FPS
    
    #Load sound effects
    GameStart_sound = pygame.mixer.Sound("SoundEffects/GameStart.mp3")
    GameOver_sound = pygame.mixer.Sound("SoundEffects/GameOver.mp3")
    Collision_sound = pygame.mixer.Sound("SoundEffects/Collision.mp3")
    ScoreSound = pygame.mixer.Sound("SoundEffects/Score.mp3")

    # Reset ball function after scoring or reset
    def reset_ball():
        nonlocal ball_Speed_X, ball_Speed_Y
        ball.center = (width // 2, height // 2)
        ball_Speed_X *= random.choice((1, -1))
        ball_Speed_Y *= random.choice((1, -1))

    # Draw elements as paddlets and ball 
    def draw_elements(screen):
        screen.fill(blue)

        # Paddles and ball
        pygame.draw.rect(screen, black, player1)
        pygame.draw.rect(screen, black, player2)
        pygame.draw.ellipse(screen, black, ball)
        pygame.draw.aaline(screen, black, (width // 2, 0), (width // 2, height))

        # Scoreboard
        p1_text = score_font.render(f"{player1_score}", True, black)
        p2_text = score_font.render(f"{player2_score}", True, black)
        screen.blit(p1_text, (width // 4 - p1_text.get_width() // 2, 20))
        screen.blit(p2_text, (width * 3 // 4 - p2_text.get_width() // 2, 20))

        # Winner
        if game_over:
            win_text = win_font.render(f"{winner} wins!", True, black)
            screen.blit(win_text, (width // 2 - win_text.get_width() // 2, height // 2 - 32))
            restart_text = small_font.render("Press R to play again", True, black)
            menu_text = small_font.render("Press ESC to return to menu", True, black)
            screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 20))
            screen.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 + 50))
        pygame.display.flip()    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return "play"
    
        # Paddles movement
        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_w] and player1.top > 0: #Paddle of player 1 goes up if W key is pressed
                player1.y -= paddle_Speed
            if keys[pygame.K_s] and player1.bottom < height: #Paddle of P1 goes down if S key is pressed
                player1.y += paddle_Speed
            if keys[pygame.K_UP] and player2.top > 0: #Paddle of P2 goes down if up arrow key is pressed
                player2.y -= paddle_Speed
            if keys[pygame.K_DOWN] and player2.bottom < height: #Paddle of P2 goes down if down arrow key is pressed
                player2.y += paddle_Speed

            # Ball movement
            ball.x += ball_Speed_X
            ball.y += ball_Speed_Y

            # Top walls collisions
            if ball.top <= 0 or ball.bottom >= height:
                ball_Speed_Y *= -1
                Collision_sound.play()

            # Paddles collisions
            if ball.colliderect(player1) or ball.colliderect(player2):
                Collision_sound.play()
                ball_Speed_X *= -1
                ball_Speed_Y += random.choice([-1, 1])

            # Point for P2
            if ball.left <= 0:
                player2_score += 1
                ScoreSound.play()
                reset_ball()

            # Point for P1
            if ball.right >= width:
                player1_score += 1
                ScoreSound.play()
                reset_ball()

            # Set winner
            if player1_score >= target_score:
                game_over = True
                winner = "Player 1"
                GameOver_sound.play()

            elif player2_score >= target_score:
                game_over = True
                winner = "Player 2"
                GameOver_sound.play()

        # Reset game with R key
        if game_over and keys[pygame.K_r]:
            GameStart_sound.play()
            player1_score = 0
            player2_score = 0
            game_over = False
            winner = ""
            reset_ball()
            

        draw_elements(screen)
        clock.tick(60)