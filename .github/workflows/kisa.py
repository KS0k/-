import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))
pi = 3.14


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
grey = (108, 93, 83)
purple = (244, 215, 215)
blue = (42, 212, 255)

#фон
rect(sc, OLIVE, (0, 400, 600, 400))
rect(sc, SaddleBrown, (0, 0, 600, 400))

def window(x, y, k):
    rect(sc, SkyBlue, (x, y, 270 * k, 370 * k))
    rect(sc, LightSkyBlue, (x + 10, y + 12, 110 * k, 100 * k))
    rect(sc, LightSkyBlue, (x + 105, y + 12, 105 * k, 100 * k))
    rect(sc, LightSkyBlue, (x + 10, y + 95, 110 * k, 220 * k))
    rect(sc, LightSkyBlue, (x + 105, y + 95, 105 * k, 220 * k))
    pygame.display.update()

def clew(x, y, r):
    #клубок
    circle(sc, GREY, (x, y), r)
    circle(sc, BLACK, (x, y), r, 1)
    #нитки на клубке
    screen = pygame.Surface((r, r))
    screen.fill(GREY)
    arc(screen, BLACK, (r * 0.45, r * 0.18, r, r), pi, -pi * 0.5, 1)
    arc(screen, BLACK, (r * 0.63, r * 0.18, r, r), pi, -pi * 0.5, 1)
    arc(screen, BLACK, (r * 0.72, r * 0.09, r, r), pi, -pi * 0.5, 1)
    arc(screen, BLACK, (r * 0.27, 0, r, r), 0, pi, 1)
    arc(screen, BLACK, (r * 0.27, r * 0.18, r, r), 0, pi, 1)
    arc(screen, BLACK, (r * 0.27, r * 0.36, r, r), 0, pi, 1)
    screen2 = pygame.transform.rotate(screen, 290)
    sc.blit(screen2, (x - r + r * 0.309, y - r + r * 0.309))
    #нитка
    arc(sc, GREY, (x - r * 2, y + r * 0.5, r * 1.818, r * 0.36), 0, pi, 1)
    arc(sc, GREY, (x - r * 2 - r * 1.05, y + r * 0.5, r * 1.09, r * 0.36), pi, pi * 2, 1)
    arc(sc, GREY, (x - r * 2 - r * 1.95, y + r * 0.25, r * 0.909, r * 0.818), 0, pi, 1)
    pygame.display.update()

def clew_left(x, y, r):
    screen3 = sc.convert_alpha( )
    screen3.fill([0, 0, 0, 0])
    #клубок
    circle(screen3, GREY, (x, y), r)
    circle(screen3, BLACK, (x, y), r, 1)
    #нитки на клубке
    screen = pygame.Surface((r, r))
    screen.fill(GREY)
    arc(screen, BLACK, (r * 0.45, r * 0.18, r, r), pi, -pi * 0.5, 1)
    arc(screen, BLACK, (r * 0.63, r * 0.18, r, r), pi, -pi * 0.5, 1)
    arc(screen, BLACK, (r * 0.72, r * 0.09, r, r), pi, -pi * 0.5, 1)
    arc(screen, BLACK, (r * 0.27, 0, r, r), 0, pi, 1)
    arc(screen, BLACK, (r * 0.27, r * 0.18, r, r), 0, pi, 1)
    arc(screen, BLACK, (r * 0.27, r * 0.36, r, r), 0, pi, 1)
    screen2 = pygame.transform.rotate(screen, 290)
    screen3.blit(screen2, (x - r + r * 0.309, y - r + r * 0.309))
    #нитка
    arc(screen3, GREY, (x - r * 2, y + r * 0.5, r * 1.818, r * 0.36), 0, pi, 1)
    arc(screen3, GREY, (x - r * 2 - r * 1.05, y + r * 0.5, r * 1.09, r * 0.36), pi, pi * 2, 1)
    arc(screen3, GREY, (x - r * 2 - r * 1.95, y + r * 0.25, r * 0.909, r * 0.818), 0, pi, 1)
    screen3 = pygame.transform.flip(screen3, 1, 0)
    sc.blit(screen3, (0, 0))
    pygame.display.update()

