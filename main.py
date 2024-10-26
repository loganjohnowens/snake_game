import pygame
screen_1 = 0
distance = 50
screen_size = 500
num_blocks = screen_size/distance
pygame.init()
screen = pygame.display.set_mode((screen_size, screen_size))
h =input ('is the display here')
pygame.display.set_caption("snake")
screen.fill((0, 0, 0))
snake = [[num_blocks / 2 ,num_blocks / 2]]
while True:
    for j in range(1, (len(snake)-1)):
        for i in snake[j][0]:
           pygame.draw.rect(screen, (255, 255, 255), (distance*i, distance*i, distance, distance))
        for i in snake[j][1]:
            pygame.draw.rect(screen, (255, 255, 255), (distance*i, distance*i, distance, distance))
        print('hi')
    pygame.display.flip()
    
