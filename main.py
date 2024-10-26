import pygame
import time
pygame.init()

distance = 50
screen_size = 500
num_blocks = screen_size // distance

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("snake")

snake = [[num_blocks // 2 - 1, num_blocks // 2]]


def move():
    diectoin = pygame.key.get_pressed()
    if diectoin[pygame.K_d]:
        snake.insert(0, [snake[0][0]+1, snake[0][0]])


running = True
while running:
    screen.fill((0, 0, 0))
    move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for segment in snake:
        x = segment[0]
        y = segment[1]
        pygame.draw.rect(screen, (0, 225, 0),
                         (x * distance, y * distance, distance, distance))

    pygame.display.flip()
    time.sleep(1)
pygame.quit()
