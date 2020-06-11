from datetime import datetime
from guizero import App, Text, PushButton, Drawing

import os
import time
import math
from random import randint

MainTextMode = ''

def hdat_Pressed():
   global MainTextMode
   MainTextMode = 'hdat'

def mindat_Pressed():
   global MainTextMode
   MainTextMode = 'mindat'

def Hour_Pressed():
   global MainTextMode
   MainTextMode = 'hour'

def Date_Pressed():
   global MainTextMode
   MainTextMode = 'date'

def Temp_Pressed():
   global MainTextMode
   MainTextMode = 'temp'

def Memo_Pressed():
   global MainTextMode
   MainTextMode = 'memo'

def TrackMode_Pressed():
   global MainTextMode
   MainTextMode = 'TrackMode'
   
def OBCMode_Pressed():
   global MainTextMode
   MainTextMode = ''

def OBC_Data():
    if MainTextMode == '':
      OBCMainText.value = (datetime.now()).strftime("%I:%M:%S %p")
      TRACK.hide()
      OBC.show()
      OBC.focus()
    if MainTextMode == 'hdat':
      OBCMainText.value = 'h/Dat'
    if MainTextMode == 'mindat':
      OBCMainText.value = 'min/Dat'
    if MainTextMode == 'hour':
      OBCMainText.value = (datetime.now()).strftime("%I:%M:%S %p")
    if MainTextMode == 'date':
      OBCMainText.value = (datetime.now()).strftime("%m/%d/%y")
    if MainTextMode == 'temp':
      OBCMainText.value = (((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip())
    if MainTextMode == 'memo':
      OBCMainText.value = 'Memo'
    if MainTextMode == 'TrackMode':
      OBCMainText.value = 'TrackMode'
      OBC.hide()
      TRACK.show()
      TRACK.focus()
      
def Track_Data():
    global radius
    """
    if Q1TargetP <= 100:
        Q1TargetP = Q1TargetP + randint(1,5)
    else:
        Q1TargetP = 0
    """
    #Q1 Gauge
    global Q1xc
    global Q1yc
    global Q1Needle
    global Q1TargetP
    global Q1Min
    global Q1Max
    Q1TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q1Needle)
    Q1Needle = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((Q1TargetP - Q1Min) * ((3.141592 * 1.25) - 0)) / (Q1Max - Q1Min))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((Q1TargetP - Q1Min) * ((3.141592 * 1.25) - 0)) / (Q1Max - Q1Min))-(3.141592 / .75)) * radius), color="black", width=5)
    #Q2 Gauge
    global Q2xc
    global Q2yc
    global Q2Needle
    global Q2TargetP
    if Q2TargetP <= 100:
        Q2TargetP = Q2TargetP + randint(1,2)
    else:
        Q2TargetP = 0
    GaugeCluster.delete(Q2Needle)
    Q2Needle = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((Q2TargetP - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((Q2TargetP - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=5)
    #Q3Gauge
    global Q3xc
    global Q3yc
    global Q3Needle
    global Q3TargetP
    if Q3TargetP <= 100:
        Q3TargetP = Q3TargetP + randint(1,2)
    else:
        Q3TargetP = 0
    GaugeCluster.delete(Q3Needle)
    Q3Needle = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((Q3TargetP - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((Q3TargetP - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=5)    
    #Q4Gauge
    global Q4xc
    global Q4yc
    global Q4Needle
    global Q4TargetP
    Q4TargetP = float((((os.popen("vcgencmd measure_volts").readline()).replace("volt=","")).replace("V","")).strip()) * 25
    GaugeCluster.delete(Q4Needle)
    Q4Needle = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((Q4TargetP - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((Q4TargetP - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=5)  
#----------------OBC MENU----------------
OBC = App(title="OBC", layout="grid")
OBC.bg = "#5E0000"
spacer = Text(OBC, text = "                                                                                                        ", font="digital-7", height="1", size=9, color="orange", grid=[0,0])
spacer = Text(OBC, text="", grid=[0,1])
OBCMainText = Text(OBC, text = "Loading", font="digital-7", height="2", size=50, color="orange", grid=[0,2])
OBCMainText.repeat(250, OBC_Data)
spacer = Text(OBC, text="", grid=[0,3])
spacer = Text(OBC, text="", grid=[0,4])
spacer = Text(OBC, text="", grid=[0,5])
spacer = Text(OBC, text="", grid=[0,6])
OBChdat = PushButton(OBC, command=hdat_Pressed, text="h/dat        ", align="left", width="fill", grid=[0,7])
OBChdat.bg = "white"
OBCmindat = PushButton(OBC, command=mindat_Pressed, text="        min/dat", align="right", width="fill", grid=[0,7])
OBCmindat.bg = "white"
spacer = Text(OBC, text="", grid=[0,8])
spacer = Text(OBC, text="", grid=[0,9])
OBChour = PushButton(OBC, command=Hour_Pressed, text="Hour        ", align="left", width="fill", grid=[0,10])
OBChour.bg = "white"
OBCdate = PushButton(OBC, command=Date_Pressed, text="        Date", align="right", width="fill", grid=[0,10])
OBCdate.bg = "white"
spacer = Text(OBC, text="", grid=[0,11])
spacer = Text(OBC, text="", grid=[0,12])
OBCtemp = PushButton(OBC, command=Temp_Pressed, text="Temp        ", align="left", width="fill", grid=[0,13])
OBCtemp.bg = "white"
OBCmemo = PushButton(OBC, command=Memo_Pressed, text="        Memo", align="right", width="fill", grid=[0,13])
OBCmemo.bg = "white"
TrackMode= PushButton(OBC, command=TrackMode_Pressed, text="TRACK", width="fill", grid=[0,13])
TrackMode.bg = "white"

#----------------TRACK MENU----------------
TRACK = App(title="TRACK")
TRACK.bg = "BLACK"
#Gauge Cluster
NumberOfGauges = 4
Width = 300
Height = 300
GaugeCluster = Drawing(TRACK, width=Width, height=Height)
GaugeCluster.oval(0, 0, Width/(NumberOfGauges/2), Height/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(Width/(NumberOfGauges/2), 0, Width, Height/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(0, Height, Width/(NumberOfGauges/2), Height/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(Width/(NumberOfGauges/2), Height, Width, Height/(NumberOfGauges/2), color="white", outline=True)

radius = Width/4
#Q1 Gauge
Q1TargetP = 0
Q1Min = 50
Q1Max = 60
Q1xc = radius
Q1yc = radius
Q1x = radius
Q1y = 0
Q1Needle = GaugeCluster.line(Q1xc, Q1yc, Q1x, Q1y, color="red", width=5)
Q1Text = GaugeCluster.text(Q1xc , Q1yc+15, text = "Temp",size=15)
Q1Max1 = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q1Min1 = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q1MaxRadius = Width/6
for i in range(0, 11):
    Q1Dashes = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
    Q1DashCover = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q1MaxRadius), Q1yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q1MaxRadius), color="white", width=5)
#Q2 Gauge
Q2TargetP = 0
Q2Min = 0
Q2Max = 100
Q2xc = radius*3
Q2yc = radius
Q2x = radius*2
Q2y = 0
Q2Needle = GaugeCluster.line(Q2xc, Q2yc, Q2x, Q2y, color="red", width=5)
Q2Text = GaugeCluster.text(Q2xc , Q2yc+15, text = "MPH",size=15)
Q2Max1 = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q2Min1 = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q2MaxRadius = Width/6
for i in range(0, 11):
    Q2Dashes = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
    Q2DashCover = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q2MaxRadius), Q2yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q2MaxRadius), color="white", width=5)
#Q3 Gauge
Q3TargetP = 0
Q3Min = 0
Q3Max = 100
Q3xc = radius
Q3yc = radius*3
Q3x = radius
Q3y = 0
Q3Needle = GaugeCluster.line(Q3xc, Q3yc, Q3x, Q3y, color="red", width=5)
Q3Text = GaugeCluster.text(Q3xc , Q3yc+15, text = "RPM",size=15)
Q3Max1 = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q3Min1 = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q3MaxRadius = Width/6
for i in range(0, 11):
    Q3Dashes = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
    Q3DashCover = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q3MaxRadius), Q3yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q3MaxRadius), color="white", width=5)
#Q4 Gauge
Q4TargetP = 0
Q4Min = 0
Q4Max = 100
Q4xc = radius*3
Q4yc = radius*3
Q4x = radius*3
Q4y = radius*2
Q4Needle = GaugeCluster.line(Q4xc, Q4yc, Q4x, Q4y, color="red", width=5)
Q4Text = GaugeCluster.text(Q4xc , Q4yc+15, text = "Volt",size=15)
Q4Max1 = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q4Min1 = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q4MaxRadius = Width/6
for i in range(0, 11):
    Q4Dashes = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
    Q4DashCover = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q4MaxRadius), Q4yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q4MaxRadius), color="white", width=5)

GaugeCluster.repeat(100, Track_Data)

spacer = Text(TRACK, text="")
spacer = Text(TRACK, text="")
spacer = Text(TRACK, text="")
OBCMode= PushButton(TRACK, command=OBCMode_Pressed, text="OBC", width="20")
OBCMode.bg = "white"

OBC.display()
TRACK.display()