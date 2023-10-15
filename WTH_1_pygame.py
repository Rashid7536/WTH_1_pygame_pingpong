import pygame
pygame.init()
# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

# Paddle positions
player_y = (HEIGHT - PADDLE_HEIGHT) // 2
opponent_y = (HEIGHT - PADDLE_HEIGHT) // 2


# Ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 7
ball_speed_y = 7

# Scores
player_score = 0
opponent_score = 0

#GAME LOOP

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here
    # Inside the game loop:

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and opponent_y > 0:
        opponent_y -= 5
    if keys[pygame.K_DOWN] and opponent_y < HEIGHT - PADDLE_HEIGHT:
        opponent_y += 5
    if keys[pygame.K_w] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_s] and player_y < HEIGHT - PADDLE_HEIGHT:
        player_y += 5

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (
        ball_x <= 50 + PADDLE_WIDTH
        and player_y <= ball_y <= player_y + PADDLE_HEIGHT
    ) or (
        ball_x >= WIDTH - 50 - PADDLE_WIDTH - BALL_SIZE
        and opponent_y <= ball_y <= opponent_y + PADDLE_HEIGHT
    ):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds (scoring)
    if ball_x < 0:
        opponent_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = 1
        ball_speed_y = 1
    if ball_x > WIDTH:
        player_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = 1
        ball_speed_y = 1

    # Game over condition
    if player_score >= 5 or opponent_score >= 5:
        # Display the winner and end the game
        winner = "Player" if player_score >= 5 else "Opponent"
        font = pygame.font.Font(None, 72)
        winner_text = font.render(f"{winner} wins!", True, WHITE)
        screen.blit(winner_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(2000)  # Display winner for 2 seconds
        running = False


    # Clear the screen
    screen.fill((80, 100, 100))

    # Draw paddles, ball, and scores here
    # Inside the game loop:

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (50, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Player paddle
    pygame.draw.rect(screen, WHITE, (WIDTH - 50 - PADDLE_WIDTH, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Opponent paddle

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE)

    # Draw scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"Player 1: {player_score}", True, WHITE)
    opponent_text = font.render(f"Player 2: {opponent_score}", True, WHITE)
    screen.blit(player_text, (20, 20))
    screen.blit(opponent_text, (WIDTH - 200, 20))

    # Update the display
    pygame.display.flip()

pygame.quit()
