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
              time.sleep(2)
              clear() 
              print("has cleared")
              exit()
              #thread._Thread_stop()
              thread.join()
              break
#             print("logging started")
#             count=1
#             now= datetime.now()
#             current_time = now.strftime("%H:%M:%S")
#             x=chan.voltage-0.5
#             temperature=x/0.01
#             print("Time      Sys Timer  Temp") #spaces of 4 between words
#             print(current_time,end="")
#             print("  00:00:00",end="")
#             print("{:-8.1f} C".format(temperature))
#             printit()
#         if(GPIO.input(16)) and count==1:
            
#             print("logging has stopped")
#             time.sleep(2)
#             clear() 
#             sys.exit()
            #os.killpg(p.pid, signal.SIGTERM)
            #subOut = subprocess.Popen(['your', 'subprocess', ...], preexec_fn=os.setgrp)

# when it's time to kill
            #os.killpg(os.getpgid(subOut.pid), signal.SIGTERM)
#             _thread.join()
#             cleanup_stop_thread()
            #sys.exit()
            #complete=True
#             break
        
#         else:
#             if (not btn_already_pressed):
                
#                 print("Press button to start monitoring the sensor")
#                 time.sleep(5)
            ##clear screen
            
            #print("logging has stopped")
            #time.sleep(2)
            #clear()
#GPIO.cleanup() # release pins from this operation
#time.sleep(1)#allow all the threads to finish
pressBtn()
