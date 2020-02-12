# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:55:32 2019
@author: hamza
"""


import os
import speech_recognition as sr
import time
import pandas as pd

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def Recognizer(input_files_folder,output_scripts_folder):
    #input_files_folder='C:\\Users\\Areeba Shamsi\\Anaconda3\\envs\\flask-app\\Lib\\site-packages\\spyder\\utils\\help\\static\\audios'
    #intput_scripts_folder='C:\\Users\\Areeba Shamsi\\Anaconda3\\envs\\flask-app\\Lib\\site-packages\\spyder\\utils\\help\\static\\audios'
    # r is Speech Recognition Recognizer object
    r = sr.Recognizer()
    
    #chunks' directory
    #chunksdir = 'D:\\UrduDataset\\TalkShow\\CapitalTalk'
    #chunksdir = 'F:\\Current Semester\\FYP\\OASRU\\ResultAudio'
    chunksdir = input_files_folder
    # All folders in chunks' directroy
    
    chunksdirlist = os.listdir(chunksdir)
    chunksdirlist.sort(key=lambda x: os.stat(os.path.join(chunksdir, x)).st_mtime)
    #transcripts' directory 
    #scriptsdir = 'D:\\UrduDataset\\TalkShow\\CapitalTalk'
    #scriptsdir = 'F:\\Current Semester\\FYP\\OASRU\\ResultScripts\\'
    scriptsdir = output_scripts_folder
    ensure_dir(scriptsdir)
    # All folders in scripts' directroy
    #scriptdirlist = os.listdir(scriptdir)
    
    # inner
    chunkname = []
    chunkrecognitiontime = []
    chunklength = []
    
    #outer
    folderrecognitiontime = []
    folderlength = []
    foldername = []
    for folder in chunksdirlist:
        print(folder)
        chunkfolderdir=chunksdir+'\\'+folder+'\\'
        if(os.path.isdir(chunkfolderdir)):
            
            foldername.append(folder)
    
            chunks_in_folder= sorted(os.listdir(chunkfolderdir), 
                               key=lambda x: os.path.getctime(os.path.join(chunkfolderdir, x)))
            OutputFile= open(scriptsdir+folder+".doc","w+",encoding="utf-8")
            OutputFile.close()
            #OutputFile = Document()
            #OutputFile.save(scriptsdir+folder+".docx")
            for InputFile in chunks_in_folder:
                
                if(InputFile.endswith('.wav')):
                    starttime = time.time()
                    chunkname.append(InputFile)    
                    print(" Start Recognizing")
                    soundbite = sr.AudioFile(chunkfolderdir+InputFile) 
                    
                    
                    with soundbite as source:
                        #r.adjust_for_ambient_noise(source)
                        audio = r.record(source)
                        chunklength.append(soundbite.DURATION)
                        r.adjust_for_ambient_noise(source)
                        r.__reduce__
                    try:
                        # output text file open
                        OutputFile= open(scriptsdir+folder+".doc","a+",encoding="utf-8")
                        # recognized text in variable text
                        text = r.recognize_google(audio, language="ur-PK")
                        print(text)
                        print(" Writing")
                        OutputFile.write(text+"\n")
                        #test= OutputFile.read()
                        #print('Testing: '+test)
                        print('Done!')
                        endtime = time.time()
                        chunkrecognitiontime.append(endtime-starttime)
                        time.sleep(0.5)
                        
                        #close file
                        OutputFile.close()
                        
                        # Empty the text variable
                        text=""
                    except Exception as e:
                        chunkrecognitiontime.append(0)
                        # Incase there is some undefined behaviour
                        print("There is some issue with:",InputFile)
                        OutputFile.close()
                        print (e)
                    continue
                OutputFile.close()
            innerdf = pd.DataFrame()
            innerdf['chunk'] = chunkname
            innerdf['length'] = chunklength
            innerdf['recognitiontime'] = chunkrecognitiontime
            innerdf.to_csv(scriptsdir+folder+'chunkList.csv')
            flen = sum(chunklength)
            frlen = sum(chunkrecognitiontime)
            folderlength.append(flen)
            folderrecognitiontime.append(frlen)
            chunklength = []
            chunkname = []
            chunkrecognitiontime = []
    outerdf  = pd.DataFrame()        
    outerdf['chunkfolder'] = foldername
    outerdf['folderlength'] = folderlength
    outerdf['recognitiontime'] = folderrecognitiontime
    outerdf.to_csv(scriptsdir+folder+'folderList.csv')