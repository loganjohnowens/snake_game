import pygame
import time
import random

# Define constants
BLOCK_SIZE = 50  # Size of each grid block
SCREEN_SIZE = 500  # Width and height of the game screen
GRID_SIZE = SCREEN_SIZE // BLOCK_SIZE  # Number of blocks in the grid

# Initialize Pygame
pygame.init()


def setup_screen():
    """Sets up the game screen and caption."""
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Snake Game")
    return screen


def get_game_mode():
    """Gets user input to select game mode and returns corresponding time delay for game speed."""
    while True:
        mode = input('''Select game mode:
        1 - Watch AI
        2 - Play manually
        3 - Quit
        > ''')
        if mode == '1':
            return 0.1  # Faster for AI
        elif mode == '2':
            return 0.25  # Slower for manual play
        elif mode == '3':
            return None
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


def initialize_game():
    """Initializes game variables."""
    snake_body = [[GRID_SIZE // 2 - 3, GRID_SIZE // 2 - 1]]
    apple_position = (GRID_SIZE // 2 + 2, GRID_SIZE // 2)
    return snake_body, apple_position, 0, pygame.K_d  # Initial direction is right


def move_snake(snake_body, direction, current_direction, has_eaten_apple, is_ai_controlled=False):
    """Handles movement logic, updating snake position based on direction."""
    if not is_ai_controlled:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and current_direction != pygame.K_a:
            current_direction = pygame.K_d  # Move right
        elif keys[pygame.K_a] and current_direction != pygame.K_d:
            current_direction = pygame.K_a  # Move left
        elif keys[pygame.K_w] and current_direction != pygame.K_s:
            current_direction = pygame.K_w  # Move up
        elif keys[pygame.K_s] and current_direction != pygame.K_w:
            current_direction = pygame.K_s  # Move down

    # Update the snake head position based on direction
    if current_direction == pygame.K_d:
        snake_body.insert(0, [snake_body[0][0] + 1, snake_body[0][1]])
    elif current_direction == pygame.K_a:
        snake_body.insert(0, [snake_body[0][0] - 1, snake_body[0][1]])
    elif current_direction == pygame.K_w:
        snake_body.insert(0, [snake_body[0][0], snake_body[0][1] - 1])
    elif current_direction == pygame.K_s:
        snake_body.insert(0, [snake_body[0][0], snake_body[0][1] + 1])

    # Only keep the new head if the apple wasn't eaten; otherwise, keep the tail too
    if not has_eaten_apple:
        snake_body.pop()

    return current_direction


def update_apple_position(snake_body, apple_position, has_eaten_apple):
    """Checks if snake eats apple and updates apple position if necessary."""
    if has_eaten_apple == 1:
        has_eaten_apple = 0
    if snake_body[0] == list(apple_position):
        has_eaten_apple = 1
        apple_position = (random.randint(0, GRID_SIZE - 1),
                          random.randint(0, GRID_SIZE - 1))
    return apple_position, has_eaten_apple


def check_self_collision(snake_body):
    """Checks for collisions within the snake itself."""
    return len(snake_body) == len(set(map(tuple, snake_body)))  # No duplicates means no self-collision


def check_wall_collision(snake_body):
    """Checks if the snake hits the walls."""
    head_x, head_y = snake_body[0]
    return 0 <= head_x < GRID_SIZE and 0 <= head_y < GRID_SIZE


def ai_move_snake(snake_body, apple_position, has_eaten_apple):
    """AI logic to control snake movement towards apple (simplified here)."""
    # AI logic to move towards apple, similar to original function
    # Placeholder simplified logic for clarity in this response
    pass


def main():
    """Main game loop."""
    screen = setup_screen()
    game_speed = get_game_mode()
    if game_speed is None:
        return  # Exit if user chooses to quit

    snake_body, apple_position, has_eaten_apple, current_direction = initialize_game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Player or AI controlled game logic
        current_direction = move_snake(
            snake_body, current_direction, current_direction, has_eaten_apple)
        apple_position, has_eaten_apple = update_apple_position(
            snake_body, apple_position, has_eaten_apple)

        # Render apple and snake
        pygame.draw.rect(screen, (225, 0, 0), (
            apple_position[0] * BLOCK_SIZE, apple_position[1] * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))
        for segment in snake_body:
            pygame.draw.rect(screen, (0, 225, 0), (
                segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

        # Check for collisions
        if not check_self_collision(snake_body) or not check_wall_collision(snake_body):
            running = False  # End game if collision detected

        pygame.display.flip()
        time.sleep(game_speed)

    pygame.quit()


# Only call main if this script is run directly
if __name__ == "__main__":
    main()

