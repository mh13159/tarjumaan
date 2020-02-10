# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:57:38 2020

@author: hamza
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 01:52:58 2020

@author: hamza
"""

import arabic_reshaper
from os import path
from wordcloud import WordCloud
import spacy
import matplotlib.pyplot as plt
from urduhack import normalize
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display
from urduhack import stop_words,normalization

d = "F:\\Current Semester\\FYP\\OASRU_CLEN\\OASRU\\ResultScripts"

configuration = {
    'delete_harakat': False,
    'support_ligatures': True,
    'RIAL SIGN': True,  # Replace ر ي ا ل with ﷼
}

reshaper = ArabicReshaper(configuration=configuration)
text_to_be_reshaped = "ترجمان"
text_to_be_reshaped = normalize(text_to_be_reshaped)
text_to_be_reshaped = normalization.normalize_characters(text_to_be_reshaped)
text_to_be_reshaped = normalization.normalize_combine_characters(text_to_be_reshaped)
text_to_be_reshaped = normalization.punctuations_space(text_to_be_reshaped)
nlp = spacy.blank("ur")
reshaped_text = reshaper.reshape(text_to_be_reshaped)
doc = nlp(text_to_be_reshaped)
text = []

for each in doc:
    if str(each) not in str(stop_words.STOP_WORDS):
        #(each)
        text.append(str(each))
reshaped_text = ""

for each in text:
        reshaped_text = reshaped_text+" "+each
    
reshaped_text = reshaper.reshape(reshaped_text)

from bidi.algorithm import get_display
bidi_text = get_display(reshaped_text)
fontdir="F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\project_updated_6thFeb\\Urdu_fonts\\"

import os

fonts = os.listdir(fontdir)
x=1

for font in fonts:
    print(x)
    if font.endswith("ttf"):
        print("Font",font)
        plt.title="Word Cloud"
        
        plt.figure(figsize=(20,15),dpi=50)
        wordcloud = WordCloud("F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\project_updated_6thFeb\\Urdu_fonts\\"+font,
                              width=2000,
                              height=1500,
                              include_numbers=True,
                              stopwords=stop_words.STOP_WORDS,
                              min_font_size=30,
                              background_color="black",
                              margin=0,
                              max_words=200).generate(bidi_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        x+=1
        plt.show()


