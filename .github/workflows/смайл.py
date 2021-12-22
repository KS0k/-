import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.draw.rect(screen, WHITE, (-400, -400, 800, 800))
pygame.draw.circle(screen, YELLOW, (200, 200), 100)
pygame.draw.circle(screen, BLACK, (200, 200), 100, 1)
pygame.draw.circle(screen, RED, (150, 170), 20)
pygame.draw.circle(screen, BLACK, (150, 170), 20, 1)
pygame.draw.circle(screen, RED, (250, 170), 15)
pygame.draw.circle(screen, BLACK, (250, 170), 15, 1)
pygame.draw.circle(screen, BLACK, (150, 170), 10)
pygame.draw.circle(screen, BLACK, (250, 170), 7)
pygame.draw.rect(screen, BLACK, (150, 250, 100, 20))
pygame.draw.line(screen, BLACK, (110,120), (180, 161), 10) 
pygame.draw.line(screen, BLACK, (220, 160), (290, 132), 10)

pygame.display.update()
