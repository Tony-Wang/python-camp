

class Animal:
  def run(self):
    print "Animal is running......"


class Dog(Animal):
  def run(self):
    print "dog is running......"

class Cat(Animal):
  def run(self):
    print "cat is running......"

def main():
  dog = Dog()
  cat = Cat()

  animalList = []
  animalList.append(dog)
  animalList.append(cat)

  for animal in animalList:
    animal.run()

if __name__ == '__main__':
  main()