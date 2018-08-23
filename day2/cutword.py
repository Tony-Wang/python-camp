import jieba
import pickle 
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



