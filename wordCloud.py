# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:37:51 2020

@author: hamza
"""
import os

from os import path
from wordcloud import WordCloud
import spacy

from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from urduhack import stop_words,normalization
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = "F:\\Current Semester\\FYP\\OASRU_CLEN\\OASRU\\ResultScripts"
# Read the whole text.
text = open(path.join(d, 'result - 45 MINUTES 20 04 2019.flac.doc'),encoding="UTF-8").read()
text = "اباوگل پاکستان ﻤﯿﮟ 20 سال ﺳﮯ، وسائل کی کوئی کمی نہیں ﮨﮯ"
text = normalization.normalize(text)
nlp = spacy.blank("ur")
print(len(text))
for each in stop_words.STOP_WORDS:
    text = text.replace(str(each),"")
print(len(text))
text=normalization.character.normalize_characters(text)
doc = nlp(text)
'''
text = arabic_reshaper.reshape(text)
text = get_display(arabic_reshaper.reshape(text))
# Generate a word cloud image
#text= normalization.normalize(text)
#text = normalization.normalize_combine_characters(text)
text =normalization.character.normalize_characters(text)
text = arabic_reshaper.reshape(text)

text = get_display(arabic_reshaper.reshape(text))
text =normalization.character.normalize_characters(text)
'''
tex=""
for word in doc:
    #print((word.text)[::-1])
    tex = tex+" "+(word.text)[::-1]
#tex = arabic_reshaper.reshape(tex)

#tex = get_display(arabic_reshaper.reshape(tex))
tex = normalization.normalize(tex)

wordcloud = WordCloud("F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\project_updated_6thFeb\\Urdu_fonts\\AlQalam Taj Nastaleeq-Regular1(shipped).ttf").generate(tex)


wordcloud.to_image()
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
