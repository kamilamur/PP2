import psycopg2
import pygame
import time
import random
from datetime import datetime

def connect():
    return psycopg2.connect(
        dbname="postgres",     
        user="postgres",       
        password="KamaMur_205",  
        host="localhost",
        port="5432"
    )
def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

def get_user_level(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1;", (user_id,))
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result[0] if result else 1

def save_game_state(user_id, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s);",
        (user_id, score, level)
    )
    conn.commit()
    cur.close()
    conn.close()
create_tables()
username = input("Please, enter your name: ")
user_id = get_or_create_user(username)
level = get_user_level(user_id)

print(f"Welcome to the game, {username}! Your level is: {level}")

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
time.sleep(1)  

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
food_timer = 100
score = 0
speed = 10

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
        break
    
    snake.insert(0, new_head)
    
    if new_head[0] < food[0] + food_size and new_head[0] + CELL_SIZE > food[0] and \
       new_head[1] < food[1] + food_size and new_head[1] + CELL_SIZE > food[1]:
        score += food_size // CELL_SIZE
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
        food_timer = 100
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    
    food_timer -= 1
    if food_timer <= 0:
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
        food_timer = 100
    
    pygame.draw.rect(screen, RED, (food[0], food[1], food_size, food_size))
    
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))
    pygame.display.update()
    clock.tick(speed)
save_game_state(user_id, score, level)
print(f"Game is finished. Score: {score}, Level: {level} saved.")
pygame.quit()