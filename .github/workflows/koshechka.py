import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))


OLIVE = (128, 102, 0)
SaddleBrown = (85, 68, 0)
SkyBlue = (213, 255, 230)
LightSkyBlue = (135, 205, 222)
CHOCOLATE = (200, 113, 55)
BLACK = (0, 0, 0)
LightSalmon = (222, 170, 135)
GREEN = (136, 170, 0)
ROSE = (255, 204, 170)
BROWN = (127, 72, 35)
WHITE = (255, 255, 255)
GREY = (153, 153, 153)

#фон
rect(sc, OLIVE, (0, 400, 600, 400))
rect(sc, SaddleBrown, (0, 0, 600, 400))


#окно
rect(sc, SkyBlue, (320, 20, 270, 370))
rect(sc, LightSkyBlue, (335, 35, 110, 100))
rect(sc, LightSkyBlue, (470, 35, 105, 100))
rect(sc, LightSkyBlue, (335, 155, 110, 220))
rect(sc, LightSkyBlue, (470, 155, 105, 220))

#хвост
screen = pygame.Surface((200, 70))
screen.fill(OLIVE)
rect = (screen, OLIVE, (0, 0, 200, 70))
size = (0, 0, 200, 70)
ellipse(screen, CHOCOLATE, size)
ellipse(screen, BLACK, size, 1)
screen2 = pygame.transform.rotate(screen, 150)
sc.blit(screen2, (430, 460))


#туловище
ellipse(sc, CHOCOLATE, (90, 420, 400, 200))
ellipse(sc, BLACK, (90, 420, 400, 200), 1)


#передняя(скрытая) лапка
ellipse(sc, CHOCOLATE, (70, 510, 45, 80))
ellipse(sc, BLACK, (70, 510, 45, 80), 1)


#голова
circle(sc, CHOCOLATE, (110, 505), 70)
circle(sc, BLACK, (110, 505), 70, 1)
#уши
polygon(sc, CHOCOLATE, [(35, 440), (70, 453), (47, 485)])
polygon(sc, BLACK, [(35, 440), (70, 453), (47, 485)], 1)
polygon(sc, CHOCOLATE, [(140, 450), (175, 432), (165, 478)])
polygon(sc, BLACK, [(140, 450), (175, 432), (165, 478)], 1)
polygon(sc, LightSalmon, [(145, 451), (170, 438), (163, 472)])
polygon(sc, BLACK, [(145, 451), (170, 438), (163, 472)], 1)
polygon(sc, LightSalmon, [(40, 445), (65, 454), (49, 477)])
polygon(sc, BLACK, [(40, 445), (65, 454), (49, 477)], 1)
#глаза
ellipse(sc, GREEN, (65, 493, 33, 38))
ellipse(sc, BLACK, (65, 493, 33, 38), 1)
ellipse(sc, GREEN, (123, 493, 33, 38))
ellipse(sc, BLACK, (123, 493, 33, 38), 1)
#блики
screen = pygame.Surface((6, 15))
screen.fill(GREEN)
rect = (screen, GREEN, (0, 0, 6, 15))
size = (0, 0, 6, 15)
ellipse(screen, WHITE, size)
screen2 = pygame.transform.rotate(screen, 35)
sc.blit(screen2, (72, 497))
screen = pygame.Surface((6, 15))
screen.fill(GREEN)
rect = (screen, GREEN, (0, 0, 6, 15))
size = (0, 0, 6, 15)
ellipse(screen, WHITE, size)
screen2 = pygame.transform.rotate(screen, 35)
sc.blit(screen2, (131, 497))
#зрачки
ellipse(sc, BLACK, (142, 493, 5, 35))
ellipse(sc, BLACK, (83, 493, 5, 35))
#носик
polygon(sc, ROSE, [(105, 530), (117, 530), (111, 536)])
polygon(sc, BLACK, [(105, 530), (117, 530), (111, 536)], 1)
#рот
pi = 3.14
line(sc, BLACK, (111, 536), (111, 544))
arc(sc, BLACK, (111, 539, 15, 15), pi, pi * 2, 1)
arc(sc, BLACK, (98, 539, 15, 15), -pi, pi * (-2), 1)
#усы
arc(sc, BROWN, (10, 533, 80, 8), 0, pi * 0.96, 1)
arc(sc, BROWN, (10, 536, 80, 8), 0, pi * 0.96, 1)
arc(sc, BROWN, (10, 539, 80, 8), 0, pi * 0.96, 1)
arc(sc, BROWN, (130, 533, 80, 8), 0, pi * 0.96, 1)
arc(sc, BROWN, (130, 536, 80, 8), 0, pi * 0.96, 1)
arc(sc, BROWN, (130, 539, 80, 8), 0, pi * 0.96, 1)

