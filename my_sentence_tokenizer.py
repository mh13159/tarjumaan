# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:18:32 2020

@author: hamza
"""
import string
text= "I am P.C.H. manager Dr. Ehsan. I work at hos too as a manager."

sentence_tokens = "<s>"
mypunc = ".?:!"
'''
while (len(text)>0):
    i=0
    for char in text:
        if ((char in mypunc)):
            if char  not in text[i-3:i]:
                
                print(char)
                token = text[0:i]
                print("TOKEN",token)
                print("TEXT",text)
                sentence_tokens = sentence_tokens+token +"</s> <s>"
                text = text[i+1:]
                print("NEW TEXT",text)
            break
        i+=1
'''


tokens = text.split(" ")
i=0
while (len(tokens)>0):
    
    for word in tokens:
        #print(word)
        if word.endswith("."):
            print("FIRSTCHECK",word)
            if word.count(".")<=1:
                if len(word)>=4:
                    print(word)
                    sentence = str(tokens[0:i+1])
                    print("TOKEN",sentence)
                    print("TEXT",tokens)
                    sentence_tokens = sentence_tokens+sentence +"</s> <s>"
                    tokens = tokens[i+1:]
                    print("NEW TEXT",tokens)
                    break
                    
        i+=1