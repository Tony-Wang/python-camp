[TOC]

# 知识点复习

## Python安装方式

* window
* linux
* mac



## 程序执行方式

1. 使用交互界面输入指令

   > 进入方式 命令行环境下输入```python```
   >
   > 退出方式 exit() 或 ctrl+d

2. 执行脚本文件

   > 在命令行环境下，执行 ```python 文件名```

   

## 语法

### 变量

* 整型 ```number = 10001```

  > **5**个苹果，每个星期有**7**天

* 浮点型 ``` pi = 3.1415926```

  > 四分之三片药片，52.4KG

* 字符串 ``` name = "tony"```

  > 小明说：“明天将有一个重达2.3吨的大象到马戏团表演”

* 布尔型 ```success = True```

  > 作业已经写完了吗？这件事情是真的吗？

* 复数型

  

  

### 列表

```Python
# 新建列表
l = []

# 初始化列表
 l = [1,2,3]

# 插入数据
l.append(1)

# 遍历数据
for i in l:
    print i
    
```

### 元组

```Python
# 初始化
tuple1 = (1,2,3,4,5)
tuple2 = ("hello", 3, 3.1415926)
tuple3 = (50,)

# 访问操作
tuple1[1]
tuple1[1:4]

# list 转 tuple
tuple(l)

# tuple 转list 
list(t)

# 元组重复
tupel1 * 50

# 元组相加
tuple1 = tuple1 + tuple2

# 遍历元组
for i in (1,2,3,4,5,6):
    print i
    
# 布尔操作
3 in tuple


```

### 字典

```Python
# 初始化
dict1 = {}


```



### 集合 ###

```
s = Set()
```





## 有用的函数

```Python
# 显示当前名字空间的内容
dir()

# 显示变量的类型
type(var)

# 接受用户的输入
raw_input()

# 随机数模型
random

# 打印数据
print(var)



```





### 条件判断

```Python
if condition :
elif condition:
...

if condition:
	xxxxxxxx
else:
	xxxxxxxx
    
    
while condition:
    xxxxxxxxxxxx
    
   
```

### 循环

```Python
for i in enum:
	pass
	
while condition:
	pass

# 使用break continue两种语种来对循环体实现控制

```

> `break`退出循环
>
> `continue`提前结束本次迭代



### 文件操作

```Python
# 打开文件
f = open(filename)

# 读取内容
contents = f.readlines()

# 写数据
f.write(line)

# 关闭文件
f.close()



```



## 字符串

```python
strVar = 'Hello World'
strVar2 = "Python"

# 字符串运算
print strVar + strVar2

# 字符串重复
print "Hello" * 10

# 取子字符串
print strVar[2]
print strVar[0:3]

# 测试成员运算

'H' in strVar

'P' not in strVar2

 'capitalize',
 'center',
 'count',
 'decode',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'index',
 'isalnum',
 'isalpha',
 'isdigit',
 'islower',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill'

```



### 打印名字功能

```Python

welcomTemplate = "hi, %s welcome"
f = open("classmates.txt")
content = f.readlines()
f.close()
content = content[0]
nameList = content.split(',')
for name in nameList:
    print welcomeTemplate % name
```



### 时间模块

```Python
import time
import datetime

print time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime())

# 返回当前时间
datetime.datetime.now()

# 返回今天的日期
datetime.date.today()

# 计算你已经活了多少天
datetime.date.today() - datetime.date(2000, 4, 1)

```



### 函数

```Python
def foo(p1=1, p2=2):
    print "you input %d and %d" % (p1, p2)
    
foo()
foo(2)
foo(2, 3)
foo(p2=4)

def foo(*argv):
    for p in argv:
        print p

def foo(**argv):
    for k,v in argv.items:
        print k,v

# 匿名函数
double = lambda x:2*x
        
# 生成一个列表，并把每个元素乘2
# 方法1
l = range(1,10)
doubleList = []
for i in l:
    doubleList.append(i*2)
doubleList

# 方法2 
[ 2*x for x in l]

# 方法3
double = lambda x:2*x
double(1)
map(double, l)
```



## 生成HTML

```Python
import datetime

htmlTemplate='''
<html>
<body>
    <h1>%s</h1>
    <img src="girl.jpg" />
</body>
</html>
'''

def main():
  htmlFile = open("index.html", "w")
  htmlFile.write(htmlTemplate % datetime.datetime.now())
  htmlFile.close()

if __name__ == '__main__':
  main()
```



## 从第三方源安装模块

####  安装结巴分词

```Shell
pip install jieba -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

#### 测试是否安装成功

```Python
# 在交互界面输入
import jieba
```

#### 安装wordcloud

```
pip install wordcloud -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```



##  词图实验

### 生成分词文件

```Python
import jieba

f = open("meidi.txt")
contents = f.readlines()
f.close()

tokens = ""
for line in contents:
  line = line.strip("\n")
  tokens = tokens + " ".join(jieba.cut(line))
  tokens = tokens + " "

fileOut = open("meidi_cut.txt",'wb')
fileOut.write(tokens.encode("utf-8"))
fileOut.close()
```

### 生成图型

```Python
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt

f = open("meidi_cut.txt", 'rb')
contents = f.readlines()
contents = contents[0].decode("utf-8")
f.close()
print contents

bgImage = plt.imread("girl.jpg")
wc = WordCloud(
  background_color='white',
  mask=bgImage,
  max_words=200,
  stopwords=STOPWORDS,
  max_font_size=50,
  font_path="c:/Users/Windows/fonts/msyh.ttf",
  random_state=50
)
imageColor = ImageColorGenerator(bgImage)
wc.generate(contents)
wc.recolor(color_func=imageColor)
plt.imshow(wc)
plt.show()

```

### 统计词频

```Python

def top_10_by_value(d):
  items = d.items()

  backItems = [[v[1],v[0]] for v in items]
  '''
  上一行代码等价于下面的代码
  backItems = []
  for v in items:
     backItems.append([v[1], v[0]])
  '''

  backItems.sort()
  backItems.reverse()
  return [backItems[i][1] for i in range(0,10)] 
'''
  result = []
  for i in range(0,10):
    result.append(backItems[i][1])
  return result
'''


def main():
  f = open("../day2/meidi_cut.txt")
  content = f.readlines()[0].strip("\n").decode("utf-8")
  tokens = content.split()
  dictWordCount = {}
  for t in tokens:
    if dictWordCount.has_key(t):
      dictWordCount[t] += 1
    else:
      dictWordCount[t] = 1

  top10 = top_10_by_value(dictWordCount)
  for t in top10:
    print t

if __name__ == '__main__':
  main()
```



## 康威生命游戏

```Python
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
```



### 面向对象

```Python


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
```





### 康威生命游戏OO版

```Python
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

```



### 操作符重载

```Python


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

```



### 文件处理

```Python
import os, glob, shutil

BAK_DIR = "/Users/tony/MyProject/python/bak/"
"c:\\n\n"

os.chdir("/Users/tony/MyProject/python/day4/")

fileList = glob.glob("*.py")

if not os.path.exists(BAK_DIR):
  os.mkdir(BAK_DIR)

for file in fileList:
  shutil.copy(file, BAK_DIR)


shutil.make_archive("bak", "zip", BAK_DIR)

shutil.rmtree(BAK_DIR)
```



### 图形界面

```Python

from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.byeLabel = Label(self, text='Good bye, world!')
        self.byeLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

def main():
  app = Application()
  app.master.title("hello world")
  app.mainloop()

if __name__ == '__main__':
  main()
```



