import pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RADIUS = 25
x, y = WIDTH // 2, HEIGHT // 2
SPEED = 20  

running = True
while running:
    pygame.time.delay(50)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - RADIUS - SPEED >= 0:
        y -= SPEED
    if keys[pygame.K_DOWN] and y + RADIUS + SPEED <= HEIGHT:
        y += SPEED
    if keys[pygame.K_LEFT] and x - RADIUS - SPEED >= 0:
        x -= SPEED
    if keys[pygame.K_RIGHT] and x + RADIUS + SPEED <= WIDTH:
        x += SPEED

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RADIUS)
    pygame.display.flip()
pygame.quit()