import os
import speech_recognition as sr
import time


# r is Speech Recognition Recognizer object
r = sr.Recognizer()


# please put the name of file which you segmented before e.g PM_IK , Sample1
#dire ='D:\\UrduDataset\\shairi\\'
def speechtotext(filename):

    if filename.endswith('.wav'):
        print(filename)
        print(" Start Recognizing")
        soundbite = sr.AudioFile(filename) 
        with soundbite as source:
            #r.adjust_for_ambient_noise(source)
            r.energy_threshold = 100
            r.non_speaking_duration =1
            r.dynamic_energy_threshold = False
            audio = r.record(source)
        try:
            # output text file open
            OutputFile= open(filename.split(".")[0]+".doc","a+",encoding="utf-8")
            text = r.recognize_google(audio, language="UR-PK", show_all=False)
            print(" Writing ")
            print (text)
            OutputFile.write(text+"\n")
            time.sleep(2)
        except Exception as e:
            print("There is some issue with:")
            print (e)
            
