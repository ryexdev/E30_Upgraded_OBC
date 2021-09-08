#---------Manual Revision Number-------------
SoftVers = "v2.22"
#--------------------------------------------
import os
from subprocess import call,Popen,PIPE
import time
from datetime import datetime
import math
import socket
from random import randint
#GPS Comms
from gps import *
import threading
#Drawing
from guizero import *

#Declare GPS
gpsd = None
UpdateTimeCycle = 30
PrevUTC = 0
GPSErrorCounter = 0

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd
    gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()

MainTextMode = ''

#---------Button Controls---------
def hdat_Pressed():
   global MainTextMode
   MainTextMode = 'hdat'

def mindat_Pressed():
   global MainTextMode
   MainTextMode = 'mindat'

def Hour_Pressed():
   global MainTextMode
   MainTextMode = 'hour'
   OBC.show()
   OBC.focus()

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
   OBC.hide()
   TRACK.show()
   
def GPSMode_Pressed():
    TRACK.hide()
    GPS.show()

def ADMINMode_Pressed():
   GPS.hide()
   ADMIN.show()  

def OBCMode_Pressed():
   global MainTextMode
   MainTextMode = 'hour'
   ADMIN.hide()
   OBC.show()
   
def Reboot_Pressed():
    call("sudo reboot", shell = True)

def KillAll_Pressed():
    call("sudo killall python3", shell = True)

def Shutdown_Pressed():
    call("sudo shutdown -h now", shell = True)
    
def Update_Pressed():
    call("cd Desktop/E30_Upgraded_OBC;sudo git pull --all;sudo reboot", shell = True)
    
