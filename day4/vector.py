

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "[x: %d y: %d]" % (self.x, self.y)

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __len__(self):
    return self.x * self.x + self.y * self.y

  def __cmp__(self, other):
    if len(self) < len(other):
      return -1
    elif len(self) > len(other):
      return 1
    else:
      return 0

#########################
a = Vector(10, 10)
b = Vector(2,2)
print a+b
print len(a+b)
print a > b
print a < b


