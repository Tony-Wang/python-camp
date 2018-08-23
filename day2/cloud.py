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

