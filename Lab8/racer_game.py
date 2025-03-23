import pygame
import random
pygame.init()

WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

clock = pygame.time.Clock()
FPS = 60
player_img = pygame.image.load("car.png")
enemy_img = pygame.image.load("enemy.png")
coin_img = pygame.image.load("coin.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 120)
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 40:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 40:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), -100)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(50, WIDTH - 50), -100)
            self.speed = random.randint(3, 7)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), -50)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)

coin_count = 0
font = pygame.font.SysFont("Arial", 24)

running = True
coin_timer = 0

while running:
    clock.tick(FPS)
    win.fill(GRAY)

    coin_timer += 1
    if coin_timer > 90:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)
        coin_timer = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    collected = pygame.sprite.spritecollide(player, coins, True)
    coin_count += len(collected)

    if pygame.sprite.spritecollideany(player, enemies):
        running = False

    all_sprites.draw(win)

    text = font.render(f"Coins: {coin_count}", True, WHITE)
    win.blit(text, (WIDTH - 120, 10))
    pygame.display.update()
pygame.quit()