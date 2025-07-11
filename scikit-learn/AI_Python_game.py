import pygame
import random
#THIS IS FROM CHATGPT
# Initialize
pygame.init()
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Snake Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake & Food Setup
snake = [(5, 5)]
direction = (1, 0)
food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))

def draw_snake():
    for seg in snake:
        pygame.draw.rect(screen, GREEN, (seg[0]*CELL_SIZE, seg[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_snake():
    global food
    head_x, head_y = snake[0]

    # Simple AI: move toward the food
    if food[0] > head_x:
        new_dir = (1, 0)
    elif food[0] < head_x:
        new_dir = (-1, 0)
    elif food[1] > head_y:
        new_dir = (0, 1)
    else:
        new_dir = (0, -1)

    new_head = (head_x + new_dir[0], head_y + new_dir[1])

    # Check for collisions
    if (new_head in snake or
        not 0 <= new_head[0] < WIDTH // CELL_SIZE or
        not 0 <= new_head[1] < HEIGHT // CELL_SIZE):
        return False  # Game over

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))
    else:
        snake.pop()

    return True

# Game Loop
running = True
while running:
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    pygame.display.flip()

    if not move_snake():
        print("Game Over")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(10)

pygame.quit()
