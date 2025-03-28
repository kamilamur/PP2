import pygame
import sys
import math
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
shape_start = None

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
    "eraser": pygame.Rect(410, 10, 60, 30),
    "square": pygame.Rect(480, 10, 60, 30),
    "right": pygame.Rect(550, 10, 60, 30),
    "equilater": pygame.Rect(620, 10, 60, 30),
    "rhombus": pygame.Rect(690, 10, 60, 30),
}
#добавляем панель инструментов и цветов
def draw_ui():
    for name, rect in color_buttons.items():
        pygame.draw.rect(screen, eval(name.upper()), rect)
        if color == eval(name.upper()):
            pygame.draw.rect(screen, BLACK, rect, 2)
    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        font = pygame.font.SysFont(None, 20)
        text = font.render(name, True, BLACK)
        screen.blit(text, (rect.x + 3, rect.y + 5))
#рисование фигуры
def draw_shape(tool, start, end):
    if not start or not end:
        return
    if tool == "rect":
        x, y = start
        w = end[0] - x
        h = end[1] - y
        pygame.draw.rect(screen, color, (x, y, w, h), 2)
    elif tool == "circle":
        center = ((start[0]+end[0])//2, (start[1]+end[1])//2)
        radius = max(abs(end[0] - start[0]) // 2, abs(end[1] - start[1]) // 2)
        pygame.draw.circle(screen, color, center, radius, 2)

    elif tool == "square":
        x, y = start
        side = min(abs(end[0] - x), abs(end[1] - y))
        pygame.draw.rect(screen, color, (x, y, side, side), 2)

    elif tool == "right_triangle":
        x1, y1 = start
        x2, y2 = end
        points = [(x1, y1), (x2, y2), (x1, y2)]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "equilateral_triangle":
        x1, y1 = start
        x2, y2 = end
        side = abs(x2 - x1)
        height = side * (3**0.5) / 2
        if y2 < y1:
            height = -height
        points = [(x1, y1), (x1 + side, y1), (x1 + side / 2, y1 + height)]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "rhombus":
        x1, y1 = start
        x2, y2 = end
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
        pygame.draw.polygon(screen, color, points, 2)
running = True
while running:
    clock.tick(60)
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for name, rect in color_buttons.items():
                if rect.collidepoint(pos):
                    color = eval(name.upper())
            for name, rect in tool_buttons.items():
                if rect.collidepoint(pos):
                    tool = name
            drawing = True
            shape_start = pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and tool in ["rect", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
                draw_shape(tool, shape_start, pygame.mouse.get_pos())
            drawing = False
            shape_start = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pen":
                pygame.draw.line(screen, color, last_pos, event.pos, radius)
            elif drawing and tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, radius)
            last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "square"
            elif event.key == pygame.K_2:
                tool = "right_triangle"
            elif event.key == pygame.K_3:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_4:
                tool = "rhombus"
    #обновление экрана
    pygame.display.flip()
pygame.quit()