def OBC_Data():
    global MainTextMode
    global TextCounter
    if MainTextMode == '':
        TRACK.hide()
        GPS.hide()
        ADMIN.hide()
        MainTextMode = 'hour'
    if MainTextMode == 'hour':
        OBCMainText.value = (datetime.now()).strftime("%I:%M:%S %p")
        
    if MainTextMode == 'hdat':
        OBCMainText.value = GPSspeedTargetP
        
    if MainTextMode == 'mindat':
        OBCMainText.value = 'min/Dat'
        call("cd Desktop/E30_Upgraded_OBC;sudo git pull --all;sudo reboot", shell = True)
        
    if MainTextMode == 'date':
        OBCMainText.value = (datetime.now()).strftime("%m/%d/%y")
        
    if MainTextMode == 'temp':
        OBCMainText.value = (((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip())
        
    if MainTextMode == 'memo':
        OBCMainText.value = 'memo'
        call("sudo shutdown -h now", shell = True)
    
      
def Track_Data():
    global radius
    #Q1 Gauge
    global Q1xc
    global Q1yc
    global Q1Needle
    global Q1TargetP
    global Q1ReadingSize
    global Q1Min
    global Q1Max
    global Q1MainReading
    global Q1ErrorCount
    try:
      Q1TargetP = float(data.decode("utf-8"))
      Q1ErrorCount = 0
    except:
      Q1ErrorCount += 1
    if Q1ErrorCount > 10:
      Q1TargetP = 0.0
    GaugeCluster.delete(Q1Needle)
    GaugeCluster.delete(Q1MainReading)
    Q1Needle = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((Q1TargetP - Q1Min) * ((3.141592 * 1.25) - 0)) / (Q1Max - Q1Min))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((Q1TargetP - Q1Min) * ((3.141592 * 1.25) - 0)) / (Q1Max - Q1Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q1MainReading = GaugeCluster.text(Q1xc , Q1yc+45, text = Q1TargetP,size=Q1ReadingSize)
    #Q2 Gauge
    global Q2xc
    global Q2yc
    global Q2Needle
    global Q2TargetP
    global Q2ReadingSize
    global Q2Min
    global Q2Max
    global Q2MainReading
    global Q2ErrorCount
    """
    try:
      data, addr = sock.recvfrom(256)
      Q2TargetP = float(data.decode("utf-8"))
      Q2ErrorCount = 0
    except:
      Q2ErrorCount += 1
    if Q2ErrorCount > 10:
      Q2TargetP = 0
    """
    Q2TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q2Needle)
    GaugeCluster.delete(Q2MainReading)
    Q2Needle = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((Q2TargetP - Q2Min) * ((3.141592 * 1.25) - 0)) / (Q2Max - Q2Min))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((Q2TargetP - Q2Min) * ((3.141592 * 1.25) - 0)) / (Q2Max - Q2Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q2MainReading = GaugeCluster.text(Q2xc , Q2yc+45, text = Q2TargetP,size=Q2ReadingSize)
    #Q3 Gauge
    global Q3xc
    global Q3yc
    global Q3Needle
    global Q3TargetP
    global Q3ReadingSize
    global Q3Min
    global Q3Max
    global Q3MainReading
    global Q3ErrorCount
    """
    try:
      data, addr = sock.recvfrom(256)
      Q3TargetP = float(data.decode("utf-8"))
      Q3ErrorCount = 0
    except:
      Q3ErrorCount += 1
    if Q3ErrorCount > 10:
      Q3TargetP = 0
    """
    Q3TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q3Needle)
    GaugeCluster.delete(Q3MainReading)
    Q3Needle = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((Q3TargetP - Q3Min) * ((3.141592 * 1.25) - 0)) / (Q3Max - Q3Min))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((Q3TargetP - Q3Min) * ((3.141592 * 1.25) - 0)) / (Q3Max - Q3Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q3MainReading = GaugeCluster.text(Q3xc , Q3yc+45, text = Q3TargetP,size=Q3ReadingSize)
    #Q4 Gauge
    global Q4xc
    global Q4yc
    global Q4Needle
    global Q4TargetP
    global Q4ReadingSize
    global Q4Min
    global Q4Max
    global Q4MainReading
    global Q4ErrorCount
    """
    try:
      data, addr = sock.recvfrom(256)
      Q4TargetP = float(data.decode("utf-8"))
      Q4ErrorCount = 0
    except:
      Q4ErrorCount += 1
    if Q4ErrorCount > 10:
      Q4TargetP = 0
    """
    Q4TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q4Needle)
    GaugeCluster.delete(Q4MainReading)
    Q4Needle = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((Q4TargetP - Q4Min) * ((3.141592 * 1.25) - 0)) / (Q4Max - Q4Min))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((Q4TargetP - Q4Min) * ((3.141592 * 1.25) - 0)) / (Q4Max - Q4Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q4MainReading = GaugeCluster.text(Q4xc , Q4yc+45, text = Q4TargetP,size=Q4ReadingSize)
    
def GPS_Data():
    global GPSradius
    #GPSspeed Gauge
    global GPSspeedxc
    global GPSspeedyc
    global GPSspeedNeedle
    global GPSspeedTargetP
    global GPSspeedMin
    global GPSspeedMax
    global GPSspeedMainReading
    global gpsp
    global gpsd
    global UpdateTimeCycle
    global PrevUTC
    global GlobalGPSStatus
    global GPSspeedMainReadingSize
    global GPSErrorCounter
    GPSspeed = round((gpsd.fix.speed*2.237),2)
    if math.isnan(GPSspeed) or GPSspeed < 1:
        GPSspeed = 0
    GPSspeedTargetP = GPSspeed
    GPSGaugeCluster.delete(GPSspeedNeedle)
    GPSGaugeCluster.delete(GPSspeedMainReading)
    GPSspeedNeedle = GPSGaugeCluster.line(GPSspeedxc, GPSspeedyc,GPSspeedxc + (math.cos((((GPSspeedTargetP - GPSspeedMin) * ((3.141592 * 1.25) - 0)) / (GPSspeedMax - GPSspeedMin))-(3.141592 / .75)) * GPSradius), GPSspeedyc + (math.sin((((GPSspeedTargetP - GPSspeedMin) * ((3.141592 * 1.25) - 0)) / (GPSspeedMax - GPSspeedMin))-(3.141592 / .75)) * GPSradius), color="black", width=8)
    GPSspeedMainReading = GPSGaugeCluster.text(GPSspeedxc+50 , GPSspeedyc+90, text = int(GPSspeedTargetP),size=GPSspeedMainReadingSize)
    if gpsd.utc != None and gpsd.utc != '' and gpsd.utc != PrevUTC:
        if UpdateTimeCycle >= 60:
            gpstime = gpsd.utc[0:4] + gpsd.utc[5:7] + gpsd.utc[8:10] + ' ' + gpsd.utc[11:19]
            os.system('sudo date -u --set="%s"' % gpstime)
            UpdateTimeCycle = 0
            PrevUTC = gpsd.utc
            GPSErrorCounter = 0
        else:
            UpdateTimeCycle += 1
        GlobalGPSStatus = 1
    else:
        GPSErrorCounter += 1 
        if GPSErrorCounter > 2:
            GlobalGPSStatus = 0
        
def Wifi_Status():
    ADMINStatus1.bg = "green"
    try:
        IpAddressSocket = socket.create_connection(("1.1.1.1", 53))
        AdminTitle.value = (IpAddressSocket.getsockname())[0] + " - " + SoftVers
        ADMINStatus1.bg = "green"
    except OSError:
        AdminTitle.value = "Admin" + " - " + SoftVers
        ADMINStatus1.bg = "red"

def GPS_Status():
    global GlobalGPSStatus    
    if GlobalGPSStatus == 1:
        ADMINStatus2.bg = "green"
    else:
        ADMINStatus2.bg = "red"

#******************************************************************************************************************************
#----------------OBC MENU----------------************************************************************************************
#******************************************************************************************************************************
OBCSpacing = 1
OBC = App(title="OBC", width=480, height=600, layout="grid")
OBC.bg = "black"
OBC.full_screen = True
OBCMainText = Text(OBC, text = "Loading", font="digital-7", width=11, height="3", size=65, color="orange", grid=[0,OBCSpacing]);OBCSpacing += 1;
OBCMainText.bg = "#5E0000"
OBCMainText.repeat(250, OBC_Data)
spacer = Text(OBC, text="", grid=[0,OBCSpacing]);OBCSpacing += 1;
spacer = Text(OBC, text="", grid=[0,OBCSpacing]);OBCSpacing += 1;
OBChdat = PushButton(OBC, command=hdat_Pressed, text="Speed                          ", align="left", height="6", width="fill", grid=[0,OBCSpacing])
OBChdat.bg = "black"
OBChdat.text_color = "white"
OBCmindat = PushButton(OBC, command=Temp_Pressed, text="               Temperature", align="right", height="6", width="fill", grid=[0,OBCSpacing]);OBCSpacing += 1;
OBCmindat.bg = "black"
OBCmindat.text_color = "white"
spacer = Text(OBC, text="", grid=[0,OBCSpacing]);OBCSpacing += 1;
OBChour = PushButton(OBC, command=Hour_Pressed, text="Hour                           ", align="left", height="6", width="fill", grid=[0,OBCSpacing])
OBChour.bg = "black"
OBChour.text_color = "white"
OBCdate = PushButton(OBC, command=Date_Pressed, text="                            Date", align="right", height="6", width="fill", grid=[0,OBCSpacing]);OBCSpacing += 1;
OBCdate.bg = "black"
OBCdate.text_color = "white"
spacer = Text(OBC, text="", grid=[0,OBCSpacing]);OBCSpacing += 1;
OBCtemp = PushButton(OBC, command=mindat_Pressed, text="Update                       ", align="left", height="6", width="fill", grid=[0,OBCSpacing])
OBCtemp.bg = "black"
OBCtemp.text_color = "white"
OBCmemo = PushButton(OBC, command=Memo_Pressed, text="                    Shutdown", align="right", height="6", width="fill", grid=[0,OBCSpacing])
OBCmemo.bg = "black"
OBCmemo.text_color = "white"
TrackMode= PushButton(OBC, command=TrackMode_Pressed, text="TRACK", height="6", width="8", grid=[0,OBCSpacing])
TrackMode.bg = "black"
TrackMode.text_color = "white"
#******************************************************************************************************************************
#----------------TRACK MENU----------------************************************************************************************
#******************************************************************************************************************************
TRACK = Window(OBC, title = "TRACK")
TRACK.bg = "BLACK"
TRACK.full_screen = True
#Gauge Face Cluster
DrawingWidth = 480
DrawingHeight = 480
NumberOfGauges = 4
GaugeWidth = DrawingWidth
GaugeHeight = 480
GaugeCluster = Drawing(TRACK, width=DrawingWidth, height=DrawingHeight)
GaugeCluster.oval(0, 0, GaugeWidth/(NumberOfGauges/2), GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(GaugeWidth/(NumberOfGauges/2), 0, GaugeWidth, GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(0, GaugeHeight, GaugeWidth/(NumberOfGauges/2), GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(GaugeWidth/(NumberOfGauges/2), GaugeHeight, GaugeWidth, GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
#Gauge Needles
radius = GaugeWidth/4
#Q1 Gauge
Q1xc = radius
Q1yc = radius
Q1x = radius
Q1y = 0
#///Q1 VARIABLES////
Q1CapSizes = 15
Q1Min = 32
Q1Max = 110
Q1Title = "Cab *F"
Q1TitleSize = 22
Q1ReadingSize = Q1TitleSize + 5
#///////////////////
Q1TargetP = 0.0
Q1Needle = GaugeCluster.line(Q1xc, Q1yc, Q1x, Q1y, color="red", width=5)
Q1MainText = GaugeCluster.text(Q1xc , Q1yc+20, text = Q1Title,size=Q1TitleSize)
Q1MainReading = GaugeCluster.text(Q1xc , Q1yc+45, text = "0",size=Q1ReadingSize)
Q1ErrorCount = 0
Q1MinText = GaugeCluster.text(Q1xc-40 , Q1yc+75, text = Q1Min,size=Q1CapSizes)
Q1MaxText = GaugeCluster.text(Q1xc+75, Q1yc-15, text = Q1Max,size=Q1CapSizes)
Q1Max1 = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q1Min1 = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q1MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q1Dashes = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q1DashCover = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q1MaxRadius), Q1yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q1MaxRadius), color="white", width=5)
#Q2 Gauge
Q2xc = radius*3
Q2yc = radius
Q2x = radius*2
Q2y = 0
#///Q2 VARIABLES////
Q2CapSizes = 15
Q2Min = 0
Q2Max = 100
Q2Title = "Pi CPU 1"
Q2TitleSize = 22
Q2ReadingSize = Q2TitleSize + 5
#///////////////////
Q2TargetP = 0.0
Q2Needle = GaugeCluster.line(Q2xc, Q2yc, Q2x, Q2y, color="red", width=5)
Q2MainText = GaugeCluster.text(Q2xc , Q2yc+20, text = Q2Title,size=Q2TitleSize)
Q2MainReading = GaugeCluster.text(Q2xc , Q2yc+45, text = "0",size=Q2ReadingSize)
Q2ErrorCount = 0
Q2MinText = GaugeCluster.text(Q2xc-40 , Q2yc+75, text = Q2Min,size=Q2CapSizes)
Q2MaxText = GaugeCluster.text(Q2xc+75, Q2yc-15, text = Q2Max,size=Q2CapSizes)
Q2Max1 = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q2Min1 = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q2MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q2Dashes = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q2DashCover = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q2MaxRadius), Q2yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q2MaxRadius), color="white", width=5)
#Q3 Gauge
Q3xc = radius
Q3yc = radius*3
Q3x = radius
Q3y = 0
#///Q3 VARIABLES////
Q3CapSizes = 15
Q3Min = 20
Q3Max = 80
Q3Title = "Pi CPU 2"
Q3TitleSize = 22
Q3ReadingSize = Q3TitleSize + 5
#///////////////////
Q3TargetP = 0.0
Q3Needle = GaugeCluster.line(Q3xc, Q3yc, Q3x, Q3y, color="red", width=5)
Q3MainText = GaugeCluster.text(Q3xc , Q3yc+20, text = Q3Title,size=Q3TitleSize)
Q3MainReading = GaugeCluster.text(Q3xc , Q3yc+45, text = "0",size=Q3ReadingSize)
Q3ErrorCount = 0
Q3MinText = GaugeCluster.text(Q3xc-40 , Q3yc+75, text = Q3Min,size=Q3CapSizes)
Q3MaxText = GaugeCluster.text(Q3xc+75, Q3yc-15, text = Q3Max,size=Q3CapSizes)
Q3Max1 = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q3Min1 = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q3MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q3Dashes = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q3DashCover = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q3MaxRadius), Q3yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q3MaxRadius), color="white", width=5)
#Q4 Gauge
Q4xc = radius*3
Q4yc = radius*3
Q4x = radius*3
Q4y = radius*2
#///Q4 VARIABLES////
Q4CapSizes = 15
Q4Min = 40
Q4Max = 60
Q4Title = "Pi CPU 3"
Q4TitleSize = 22
Q4ReadingSize = Q4TitleSize + 5
#///////////////////
Q4TargetP = 0.0
Q4Needle = GaugeCluster.line(Q4xc, Q4yc, Q4x, Q4y, color="red", width=5)
Q4MainText = GaugeCluster.text(Q4xc , Q4yc+20, text = Q4Title,size=Q4TitleSize)
Q4MainReading = GaugeCluster.text(Q4xc , Q4yc+45, text = "0",size=Q4ReadingSize)
Q4ErrorCount = 0
Q4MinText = GaugeCluster.text(Q4xc-40 , Q4yc+75, text = Q4Min,size=Q4CapSizes)
Q4MaxText = GaugeCluster.text(Q4xc+75, Q4yc-15, text = Q4Max,size=Q4CapSizes)
Q4Max1 = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q4Min1 = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q4MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q4Dashes = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q4DashCover = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q4MaxRadius), Q4yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q4MaxRadius), color="white", width=5)