def cat(x, y, l):
    #хвост
    screen = pygame.Surface((l, l * 0.35))
    screen.fill(OLIVE)
    size = (0, 0, l, l * 0.35)
    ellipse(screen, CHOCOLATE, size)
    ellipse(screen, BLACK, size, 1)
    screen2 = pygame.transform.rotate(screen, 150)
    sc.blit(screen2, (x + l * 1.7, y + 2 * l * 0.1))
    #туловище
    ellipse(sc, CHOCOLATE, (x, y, l * 2, l))
    ellipse(sc, BLACK, (x, y, l * 2, l), 1)
    #передняя(скрытая) лапка
    ellipse(sc, CHOCOLATE, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4))
    ellipse(sc, BLACK, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4), 1)
    #голова
    circle(sc, CHOCOLATE, (x + l * 0.1, y + l * 0.425), l * 0.35)
    circle(sc, BLACK, (x + l * 0.1, y + l * 0.425), l * 0.35, 1)
    #уши
    polygon(sc, CHOCOLATE, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)])
    polygon(sc, BLACK, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)], 1)
    polygon(sc, CHOCOLATE, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)])
    polygon(sc, BLACK, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)], 1)
    polygon(sc, LightSalmon, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)])
    polygon(sc, BLACK, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)], 1)
    polygon(sc, LightSalmon, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)])
    polygon(sc, BLACK, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)], 1)
    #глаза
    ellipse(sc, GREEN, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(sc, BLACK, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    ellipse(sc, GREEN, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(sc, BLACK, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    #блики
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(GREEN)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    sc.blit(screen2, (x - l * 0.09, y + l * 0.385))
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(GREEN)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    sc.blit(screen2, (x + l * 0.205, y + l * 0.385))
    #зрачки
    ellipse(sc, BLACK, (x + l * 0.26, y + l * 0.365, l * 0.025, l * 0.175))
    ellipse(sc, BLACK, (x - l * 0.035, y + l * 0.365, l * 0.025, l * 0.175))
    #носик
    polygon(sc, ROSE, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)])
    polygon(sc, BLACK, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)], 1)
    #рот
    pi = 3.14
    line(sc, BLACK, (x + l * 0.105, y + l * 0.58), (x + l * 0.105, y + l * 0.62))
    arc(sc, BLACK, (x + l * 0.105, y + l * 0.595, l * 0.075, l * 0.075), pi, pi * 2, 1)
    arc(sc, BLACK, (x + l * 0.04, y + l * 0.595, l * 0.075, l * 0.075), -pi, pi * (-2), 1)
    #усы
    arc(sc, BROWN, (x - l * 0.4, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x - l * 0.4, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x - l * 0.4, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x + l * 0.2, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x + l * 0.2, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x + l * 0.2, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    #передняя лапка
    ellipse(sc, CHOCOLATE, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25))
    ellipse(sc, BLACK, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25), 1)
    #ляшка
    circle(sc, CHOCOLATE, (x + l * 1.75, y + l * 0.725), l * 0.275)
    circle(sc, BLACK, (x + l * 1.75, y + l * 0.725), l * 0.275, 1)
    #лапка задняя
    ellipse(sc, CHOCOLATE, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45))
    ellipse(sc, BLACK, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45), 1)
    pygame.display.update()

