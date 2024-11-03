import pygame
import time
import random
pygame.init()

distance = 50
screen_size = 500
num_blocks = screen_size // distance

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Snake Game")

snake = [[num_blocks // 2 - 1, num_blocks // 2]]
apple_get = 0
apple_loc_x = (num_blocks // 2 + 2)
apple_loc_y = (num_blocks // 2)
move_state = [False] * 323
move_state[pygame.K_d] = True
diecoin = pygame.K_d


def move(second_loop, diecoin):
    global apple_get

    if not second_loop:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and diecoin != pygame.K_a:
            diecoin = pygame.K_d
        elif keys[pygame.K_a] and diecoin != pygame.K_d:
            diecoin = pygame.K_a
        elif keys[pygame.K_w] and diecoin != pygame.K_s:
            diecoin = pygame.K_w
        elif keys[pygame.K_s] and diecoin != pygame.K_w:
            diecoin = pygame.K_s

    if diecoin == pygame.K_d:
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif diecoin == pygame.K_a:
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif diecoin == pygame.K_w:
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    elif diecoin == pygame.K_s:
        snake.insert(0, [snake[0][0], snake[0][1] + 1])

    if apple_get != 1:
        snake.pop()

    return diecoin


def apple():
    global apple_get
    global apple_loc_x
    global apple_loc_y
    if apple_get == 1:
        apple_loc_x = random.randint(0, num_blocks)
        apple_loc_y = random.randint(0, num_blocks)
        apple_get = 0
    pygame.draw.rect(screen, (225, 0, 0),
                     (apple_loc_x * distance, apple_loc_y * distance, distance, distance))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    diecoin = move(False, diecoin)

    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, (0, 225, 0), (x * distance,
                         y * distance, distance, distance))
    apple()
    pygame.display.flip()
    time.sleep(0.25)

pygame.quit()
