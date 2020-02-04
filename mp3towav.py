# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:15:48 2019
@author: muham
"""

from pydub import AudioSegment
import os 
from pydub.utils import which
AudioSegment.converter = which("ffmpeg")
    #directory = "SampleAudio"
#DIR with test files
# F:\\VoiceRecognition\\Foresight_research\\Ogni4Zubair\\Total
#directory = 'F:\\VoiceRecognition\\Foresight_research\\Ogni4Zubair'
#directory = 'F:\Current Semester\FYP\OASRU\EnglishStudioGrade'
#directory = 'F:\\Current Semester\\FYP\\OASRU\\UrduStudioGrade'
directory = "D:\\UrduDataset"

i = 0
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".wav") or filename.endswith(".mp4") or filename.endswith(".MP4")or filename.endswith(".mp3"):
        song = AudioSegment.from_wav(directory+'\\'+filename)
        print("exporting "+filename.format(i))
        song.export(
                directory+'\\'+filename[:len(filename)-4]+'.wav'.format(i),
                format="wav")
        i = i+  1  