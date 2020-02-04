# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:11:25 2020

@author: Areeba Shamsi
"""
import wave
import mutagen.flac as flac
import os

def check(file):
    
    fl = os.path.join("D:\\Flask_20thjan\\static\\Files\\Audios\\1", file)
    
    if file.endswith('.flac'):
        f = flac.FLAC(fl).info
        rate = f.sample_rate
    else:
        f = wave.open(fl)
        rate = f.getframerate()
        
    print(rate)
    if(16000 <= rate <= 48000):
        return '🙂'
    else:
        return '🙁'
    
    
    #Sample rates between 8000 Hz and 48000 Hz are supported 
    #within Cloud Speech-to-Text. The sample rate for a FLAC 
    #or WAV file can be determined from the file header instead 
    #of from the sampleRateHertz field. If you have a choice 
    #when encoding the source material, capture audio using 
    #a sample rate of 16000 Hz.]

def audioCheck(input_files_folder):
    chunksdir = input_files_folder
    chunksdirlist = os.listdir(chunksdir)
    chunksdirlist.sort(key=lambda x: os.stat(os.path.join(chunksdir, x)).st_mtime)
    checklist = []
    for file in chunksdirlist:
        checklist.append(check(file)) 
            
    return checklist

'''
def main():
    print(audioCheck('D:\\Urdu\\Audio\\'))
    
if __name__=='__main__':
    main()
'''