GaugeCluster.repeat(250, Track_Data)
spacer = Text(TRACK, text="",)
spacer = Text(TRACK, text="",)
spacer = Text(TRACK, text="",)
spacer = Text(TRACK, text="",)
GPSMode= PushButton(TRACK, command=GPSMode_Pressed, text="GPS", width=50, height=4)
GPSMode.bg = "white"
#******************************************************************************************************************************
#----------------GPS MENU----------------************************************************************************************
#******************************************************************************************************************************
GPS = Window(OBC, title = "GPS")
GPS.bg = "BLACK"
GPS.full_screen = True
#Gauge Face Cluster
DrawingWidth = 480
DrawingHeight = 480
NumberOfGauges = 2
GaugeWidth = DrawingWidth
GaugeHeight = 480
GPSGaugeCluster = Drawing(GPS, width=DrawingWidth, height=DrawingHeight)
GPSGaugeCluster.oval(0, 0, GaugeWidth/(NumberOfGauges/2), GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
#Gauge Needles
GPSradius = GaugeWidth/NumberOfGauges
#GPSspeed Gauge
GPSspeedxc = GPSradius
GPSspeedyc = GPSradius
GPSspeedx = GPSradius
GPSspeedy = 0
#///GPSspeed VARIABLES////
GPSspeedMin = 0
GPSspeedMax = 140
GPSspeedTitle = "GPS MPH"
GPSspeedTitleSize = 30
GPSspeedMainReadingSize = 60
GPSspeedSecondaryTitle = "Raw MPH"
#///////////////////
GPSspeedTargetP = 0.0
GPSspeedNeedle = GPSGaugeCluster.line(GPSspeedxc, GPSspeedyc, GPSspeedx, GPSspeedy, color="red", width=5)
GPSspeedMainText = GPSGaugeCluster.text(GPSspeedxc , GPSspeedyc+35, text = GPSspeedTitle,size=GPSspeedTitleSize)
GPSspeedMainReading = GPSGaugeCluster.text(GPSspeedxc+50 , GPSspeedyc+90, text = "0",size=GPSspeedMainReadingSize)
GPSspeedMinText = GPSGaugeCluster.text(GPSspeedxc-50 , GPSspeedyc+105, text = GPSspeedMin,size=20)
GPSspeedMaxText = GPSGaugeCluster.text(GPSspeedxc+100, GPSspeedyc-20, text = GPSspeedMax,size=20)
GPSspeedMax1 = GPSGaugeCluster.line(GPSspeedxc, GPSspeedyc,GPSspeedxc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSradius), GPSspeedyc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSradius), color="red", width=8)
GPSspeedMin1 = GPSGaugeCluster.line(GPSspeedxc, GPSspeedyc,GPSspeedxc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSradius), GPSspeedyc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSradius), color="blue", width=8)
GPSspeedMaxRadius = GaugeWidth/3
for i in range(1, 10):
    GPSspeedDashes = GPSGaugeCluster.line(GPSspeedxc, GPSspeedyc,GPSspeedxc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSradius), GPSspeedyc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSradius), color="black", width=4)
