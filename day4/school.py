
# provider
class Student:
  def __init__(self, name, score):
    self.__name = name
    self.__score = score
  def say_hello(self):
    print("hello, Mr. %s , my grade is %s" % (self.__name, self.get_grade()))

  def get_grade(self):
    if self.__score >= 90:
      return "A"
    elif self.__score >= 60:
      return "B"
    else:
      return "C"

##################################################

# customer

def main():
  student1 = Student("tony huang", 66)
  student2 = Student("tom zhang", 91)
  student1.say_hello()
  student2.say_hello()

if __name__ == '__main__':
  main()

  

