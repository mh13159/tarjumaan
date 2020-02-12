# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:10:31 2020

@author: hamza
"""

from MyWordCloudGenerator import MyWordCloudGen
from io import BytesIO
figdata = BytesIO()
plot = MyWordCloudGen()


plot.savefig("F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\tarjumaan\\static\\Files\\Results\\fig.png", format='png')