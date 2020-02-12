# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:33:56 2020

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
from flask import Markup
import os

def MyWordCloudGen(imgpath,scriptpath):
    
   # d = "F:\\Current Semester\\FYP\\OASRU_CLEN\\OASRU\\ResultScripts"
    configuration = {
        'delete_harakat': False,
        'support_ligatures': True,
        'RIAL SIGN': True,  # Replace ر ي ا ل with ﷼
    }
    reshaper = ArabicReshaper(configuration=configuration)
    text_to_be_reshaped = open(path.join(scriptpath, 'CapitalTalkSegmented_audio_1 Saal Main PTI Hukumat Ne Konsi Bari Kamiyabi Hasil Ki.wav.doc'),encoding="UTF-8").read()
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
    fontdir="D:\\tarjumaan-master\\Urdu_fonts\\"    
    import os
    plt.figure(figsize=(20,15),dpi=200)
    wordcloud = WordCloud(os.getcwd()+"\\Urdu_fonts\\"+"DecoType Thuluth.ttf",
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
    plt.savefig(imgpath+"\\image.png", format="png")
    plt.show()
        
    img = imgpath+"\\"+"image.png"
    print(img)
    print("Relative Path",os.path.relpath(img))
    img = os.path.relpath(img)
    return img


def main():
    path = MyWordCloudGen(os.getcwd()+"\\static\\assets\\images",os.getcwd()+"\\static\\Files\\Results")
    print(path.replace("\\","/"))
    
if __name__=="__main__":
    main()