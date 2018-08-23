import pygame
import sys
import math
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

points = [(200, 175), (300, 125), (400, 175), (450, 125), (450, 225), (400, 175), (300, 225)]

size = width, height = 640, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLACK, (50, 30, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 30, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 30, 150, 50), 10)

    pygame.draw.polygon(screen, GREEN, points, 0)

    pygame.draw.circle(screen, RED, (320, 400), 25, 1)
    pygame.draw.circle(screen, GREEN, (320, 400), 75, 1)
    pygame.draw.circle(screen, BLUE, (320, 400), 125, 1)

    pygame.draw.ellipse(screen, BLACK, (100, 600, 440, 100), 1)
    pygame.draw.ellipse(screen, BLACK, (220, 550, 200, 200), 1)

    pygame.draw.arc(screen, BLACK, (100, 800, 440, 100), 0, math.pi, 1)
    pygame.draw.arc(screen, BLACK, (220, 750, 200, 200), math.pi, math.pi * 2, 1)

    pygame.display.flip()

    clock.tick(10)