def cat_left(x, y, l):
    screen3 = sc.convert_alpha( )
    screen3.fill([0, 0, 0, 0])
    #хвост
    screen = pygame.Surface((l, l * 0.35), pygame.SRCALPHA)
    screen.fill([0, 0, 0, 0])
    size = (0, 0, l, l * 0.35)
    ellipse(screen, CHOCOLATE, size)
    ellipse(screen, BLACK, size, 1)
    screen2 = pygame.transform.rotate(screen, 150)
    screen3.blit(screen2, (x + l * 1.7, y + 2 * l * 0.1))
    #туловище
    ellipse(screen3, CHOCOLATE, (x, y, l * 2, l))
    ellipse(screen3, BLACK, (x, y, l * 2, l), 1)
    #передняя(скрытая) лапка
    ellipse(screen3, CHOCOLATE, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4))
    ellipse(screen3, BLACK, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4), 1)
    #голова
    circle(screen3, CHOCOLATE, (x + l * 0.1, y + l * 0.425), l * 0.35)
    circle(screen3, BLACK, (x + l * 0.1, y + l * 0.425), l * 0.35, 1)
    #уши
    polygon(screen3, CHOCOLATE, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)])
    polygon(screen3, BLACK, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)], 1)
    polygon(screen3, CHOCOLATE, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)])
    polygon(screen3, BLACK, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)], 1)
    polygon(screen3, purple, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)])
    polygon(screen3, BLACK, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)], 1)
    polygon(screen3, purple, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)])
    polygon(screen3, BLACK, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)], 1)
    #глаза
    ellipse(screen3, GREEN, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(screen3, BLACK, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    ellipse(screen3, GREEN, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(screen3, BLACK, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    #блики
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(GREEN)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    screen3.blit(screen2, (x - l * 0.09, y + l * 0.385))
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(GREEN)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    screen3.blit(screen2, (x + l * 0.205, y + l * 0.385))
    #зрачки
    ellipse(screen3, BLACK, (x + l * 0.26, y + l * 0.365, l * 0.025, l * 0.175))
    ellipse(screen3, BLACK, (x - l * 0.035, y + l * 0.365, l * 0.025, l * 0.175))
    #носик
    polygon(screen3, ROSE, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)])
    polygon(screen3, BLACK, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)], 1)
    #рот
    pi = 3.14
    line(screen3, BLACK, (x + l * 0.105, y + l * 0.58), (x + l * 0.105, y + l * 0.62))
    arc(screen3, BLACK, (x + l * 0.105, y + l * 0.595, l * 0.075, l * 0.075), pi, pi * 2, 1)
    arc(screen3, BLACK, (x + l * 0.04, y + l * 0.595, l * 0.075, l * 0.075), -pi, pi * (-2), 1)
    #усы
    arc(screen3, BROWN, (x - l * 0.4, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x - l * 0.4, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x - l * 0.4, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x + l * 0.2, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x + l * 0.2, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x + l * 0.2, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    #передняя лапка
    ellipse(screen3, CHOCOLATE, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25))
    ellipse(screen3, BLACK, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25), 1)
    #ляшка
    circle(screen3, CHOCOLATE, (x + l * 1.75, y + l * 0.725), l * 0.275)
    circle(screen3, BLACK, (x + l * 1.75, y + l * 0.725), l * 0.275, 1)
    #лапка задняя
    ellipse(screen3, CHOCOLATE, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45))
    ellipse(screen3, BLACK, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45), 1)
    screen3 = pygame.transform.flip(screen3, 1, 0)
    sc.blit(screen3, (0, 0))
    pygame.display.update()

