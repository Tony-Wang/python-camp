# -*- coding:utf-8 -*-

STOPWORDS=set([u"的",u"，",u"很",u"。",u"了",u"还"])
def top_10_by_value(d):
  items = d.items()

  backItems = [[v[1],v[0]] for v in items if v[0] not in STOPWORDS]
  '''
  上一行代码等价于下面的代码
  backItems = []
  for v in items:
    if v[0] not in STOPWORDS:
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