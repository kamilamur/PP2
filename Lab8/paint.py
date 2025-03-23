import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Drawing App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

screen.fill(WHITE)
clock = pygame.time.Clock()
drawing = False
last_pos = None
color = BLACK
radius = 5
tool = "pen"  

color_buttons = {
    "black": pygame.Rect(10, 10, 30, 30),
    "red": pygame.Rect(50, 10, 30, 30),
    "green": pygame.Rect(90, 10, 30, 30),
    "blue": pygame.Rect(130, 10, 30, 30)
}
tool_buttons = {
    "pen": pygame.Rect(200, 10, 60, 30),
    "rect": pygame.Rect(270, 10, 60, 30),
    "circle": pygame.Rect(340, 10, 60, 30),
    "eraser": pygame.Rect(410, 10, 60, 30)
}
shape_start = None
def draw_ui():
    for name, rect in color_buttons.items():
        pygame.draw.rect(screen, eval(name.upper()), rect)
        if color == eval(name.upper()):
            pygame.draw.rect(screen, BLACK, rect, 2)

    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        tool_text = pygame.font.SysFont(None, 24).render(name, True, BLACK)
        screen.blit(tool_text, (rect.x + 5, rect.y + 5))

def draw_line(surf, color, start, end, radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(surf, color, (x, y), radius)

running = True
while running:
    clock.tick(60)
    draw_ui()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for name, rect in color_buttons.items():
                if rect.collidepoint(pos):
                    color = eval(name.upper())
                    tool = "pen"  
                    break
            for name, rect in tool_buttons.items():
                if rect.collidepoint(pos):
                    tool = name
                    break

            drawing = True
            last_pos = pos
            shape_start = pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = pygame.mouse.get_pos()
                if tool == "rect":
                    x, y = shape_start
                    w = end_pos[0] - x
                    h = end_pos[1] - y
                    pygame.draw.rect(screen, color, (x, y, w, h), 2)
                elif tool == "circle":
                    center = shape_start
                    radius_circle = int(((end_pos[0] - center[0]) ** 2 + (end_pos[1] - center[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, center, radius_circle, 2)
            drawing = False
            last_pos = None
            shape_start = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pen":
                mouse_pos = pygame.mouse.get_pos()
                draw_line(screen, color, last_pos, mouse_pos, radius)
                last_pos = mouse_pos
            elif drawing and tool == "eraser":
                mouse_pos = pygame.mouse.get_pos()
                draw_line(screen, WHITE, last_pos, mouse_pos, radius)
                last_pos = mouse_pos
pygame.quit()