def cat_grey(x, y, l):
    #хвост
    screen = pygame.Surface((l, l * 0.35))
    screen.fill(OLIVE)
    size = (0, 0, l, l * 0.35)
    ellipse(screen, grey, size)
    ellipse(screen, BLACK, size, 1)
    screen2 = pygame.transform.rotate(screen, 150)
    sc.blit(screen2, (x + l * 1.7, y + 2 * l * 0.1))
    #туловище
    ellipse(sc, grey, (x, y, l * 2, l))
    ellipse(sc, BLACK, (x, y, l * 2, l), 1)
    #передняя(скрытая) лапка
    ellipse(sc, grey, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4))
    ellipse(sc, BLACK, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4), 1)
    #голова
    circle(sc, grey, (x + l * 0.1, y + l * 0.425), l * 0.35)
    circle(sc, BLACK, (x + l * 0.1, y + l * 0.425), l * 0.35, 1)
    #уши
    polygon(sc, grey, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)])
    polygon(sc, BLACK, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)], 1)
    polygon(sc, grey, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)])
    polygon(sc, BLACK, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)], 1)
    polygon(sc, purple, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)])
    polygon(sc, BLACK, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)], 1)
    polygon(sc, purple, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)])
    polygon(sc, BLACK, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)], 1)
    #глаза
    ellipse(sc, blue, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(sc, BLACK, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    ellipse(sc, blue, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(sc, BLACK, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    #блики
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(blue)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    sc.blit(screen2, (x - l * 0.09, y + l * 0.385))
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(blue)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    sc.blit(screen2, (x + l * 0.205, y + l * 0.385))
    #зрачки
    ellipse(sc, BLACK, (x + l * 0.26, y + l * 0.365, l * 0.025, l * 0.175))
    ellipse(sc, BLACK, (x - l * 0.035, y + l * 0.365, l * 0.025, l * 0.175))
    #носик
    polygon(sc, ROSE, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)])
    polygon(sc, BLACK, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)], 1)
    #рот
    pi = 3.14
    line(sc, BLACK, (x + l * 0.105, y + l * 0.58), (x + l * 0.105, y + l * 0.62))
    arc(sc, BLACK, (x + l * 0.105, y + l * 0.595, l * 0.075, l * 0.075), pi, pi * 2, 1)
    arc(sc, BLACK, (x + l * 0.04, y + l * 0.595, l * 0.075, l * 0.075), -pi, pi * (-2), 1)
    #усы
    arc(sc, BROWN, (x - l * 0.4, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x - l * 0.4, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x - l * 0.4, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x + l * 0.2, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x + l * 0.2, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(sc, BROWN, (x + l * 0.2, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    #передняя лапка
    ellipse(sc, grey, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25))
    ellipse(sc, BLACK, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25), 1)
    #ляшка
    circle(sc, grey, (x + l * 1.75, y + l * 0.725), l * 0.275)
    circle(sc, BLACK, (x + l * 1.75, y + l * 0.725), l * 0.275, 1)
    #лапка задняя
    ellipse(sc, grey, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45))
    ellipse(sc, BLACK, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45), 1)
    pygame.display.update()

