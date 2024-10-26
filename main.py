import pygame
pygame.init()

distance = 50
screen_size = 500
num_blocks = screen_size // distance

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("snake")

snake = [[num_blocks // 2, num_blocks // 2]]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, (255, 255, 255),
                         (x * distance, y * distance, distance, distance))

    pygame.display.flip()

pygame.quit()
