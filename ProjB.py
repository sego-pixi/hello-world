import threading
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
from _thread import start_new_thread
from datetime import datetime
from os import system, name
import sys
import subprocess, os
import signal
import BlynkLib

#BLYNK_AUTH='7t6Q72qVqWmrxPWydL0F18TEWejod_7P'
BLYNK_AUTH='MuR0By29Wg-I38uvkZoSLe3vfP6iyyR7'
blynk=BlynkLib.Blynk(BLYNK_AUTH)
#this is for the start/stop button (Changed pin to 16)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#this is for the interval button
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 1
chan = AnalogIn(mcp, MCP.P0)



start=time.time()
print("Press button to start monitoring the sensor")
t=5#initially
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
count=0;
count2=0


def get_press():      
        while True:                              
            if(GPIO.input(15)):                    
                    #btn_pressed = True
                    global t
                    if t==10:
                        t=2
                        time.sleep(3)
                      
                    elif t==2:
                        t=5                       
                        time.sleep(3)
                    elif t==5:
                        t=10
                        time.sleep(3)
                    print("new interval:",t)
                    blynk.virtual_write(1,"new interval:",t,"\n")

              
def start_helper_thread():
    try:
        start_new_thread(get_press,())
    except:
        print("thread error")
        
def printit():  
       global count2
       global t
       start_helper_thread()     
       while True:
        #if(GPIO.input(16)) and count2==0:
                 
#             if(GPIO.input(16)):
#              count2=1
#             else:
              x=chan.voltage-0.5
              temperature=x/0.1
              #thread = threading.Timer(5, printit).start()
              time.sleep(t)
              now= datetime.now()        
              current_time = now.strftime("%H:%M:%S")
              print(current_time,end="")   
              blynk.virtual_write(1,current_time)
                      #time.sleep(5)
              end=time.time()
              duration=end-start
              secs=round(duration)
              #sensor_data=20             
              #blynk.virtual_write(1,sensor_data)
              m, s = divmod(secs, 60)
              h, m = divmod(m, 60)
              print('  {:02d}:{:02d}:{:02d}'.format(h, m, s),end="") 
              blynk.virtual_write(1,'   {:02d}:{:02d}:{:02d}'.format(h, m, s))
              print("{:-8.1f} C".format(temperature))
              newtemp=round(temperature,1)
              blynk.virtual_write(1,"       ")
              blynk.virtual_write(1,newtemp,"\n")
                             
def main():
  
  global count
  while True:
    
    blynk.run()
    if(GPIO.input(16)):
        
        if count==0:
            
            
            print("logging started")
            blynk.run()
            blynk.virtual_write(1,"clr")
            now= datetime.now()
            current_time = now.strftime("%H:%M:%S")
            x=chan.voltage-0.5
            temperature=x/0.1
            print("Time      Sys Timer  Temp") #spaces of 4 between words
            blynk.virtual_write(1,"Time       Sys Timer      Temp\n")
            print(current_time,end="")
            blynk.virtual_write(1,current_time)
            print("  00:00:00",end="")
            blynk.virtual_write(1,"   00:00:00       ")
            print("{:-8.1f} C".format(temperature))
            newtemp=round(temperature,1)
            blynk.virtual_write(1,newtemp,"\n")
            printit()
            count=1
        elif count ==1:
                print("1..logging has stopped")
                time.sleep(4)
                clear()              
                print("Logging has stopped you can now exit the program")
                time.sleep(15)
                break

            
main()
