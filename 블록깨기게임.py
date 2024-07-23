import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('블럭 깨기 게임')

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
pink = (255, 192, 203)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_speed = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 20, paddle_width, paddle_height)

# 공 설정
ball_size = 10
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed = [5, -5]

# 블럭 설정
block_width = 60
block_height = 20
blocks = [pygame.Rect(col * (block_width + 10) + 35, row * (block_height + 10) + 35, block_width, block_height) for row in range(5) for col in range(10)]

# FPS 설정
fps = 30
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # 공 이동
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # 공이 벽에 부딪힐 때
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= screen_height:
        print("Game Over")
        running = False

    # 공이 패들에 부딪힐 때
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 공이 블럭에 부딪힐 때
    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed[1] = -ball_speed[1]
            blocks.remove(block)
            break

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, blue, paddle)
    pygame.draw.ellipse(screen, white, ball)
    for block in blocks:
        pygame.draw.rect(screen, pink, block)
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
0