for i in range(0, 11):
    GPSspeedDashCover = GPSGaugeCluster.line(GPSspeedxc, GPSspeedyc,GPSspeedxc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSspeedMaxRadius), GPSspeedyc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * GPSspeedMaxRadius), color="white", width=10)
#GPS Threading
gpsp = GpsPoller()
gpsp.start()
spacer = Text(GPS, text="")
spacer = Text(GPS, text="")
spacer = Text(GPS, text="")
spacer = Text(GPS, text="")
ADMINMode = PushButton(GPS, command=ADMINMode_Pressed, text="Admin", width=50, height=4)
ADMINMode.bg = "white"
GPSGaugeCluster.repeat(250, GPS_Data)
#******************************************************************************************************************************
#----------------ADMIN MENU----------------************************************************************************************
#******************************************************************************************************************************
ADMINspacing = 1
ADMIN = Window(OBC, title="ADMIN", width=480, height=600, layout="grid")
ADMIN.bg = "BLACK"
ADMIN.full_screen = True
#ADMIN BUTTONS
#----Title----
AdminTitle = Text(ADMIN, text = "Admin", font="digital-7", width=23, height="2", size=34, color="orange", grid=[0,ADMINspacing]);ADMINspacing += 1;
ADMINspacing += 1;spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
#----Row 1----
ADMINButton1 = PushButton(ADMIN, command=Reboot_Pressed, text="Reboot", align="left", height="3", width=12, grid=[0,ADMINspacing])
ADMINButton1.bg = "white"
ADMINButton1.text_size = 18
ADMINButton2 = PushButton(ADMIN, command=Shutdown_Pressed, text="Shutdown", align="right", height="3", width=12, grid=[0,ADMINspacing])
ADMINButton2.bg = "white"
ADMINButton2.text_size = 18
ADMINspacing += 1;spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
#----Row 2----
ADMINButton3 = PushButton(ADMIN, command=KillAll_Pressed, text="Kill Py", align="left", height="3", width=12, grid=[0,ADMINspacing])
ADMINButton3.bg = "white"
ADMINButton3.text_size = 18
ADMINButton4 = PushButton(ADMIN, command=Update_Pressed, text="Update", align="right", height="3", width=12, grid=[0,ADMINspacing])
ADMINButton4.bg = "white"
ADMINButton4.text_size = 18
spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
#----Status 1----
ADMINStatus1 = Text(ADMIN, text="        WIFI Status        ", size=22, grid=[0,ADMINspacing])
ADMINStatus1.bg = "red"
ADMINspacing += 1;spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
#----Status 2----
ADMINStatus2 = Text(ADMIN, text="        GPS Status        ", size=22, grid=[0,ADMINspacing])
ADMINStatus2.bg = "red"
ADMINspacing += 1;spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
#----Status 3----
ADMINspacing += 1;spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
ADMINspacing += 1;spacer = Text(ADMIN, text="", grid=[0,ADMINspacing]);ADMINspacing += 1;
#----Menu Change----
OBCMode = PushButton(ADMIN, command=OBCMode_Pressed, text="                        OBC                         ", align="bottom", height=3, width="fill", grid=[0,ADMINspacing])
OBCMode.bg = "white"
ADMINspacing += 1

ADMINStatus1.repeat(1000, Wifi_Status)
ADMINStatus2.repeat(1000, GPS_Status)

OBC.display()