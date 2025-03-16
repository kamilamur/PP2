import pygame
import time
import math

pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


clock_face = pygame.image.load("IMG_9340.png")  
minute_hand = pygame.image.load("IMG_9342.png")  
second_hand = pygame.image.load("IMG_9341.png")  


clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (150, 150))
second_hand = pygame.transform.scale(second_hand, (180, 180))


center = (WIDTH // 2, HEIGHT // 2)


running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_face, (0, 0))  
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    
    minute_angle = -(minutes * 6) 
    second_angle = -(seconds * 6)  
    
    
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)
    
    
    minute_rect = rotated_minute_hand.get_rect(center=center)
    second_rect = rotated_second_hand.get_rect(center=center)
    

    screen.blit(rotated_minute_hand, minute_rect.topleft)
    screen.blit(rotated_second_hand, second_rect.topleft)
    
    
    pygame.display.flip()
    pygame.time.delay(1000)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()