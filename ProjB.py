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

#this is for the start/stop button (Changed pin to 16)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#this is for the interval button
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 1
chan = AnalogIn(mcp, MCP.P1)

start=time.time()
print("Press button to start monitoring the sensor")

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
#btn_already_pressed=False
count=0;

def get_press():
        while True:           
            if(GPIO.input(15)):
                    #btn_pressed = True
                    global s
                    if s==10:
                        s=1
                        time.sleep(3)
                      
                    elif s==1:
                        s=5                       
                        time.sleep(3)
                    elif s==5:
                        s=10
                        time.sleep(3)
                    print(s)
       
                        
            else:
                btn_pressed=False

              
def start_helper_thread():
    try:
        start_new_thread(get_press,())
    except:
        print("thread error")
        
def printit():            
       start_helper_thread()     
       while True:
        x=chan.voltage-0.5
        temperature=x/0.01
        #thread = threading.Timer(5, printit).start()
        time.sleep(s)
        now= datetime.now()        
        current_time = now.strftime("%H:%M:%S")
        print(current_time,end="")           
                #time.sleep(5)
        end=time.time()
        duration=end-start
        secs=round(duration)
        m, s = divmod(secs, 60)
        h, m = divmod(m, 60)

        print('  {:02d}:{:02d}:{:02d}'.format(h, m, s),end="") 
        print("{:-8.1f} C".format(temperature))
        
        
                
                
def pressBtn():
    
#     global btn_already_pressed;
    global count
    while True:
        
        if(GPIO.input(16)):
          count=1;
          print("logging started")
          now= datetime.now()
          current_time = now.strftime("%H:%M:%S")
          x=chan.voltage-0.5
          temperature=x/0.01
          print("Time      Sys Timer  Temp") #spaces of 4 between words
          print(current_time,end="")
          print("  00:00:00",end="")
          print("{:-8.1f} C".format(temperature))
          printit()
        elif(GPIO.input(16)) and count==1:
          print("logging has stopped")
          time.sleep(2)
          clear()
          sys.exit()
            
pressBtn()
