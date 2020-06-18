#http://www.danmandle.com/blog/getting-gpsd-to-work-with-python/
"""
      print(' GPS reading')
      print('----------------------------------------')
      print('latitude    ' , gpsd.fix.latitude)
      print('longitude   ' , gpsd.fix.longitude)
      print('time utc    ' , gpsd.utc,' + ', gpsd.fix.time)
      print('altitude (m)' , gpsd.fix.altitude)
      #Speed error
		print('eps         ' , gpsd.fix.eps)
      #Longitude error
		print('epx         ' , gpsd.fix.epx)
      #Vertical Error
		print('epv         ' , gpsd.fix.epv)
      #Time error
		print('ept         ' , gpsd.fix.ept)
      print('speed (m/s) ' , gpsd.fix.speed)
      #Climb and sink in meters per second
		print('climb       ' , gpsd.fix.climb)
      #Course over ground, deg from true north
		print('track       ' , gpsd.fix.track)
      print('mode        ' , gpsd.fix.mode)
      print('sats        ' , gpsd.satellites)
 """
import os
from gps import *
from time import *
import time
import threading

import math
 
gpsd = None
 
os.system('clear')
 
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
 
if __name__ == '__main__':
  gpsp = GpsPoller()
  try:
    gpsp.start()
    while True:
      os.system('clear')
      GPSspeed = round((gpsd.fix.speed*2.237),2)
      if math.isnan(GPSspeed) or GPSspeed < 1:
        GPSspeed = 0
      print(GPSspeed)
      time.sleep(1)
 
  except (KeyboardInterrupt, SystemExit):
    print("\nKilling Thread...")
    gpsp.running = False
    gpsp.join()
  print("Done.\nExiting.")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  