#передняя лапка
ellipse(sc, CHOCOLATE, (115, 570, 80, 50))
ellipse(sc, BLACK, (115, 570, 80, 50), 1)


#ляшка
circle(sc, CHOCOLATE, (440, 565), 55)
circle(sc, BLACK, (440, 565), 55, 1)


#лапка задняя
ellipse(sc, CHOCOLATE, (470, 580, 40, 90))
ellipse(sc, BLACK, (470, 580, 40, 90), 1)

#клубок
circle(sc, GREY, (400, 720), 55)
circle(sc, BLACK, (400, 720), 55, 1)
screen = pygame.Surface((55, 55))
screen.fill(GREY)
arc(screen, BLACK, (25, 10, 55, 55), pi, -pi * 0.5, 1)
arc(screen, BLACK, (35, 10, 55, 55), pi, -pi * 0.5, 1)
arc(screen, BLACK, (40, 5, 55, 55), pi, -pi * 0.5, 1)
arc(screen, BLACK, (15, 0, 55, 55), 0, pi, 1)
arc(screen, BLACK, (15, 10, 55, 55), 0, pi, 1)
arc(screen, BLACK, (15, 20, 55, 55), 0, pi, 1)
screen2 = pygame.transform.rotate(screen, 290)
sc.blit(screen2, (362, 682))


#screen = pygame.Surface((40, 40))
#screen.fill(GREY)
#rect = (screen, GREY, (0, 0, 40, 40))
#arc(screen, BLACK, (0, 0, 40, 40), pi, -pi * 0.5, 1)
#screen2 = pygame.transform.rotate(screen, 290)
#sc.blit(screen2, (373, 717))

#screen = pygame.Surface((30, 30))
#screen.fill(GREY)
#rect = (screen, GREY, (0, 0, 30, 30))
#arc(screen, BLACK, (0, 0, 30, 30), pi, -pi * 0.5, 1)
#screen2 = pygame.transform.rotate(screen, 310)
#sc.blit(screen2, (386, 725))

#screen = pygame.Surface((40, 7))
#screen.fill(GREY)
#rect = (screen, GREY, (0, 0, 40, 7))
#arc(screen, BLACK, (0, 0, 40, 7), 0, pi * 0.96, 1)
#screen2 = pygame.transform.rotate(screen, 310)
#sc.blit(screen2, (408, 683))

#screen = pygame.Surface((50, 10))
#screen.fill(GREY)
#rect = (screen, GREY, (0, 0, 50, 10))
#arc(screen, BLACK, (0, 0, 50, 10), 0, pi * 0.96, 1)
#screen2 = pygame.transform.rotate(screen, 310)
#sc.blit(screen2, (382, 690))

#нитка
arc(sc, GREY, (290, 750, 100, 20), 0, pi, 1)
arc(sc, GREY, (230, 749, 60, 20), pi, pi * 2, 1)
arc(sc, GREY, (180, 751, 50, 10), 0, pi, 1)



pygame.display.update()
