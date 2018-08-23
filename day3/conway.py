import random
import os
import time

WIDTH = 16
HEIGHT = 16
GameBoard = {}

def init(board):
  for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
      if random.randint(0,10) < 5:
        board[(x,y)] = 1
      else:
        board[(x,y)] = 0

def render(board):
  for y in range(0, HEIGHT):
    line = ""
    for x in range(0, WIDTH):
      if board[(x,y)] == 1:
        line += "* "
      else:
        line += ". "
    print line

# return life status of one cell
def nextCell(board, x, y):
  count = 0
  if board.get((x-1,y-1), 0) == 1:
    count += 1
  if board.get((x,y-1), 0) == 1:
    count += 1
  if board.get((x+1,y-1), 0) == 1:
    count += 1
  if board.get((x-1,y), 0) == 1:
    count += 1
  if board.get((x+1,y), 0) == 1:
    count += 1
  if board.get((x-1,y+1), 0) == 1:
    count += 1
  if board.get((x,y+1), 0) == 1:
    count += 1
  if board.get((x+1,y+1), 0) == 1:
    count += 1
  if count == 2:
    return board[(x,y)]
  elif count == 3:
    return 1
  else:
    return 0

def next(board):
  newBoard={}
  for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
      newBoard[(x,y)] = nextCell(board, x,y)
  return newBoard


# TODO: next function 
# TODO: keyboard controller

def main():
  global GameBoard
  init(GameBoard)
  while True:
    os.system("clear")
    render(GameBoard)
    GameBoard = next(GameBoard)
    time.sleep(1)

if __name__ == '__main__':
  main()