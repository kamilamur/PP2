import pygame
import random
import sys
pygame.init()
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Arial', 24)

INITIAL_SPEED = 10
LEVEL_UP_FOOD = 4  

def create_walls():
    walls = []
    for x in range(GRID_WIDTH):
        walls.append((x, 0))
        walls.append((x, GRID_HEIGHT - 1))
    for y in range(GRID_HEIGHT):
        walls.append((0, y))
        walls.append((GRID_WIDTH - 1, y))
    for x in range(10, 20):
        walls.append((x, 8))
    return walls

def generate_food(snake, walls):
    while True:
        pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
        if pos not in snake and pos not in walls:
            return pos

def draw_game(snake, food, walls, score, level):
    win.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(win, GRAY, (wall[0]*CELL_SIZE, wall[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(win, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    win.blit(text, (10, 10))
    pygame.display.update()

def show_game_over(score):
    win.fill(BLACK)
    big_font = pygame.font.SysFont('Arial', 48)
    text1 = big_font.render("GAME OVER", True, RED)
    text2 = font.render(f"Your score: {score}", True, WHITE)
    text3 = font.render("Press any key to exit...", True, WHITE)
    win.blit(text1, (WIDTH//2 - text1.get_width()//2, HEIGHT//2 - 60))
    win.blit(text2, (WIDTH//2 - text2.get_width()//2, HEIGHT//2))
    win.blit(text3, (WIDTH//2 - text3.get_width()//2, HEIGHT//2 + 40))
    pygame.display.update()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
def main():
    clock = pygame.time.Clock()
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    score = 0
    level = 1
    speed = INITIAL_SPEED
    walls = create_walls()
    food = generate_food(snake, walls)
    running = True

    while running:
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 1):
            direction = (0, -1)
        elif keys[pygame.K_DOWN] and direction != (0, -1):
            direction = (0, 1)
        elif keys[pygame.K_LEFT] and direction != (1, 0):
            direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and direction != (-1, 0):
            direction = (1, 0)

        # Новая голова змеи
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (
            head in snake or
            head in walls or
            head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT
        ):
            show_game_over(score)
            running = False
            continue
        snake.insert(0, head)
        if head == food:
            score += 1
            if score % LEVEL_UP_FOOD == 0:
                level += 1
                speed += 2
            food = generate_food(snake, walls)
        else:
            snake.pop()
        draw_game(snake, food, walls, score, level)

    pygame.quit()
if __name__ == "__main__":
    main()