def cat_left_grey(x, y, l):
    screen3 = sc.convert_alpha( )
    screen3.fill([0, 0, 0, 0])
    #хвост
    screen = pygame.Surface((l, l * 0.35))
    screen.fill(OLIVE)
    size = (0, 0, l, l * 0.35)
    ellipse(screen, grey, size)
    ellipse(screen, BLACK, size, 1)
    screen2 = pygame.transform.rotate(screen, 150)
    screen3.blit(screen2, (x + l * 1.7, y + 2 * l * 0.1))
    #туловище
    ellipse(screen3, grey, (x, y, l * 2, l))
    ellipse(screen3, BLACK, (x, y, l * 2, l), 1)
    #передняя(скрытая) лапка
    ellipse(screen3, grey, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4))
    ellipse(screen3, BLACK, (x - 2 * l * 0.05, y + l * 0.45, 2 * l * 0.1125, l * 0.4), 1)
    #голова
    circle(screen3, grey, (x + l * 0.1, y + l * 0.425), l * 0.35)
    circle(screen3, BLACK, (x + l * 0.1, y + l * 0.425), l * 0.35, 1)
    #уши
    polygon(screen3, grey, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)])
    polygon(screen3, BLACK, [(x - l * 0.275, y + l * 0.1), (x - l * 0.1, y + l * 0.165), (x - l * 0.215, y + l * 0.325)], 1)
    polygon(screen3, grey, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)])
    polygon(screen3, BLACK, [(x + l * 0.25, y + l * 0.15), (x + l * 0.425, y + l * 0.06), (x + l * 0.375, y + l * 0.29)], 1)
    polygon(screen3, purple, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)])
    polygon(screen3, BLACK, [(x + l * 0.275, y + l * 0.155), (x + l * 0.4, y + l * 0.09), (x + l * 0.365, y + l * 0.26)], 1)
    polygon(screen3, purple, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)])
    polygon(screen3, BLACK, [(x - l * 0.25, y + l * 0.125), (x - l * 0.125, y + l * 0.17), (x - l * 0.205, y + l * 0.285)], 1)
    #глаза
    ellipse(screen3, blue, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(screen3, BLACK, (x - l * 0.125, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    ellipse(screen3, blue, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l))
    ellipse(screen3, BLACK, (x + l * 0.165, y + l * 0.365, 0.165 * l, 0.19 * l), 1)
    #блики
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(blue)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    screen3.blit(screen2, (x - l * 0.09, y + l * 0.385))
    screen = pygame.Surface((l * 0.03, l * 0.075))
    screen.fill(blue)
    size = (0, 0, l * 0.03, l * 0.075)
    ellipse(screen, WHITE, size)
    screen2 = pygame.transform.rotate(screen, 35)
    screen3.blit(screen2, (x + l * 0.205, y + l * 0.385))
    #зрачки
    ellipse(screen3, BLACK, (x + l * 0.26, y + l * 0.365, l * 0.025, l * 0.175))
    ellipse(screen3, BLACK, (x - l * 0.035, y + l * 0.365, l * 0.025, l * 0.175))
    #носик
    polygon(screen3, ROSE, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)])
    polygon(screen3, BLACK, [(x + l * 0.075, y + l * 0.55), (x + l * 0.135, y + l * 0.55), (x + l * 0.105, y + l * 0.58)], 1)
    #рот
    pi = 3.14
    line(screen3, BLACK, (x + l * 0.105, y + l * 0.58), (x + l * 0.105, y + l * 0.62))
    arc(screen3, BLACK, (x + l * 0.105, y + l * 0.595, l * 0.075, l * 0.075), pi, pi * 2, 1)
    arc(screen3, BLACK, (x + l * 0.04, y + l * 0.595, l * 0.075, l * 0.075), -pi, pi * (-2), 1)
    #усы
    arc(screen3, BROWN, (x - l * 0.4, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x - l * 0.4, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x - l * 0.4, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x + l * 0.2, y + l * 0.565, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x + l * 0.2, y + l * 0.58, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    arc(screen3, BROWN, (x + l * 0.2, y + l * 0.595, l * 0.4, l * 0.04), 0, pi * 0.96, 1)
    #передняя лапка
    ellipse(screen3, grey, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25))
    ellipse(screen3, BLACK, (x + l * 0.125, y + l * 0.75, l * 0.4, l * 0.25), 1)
    #ляшка
    circle(screen3, grey, (x + l * 1.75, y + l * 0.725), l * 0.275)
    circle(screen3, BLACK, (x + l * 1.75, y + l * 0.725), l * 0.275, 1)
    #лапка задняя
    ellipse(screen3, grey, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45))
    ellipse(screen3, BLACK, (x + l * 1.9, y + l * 0.8, l * 0.2, l * 0.45), 1)
    screen3 = pygame.transform.flip(screen3, 1, 0)
    sc.blit(screen3, (0, 0))
    pygame.display.update()
    



    

window(390, 50, 0.7)
window(150, 50, 0.7)
window(-110, 50, 0.7)
clew(250, 710, 55)
clew(420, 760, 20)
clew(130, 650, 20)
clew(170, 450, 20)
cat(300, 420, 100)
cat(350, 680, 35)
cat_grey(480, 740, 35)
cat_left_grey(300, 520, 100)
cat_left_grey(450, 730, 35)
clew_left(150, 595, 20)
cat_left(50, 600, 35)
clew_left(220, 635, 40)
clew_left(70, 700, 35)




