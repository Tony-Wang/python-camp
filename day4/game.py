import conwayoo

def main():
  game = conwayoo.ConwayGame()
  while True:
    game.render()
    game.waiteOneSecond()
    game.next()

if __name__ == '__main__':
  main()

