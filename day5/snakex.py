import pygame 
from pygame.locals import *
import sys
import random

WINDOWS_WIDTH=800
WINDOWS_HEIGHT=500
Cell_Size=20
Cell_W = int(WINDOWS_WIDTH / Cell_Size)
Cell_H = int(WINDOWS_HEIGHT / Cell_Size)

Snakespeed = 10
COLOR_BLACK=(0, 0, 0)
COLOR_WHITE=(255, 255, 255)
COLOR_RED=(255, 0, 0)
COLOR_DEEPGREEN=(0, 155, 0)
COLOR_GREEN=(0, 255, 0)
COLOR_DARKGRAY=(40, 40, 40)

def gameLoop():
  startx = random.randint(5, Cell_W-6)
  starty = random.randint(5, Cell_H-6)
  direction = "UP"
  score = 0
  snakeBody = [
    {'x':startx,'y':starty},
    {'x':startx-1,'y':starty},
    {'x':startx-2,'y':starty},
    ]
  head = snakeBody[0]
  
  apple = {'x': random.randint(0, Cell_W-1),'y': random.randint(0, Cell_H-1)}

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      elif event.type == KEYDOWN:
        if (event.key == K_LEFT) and direction != "RIGHT":
          direction = "LEFT"
        elif (event.key == K_RIGHT) and direction != "LEFT":
          direction = "RIGHT"
        elif (event.key == K_UP) and direction != "DOWN":
          direction = "UP"
        elif (event.key == K_DOWN) and direction != "UP":
          direction = "DOWN"
        elif event.key == K_ESCAPE:
          sys.exit()
    
    if head['x'] == apple['x'] and head['y'] == apple['y']:
      apple = {'x': random.randint(0, Cell_W-1),'y': random.randint(0, Cell_H-1)}
    else:
      del snakeBody[-1]

    if direction == "RIGHT":
      newHead = {'x': head['x']+1, 'y':head['y']}
    if direction == "LEFT":
      newHead = {'x': head['x']-1, 'y':head['y']}
    if direction == "UP":
      newHead = {'x': head['x'], 'y':head['y']-1}
    if direction == "DOWN":
      newHead = {'x': head['x'], 'y':head['y']+1}
    
    snakeBody.insert(0, newHead)
    score = len(snakeBody)
    head = newHead

    DISPLAYSURF.fill(COLOR_BLACK)
    drawGrid()
    drawApple(apple)
    drawSnake(snakeBody)
    drawScore(score)
    pygame.display.update()
    SnakespeedCLOCK.tick(Snakespeed)

def drawGrid():
  for x in range(0, WINDOWS_WIDTH,Cell_Size):
    pygame.draw.line(DISPLAYSURF, COLOR_DARKGRAY,(x, 0),(x, WINDOWS_HEIGHT))
  for y in range(0, WINDOWS_HEIGHT,Cell_Size):
    pygame.draw.line(DISPLAYSURF, COLOR_DARKGRAY,(0, y),(WINDOWS_WIDTH, y))

def drawApple(coord):
  x = coord['x'] * Cell_Size
  y = coord['y'] * Cell_Size
  appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
  pygame.draw.rect(DISPLAYSURF, COLOR_RED, appleRect)

def drawSnake(snake):
  for coord in snake:
      x = coord['x'] * Cell_Size
      y = coord['y'] * Cell_Size
      snakeRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
      pygame.draw.rect(DISPLAYSURF, COLOR_GREEN, snakeRect)


def drawScore(score):
  scoreSurf = pressFont.render("Socre: %s" % score, True, COLOR_WHITE, COLOR_BLACK)
  scoreRect = scoreSurf.get_rect()
  scoreRect.topleft = (WINDOWS_WIDTH-120, 10)
  DISPLAYSURF.blit(scoreSurf, scoreRect)

def main():
  global DISPLAYSURF, SnakespeedCLOCK

  pygame.init()
  SnakespeedCLOCK = pygame.time.Clock()
  DISPLAYSURF = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
  pygame.display.set_caption("Snake")
  showStartScreen()
  gameLoop()

def showStartScreen():
  global pressFont
  titleFont = pygame.font.Font('freesansbold.ttf', 100)
  titleSurf = titleFont.render("Snake!", True, COLOR_WHITE, COLOR_DEEPGREEN)
  pressFont = pygame.font.Font('freesansbold.ttf', 18)
  pressSurf = pressFont.render("press any key to start!", True, COLOR_WHITE, COLOR_BLACK)
  degrees = 0

  while True:
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) != 0 and keyUpEvents[0].key == K_ESCAPE:
      sys.exit()
    if len(keyUpEvents) != 0:
      return
    
    DISPLAYSURF.fill(COLOR_BLACK)
    rotatedSurf = pygame.transform.rotate(titleSurf, degrees)
    rotatedRect = rotatedSurf.get_rect()
    rotatedRect.center = (WINDOWS_WIDTH / 2, WINDOWS_HEIGHT / 2)
    DISPLAYSURF.blit(rotatedSurf, rotatedRect)

    pressRect = pressSurf.get_rect()
    pressRect.topleft = (WINDOWS_WIDTH - 200, WINDOWS_HEIGHT - 30)
    DISPLAYSURF.blit(pressSurf, pressRect)

    pygame.display.update()
    pygame.display.flip()
    SnakespeedCLOCK.tick(Snakespeed)
    degrees += 3
    

if __name__ == '__main__':
  main()