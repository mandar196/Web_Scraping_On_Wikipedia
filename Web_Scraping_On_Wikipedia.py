
import nltk
import re
import urllib
import bs4 as bs
from nltk.corpus import stopwords
nltk.download('stopwords')

source=urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()
soup=bs.BeautifulSoup(source,'lxml')

text=""
for paragraph in soup.find_all('p'):
    text=text+paragraph.text
    
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences = nltk.sent_tokenize(text)


sentences = [nltk.word_tokenize(sentence) for sentence in sentences]