import random
import os
import time

WIDTH = 16
HEIGHT = 16
HOLD_CONDITION = 2
RELIVE_CONDITION = 3

class ConwayGame:
  def __init__(self):
    self.board = Board(WIDTH, HEIGHT)

  def waiteOneSecond(self):
    time.sleep(1)

  def next(self):
    self.board.next()
  
  def render(self):
    self.board.render()

class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.cells = {}
    for y in range(0, self.height):
      for x in range(0, self.height):
        self.cells[(x,y)] = Cell()
    self.random_alive()

  def random_alive(self):
    for y in range(0, self.height):
      for x in range(0, self.width):
        if random.randint(0,10) < 5:
          self.cells[(x,y)].relive()

  def render(self):
    for y in range(0, self.height):
      line = ""
      for x in range(0, self.width):
        line += self.cells[(x,y)].render()
      print line


  def getLeftUpCell(self, x, y):
    return self.cells.get((x-1, y-1), DeadCell())

  def getALiveCellCount(self, x, y):
    count = 0
    if self.getLeftUpCell(x, y).alive():
       count += 1
    if self.cells.get((x,y-1), DeadCell()).alive() :
       count += 1
    if self.cells.get((x+1,y-1), DeadCell()).alive():
       count += 1
    if self.cells.get((x-1,y), DeadCell()).alive():
       count += 1
    if self.cells.get((x+1,y), DeadCell()).alive():
       count += 1
    if self.cells.get((x-1,y+1), DeadCell()).alive():
       count += 1
    if self.cells.get((x,y+1), DeadCell()).alive():
       count += 1
    if self.cells.get((x+1,y+1), DeadCell()).alive():
       count += 1
    return count

  def next_cell(self, x, y):
    count = self.getALiveCellCount(x, y)
    if count == HOLD_CONDITION:
      return self.cells[(x,y)]
    elif count == RELIVE_CONDITION:
      return LiveCell()
    else:
      return DeadCell()

  def next(self):
    newBoard={}
    for y in range(0, self.height):
      for x in range(0, self.width):
        newBoard[(x,y)] = self.next_cell(x, y)
    self.cells = newBoard

class Cell:
  def __init__(self):
    self.dead()

  def relive(self):
    self.__alive = True
  
  def dead(self):
    self.__alive = False

  def alive(self):
    return self.__alive
  
  def render(self):
    if self.alive():
      return "* "
    else:
      return ". "

class DeadCell(Cell):
  pass

class LiveCell(Cell):
  def __init__(self):
    self.relive()
