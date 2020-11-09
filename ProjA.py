import threading
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
from _thread import start_new_thread
#from _thread import _Thread_stop
from datetime import datetime
from os import system, name
import sys
import subprocess, os
import signal
import subprocess

#this is for the start/stop button (Changed pin to 16)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 1
chan = AnalogIn(mcp, MCP.P0)
# while True:    
#   if(GPIO.input(16)):       
#     start=time.time()
start=time.time()
#start=0
print("Press button to start monitoring the sensor")
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
        sys.exit()
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
#btn_already_pressed=False
count=0;

def start_helper_thread():
    try:
        start_new_thread(printit,())
    except:
        print("thread error")
def printit():
    
    x=chan.voltage-0.5
    temperature=x/0.1
    thread = threading.Timer(5, printit).start()
    now= datetime.now()
    time.sleep(5)
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
        #thread = threading.Timer(5, printit).start()  
        #start_helper_thread() 
#         while True:            
                    

              
#printit()

def pressBtn():
    
#     global btn_already_pressed;
    global count
    running=True
    while True:
#     #start_helper_thread() 
#     #complete=False
#     #while complete==False:
        
        if(GPIO.input(16)):
      
      
#             #complete=False
#             #this means button is pressed want to start temp
#             #btn_already_pressed=True
            #start=time.time()
            if count==0:
                print("logging started")
                now= datetime.now()
                current_time = now.strftime("%H:%M:%S")
                x=chan.voltage-0.5
                temperature=x/0.1
                print("Time      Sys Timer  Temp") #spaces of 4 between words
                print(current_time,end="")
                print("  00:00:00",end="")
                print("{:-8.1f} C".format(temperature))
                printit()
                count=1;
            elif count==1:
              print("logging has stopped")
              time.sleep(4)
              clear()            
              print("Logging has stopped you can now exit the program")
              time.sleep(15)
              
#               print("has cleared")
#               running=False
#               exit(0)
#               #thread._Thread_stop()
#               thread.join()
#               break

pressBtn()
