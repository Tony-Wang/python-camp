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