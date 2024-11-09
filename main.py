import pygame
import time
import random
pygame.init()

distance = 50
screen_size = 500
num_blocks = screen_size // distance

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Snake Game")

snake = [[num_blocks // 2 - 3, num_blocks // 2 - 1]]
apple_get = 0
apple_loc_x = (num_blocks // 2 + 2)
apple_loc_y = (num_blocks // 2)
move_state = [False] * 323
move_state[pygame.K_d] = True
diecoin = pygame.K_d
mode = input('''what mode would you like to play:
        to watch ai press 1
        to play press 2
        >''')


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
    global snake
    if apple_get == 1:
        apple_get = 0
    if snake[0] == [apple_loc_x, apple_loc_y]:
        apple_get = 1
        apple_loc_x = random.randint(0, num_blocks - 1)
        apple_loc_y = random.randint(0, num_blocks - 1)


def snake_run_in(head):
    global snake
    number = 0
    for i in snake:
        if i == head and number == 1:
            return False
        number = 1
    return True


def walls(snake):
    global num_blocks
    if snake[0][0] < 0:
        return False
    if snake[0][1] < 0:
        return False
    if snake[0][0] > num_blocks - 1:
        return False
    if snake[0][1] > num_blocks - 1:
        return False
    return True


def bot_move():
    global snake
    global apple_loc_y
    global apple_loc_x
    global apple_get
    print(apple_loc_x, apple_loc_y)
    new_potential_loc = []
    wall_new_potential_loc = []
    potential_loc = [[snake[0][0] + 1, snake[0][1]], [snake[0][0] - 1, snake[0][1]],
                     [snake[0][0], snake[0][1] + 1], [snake[0][0], snake[0][1] - 1]]
    for i in potential_loc:
        skip = [False, False, False, False]
        check = []
        check.append(i)
        check.append(['why are you reading this'])
        wall_new_potential_loc.append(walls(check))
        new_potential_loc.append(snake_run_in(i))
    if wall_new_potential_loc[0] is False:
        new_potential_loc[0] = False
    if wall_new_potential_loc[1] is False:
        new_potential_loc[1] = False
    if wall_new_potential_loc[2] is False:
        new_potential_loc[2] = False
    if wall_new_potential_loc[3] is False:
        new_potential_loc[3] = False
    print(f'before {potential_loc}')
    best_number = 0
    done = 0
    super_done = 0
    if potential_loc[0][0] == apple_loc_x and apple_loc_y == potential_loc[0][1] and new_potential_loc[0] is True:
        super_done = 1
        best_number = 0
        done = 1
    if potential_loc[1][0] == apple_loc_x and apple_loc_y == potential_loc[1][1] and new_potential_loc[1] is True:
        super_done = 1
        best_number = 1
        done = 1
    if potential_loc[2][0] == apple_loc_x and apple_loc_y == potential_loc[2][1] and new_potential_loc[2] is True:
        super_done = 1
        best_number = 2
        done = 1
    if potential_loc[3][0] == apple_loc_x and apple_loc_y == potential_loc[3][1] and new_potential_loc[3] is True:
        super_done = 1
        best_number = 3
        done = 1
    number = -1
    if super_done != 1:
        for i in potential_loc:
            number += 1
            if number == 0 and i[0] == apple_loc_x or number == 1 and i[0] == apple_loc_x:
                skip[number] = True
                potential_loc[number] = 0
            if number == 2 and i[1] == apple_loc_y or number == 3 and i[1] == apple_loc_y:
                skip[number] = True
                potential_loc[number] = 0
    if skip[0] is not True and done != 1 and potential_loc[0][0] < apple_loc_x:
        potential_loc[0] = apple_loc_x - potential_loc[0][0]
        done = 1
    if skip[0] is not True and done != 1 and potential_loc[0][0] > apple_loc_x:
        potential_loc[0] = potential_loc[0][0] - apple_loc_x
    if super_done != 1:
        done = 0
    if skip[1] is not True and done != 1 and potential_loc[1][0] < apple_loc_x:
        potential_loc[1] = apple_loc_x - potential_loc[1][0]
        done = 1
    if skip[1] is not True and done != 1 and potential_loc[1][0] > apple_loc_x:
        potential_loc[1] = potential_loc[1][0] - apple_loc_x
    if super_done != 1:
        done = 0
    if skip[2] is not True and done != 1 and potential_loc[2][1] < apple_loc_y:
        potential_loc[2] = apple_loc_y - potential_loc[2][1]
        done = 1
    if skip[2] is not True and done != 1 and potential_loc[2][1] > apple_loc_y:
        potential_loc[2] = potential_loc[2][1] - apple_loc_y
    if super_done != 1:
        done = 0
    if skip[3] is not True and done != 1 and potential_loc[3][1] < apple_loc_y:
        potential_loc[3] = apple_loc_y - potential_loc[3][1]
        done = 1
    if skip[3] is not True and done != 1 and potential_loc[3][1] > apple_loc_y:
        potential_loc[3] = potential_loc[3][1] - apple_loc_y
    print(f'after trans pot {potential_loc}')
    print(f'new {new_potential_loc}')
    best = 1000
    number = -1
    if super_done != 1:
        for i in potential_loc:
            number += 1
            if i < best and new_potential_loc[number] is True:
                if number < 2 and snake[0][0] != apple_loc_x:
                    best = i
                    best_number = number
                if number > 1 and snake[0][1] != apple_loc_y:
                    best = i
                    best_number = number
                if number < 2 and new_potential_loc[2] is False and new_potential_loc[3] is False:
                    best = i
                    best_number = number
                if number > 1 and new_potential_loc[0] is False and new_potential_loc[1] is False:
                    best = i
                    best_number = number

    if best_number == 0:
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    if best_number == 1:
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    if best_number == 2:
        snake.insert(0, [snake[0][0], snake[0][1] + 1])
    if best_number == 3:
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    if apple_get == 0:
        snake.pop()
    super_done = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if mode == '2':
        diecoin = move(False, diecoin)
        apple()
    pygame.draw.rect(screen, (225, 0, 0),
                     (apple_loc_x * distance, apple_loc_y * distance, distance - 1, distance - 1))
    if mode == '1':
        bot_move()
        apple()
    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, (0, 225, 0), (x * distance,
                         y * distance, distance - 1, distance - 1))
    running_one = snake_run_in(snake[0])
    running = walls(snake)
    if running_one is False:
        running = False
    pygame.display.flip()
    time.sleep(0.1)
pygame.quit()
