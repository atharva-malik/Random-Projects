import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width, paddle_height = 20, 100

# Ball dimensions
ball_size = 20

# Paddle speeds
paddle_speed = 5

# Ball speed
ball_speed_x = 5
ball_speed_y = 5

# Score
score_a = 0
score_b = 0

# Create paddles
paddle_a = pygame.Rect(20, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_b = pygame.Rect(width - paddle_width - 20, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Create ball
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.y -= paddle_speed
    if keys[pygame.K_s]:
        paddle_a.y += paddle_speed
    if keys[pygame.K_UP]:
        paddle_b.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle_b.y += paddle_speed

    # Keep paddles within screen
    paddle_a.clamp_ip(pygame.Rect(0, 0, width, height))
    paddle_b.clamp_ip(pygame.Rect(0, 0, width, height))

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0:
        score_b += 1
        ball.center = (width // 2, height // 2)
        ball_speed_x *= -1
        ball_speed_y *= random.choice([-1, 1])
    if ball.right >= width:
        score_a += 1
        ball.center = (width // 2, height // 2)
        ball_speed_x *= -1
        ball_speed_y *= random.choice([-1, 1])

    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle_a)
    pygame.draw.rect(screen, white, paddle_b)
    pygame.draw.ellipse(screen, white, ball)

    # Draw scores
    font = pygame.font.Font(None, 36)
    text_a = font.render(str(score_a), True, white)
    text_b = font.render(str(score_b), True, white)
    screen.blit(text_a, (width // 4, 10))
    screen.blit(text_b, (width * 3 // 4 - text_b.get_width(), 10))

    pygame.display.flip()

pygame.quit()
