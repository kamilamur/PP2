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
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Arial', 24)

INITIAL_SPEED = 10
LEVEL_UP_FOOD = 4
FOOD_LIFETIME = 5000

class Food:
    def __init__(self, snake, walls):
        self.position = None
        self.weight = 1
        self.spawn_time = 0
        self.spawn(snake, walls)

    def spawn(self, snake, walls):
        while True:
            pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
            if pos not in snake and pos not in walls:
                self.position = pos
                self.weight = random.choice([1, 2, 3])
                self.spawn_time = pygame.time.get_ticks()
                break
    def draw(self, surface):
        color = {1: RED, 2: ORANGE, 3: YELLOW}[self.weight]
        pygame.draw.rect(surface, color, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        weight_text = font.render(str(self.weight), True, BLACK)
        text_rect = weight_text.get_rect(center=(
            self.position[0]*CELL_SIZE + CELL_SIZE // 2,
            self.position[1]*CELL_SIZE + CELL_SIZE // 2
        ))
        surface.blit(weight_text, text_rect)
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

def draw_game(snake, food, walls, score, level):
    win.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(win, GRAY, (wall[0]*CELL_SIZE, wall[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    food.draw(win)
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    win.blit(text, (10, 10))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    snake = [(5, 5)]
    direction = (1, 0)
    walls = create_walls()
    food = Food(snake, walls)
    score = 0
    level = 1
    speed = INITIAL_SPEED

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

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if new_head in snake or new_head in walls:
            running = False
            continue
        snake.insert(0, new_head)

        if new_head == food.position:
            score += food.weight
            if score // LEVEL_UP_FOOD + 1 > level:
                level += 1
                speed += 1
            food.spawn(snake, walls)
        else:
            snake.pop()
        if pygame.time.get_ticks() - food.spawn_time > FOOD_LIFETIME:
            food.spawn(snake, walls)
        draw_game(snake, food, walls, score, level)
    game_over = True
    while game_over:
        win.fill(BLACK)
        over_text = font.render("Game Over", True, RED)
        exit_text = font.render("Press any key to exit", True, WHITE)
        score_text = font.render(f"Your score: {score}", True, GREEN)
        win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 60)) #рисует гейм овер
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 20))#рисует строку с счетом
        win.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 20))#рисует доп надпись выход
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
if __name__ == "__main__":
    main()