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

BLYNK_AUTH=" 7t6Q72qVqWmrxPWydL0F18TEWejod_7P"
blynk=BlynkLib.Blynk(BLYNK_AUTH)

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
chan = AnalogIn(mcp, MCP.P0)
t=5#initially
start=time.time()
print("Press button to start monitoring the sensor")

@blynk.VIRTUAL_WRITE(1)
def write_to_pin(value):
  print('Current V1 value: {}'.format(value))
  #sensor_data=20
  #blynk.virtual_write(1,sensor_data)
  #blynk.virtual_write(pin,25)
@blynk.VIRTUAL_READ(2)
def my_user_task():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, 45)
    blynk.virtual_write(3, 50)
 
  
  
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
                    print(t)
       
                        
            else:
                btn_pressed=False

              
def start_helper_thread():
    try:
        start_new_thread(get_press,())
    except:
        print("thread error")
        
def printit():     
       global t
       start_helper_thread()     
       while True:
        x=chan.voltage-0.5
        temperature=x/0.1
        #thread = threading.Timer(5, printit).start()
        time.sleep(t)
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
          if count==0:
            
            print("logging started")
            #sensor_data=20
            #blynk.virtual_write(1,sensor_data)
            #write_to_pin(4)
            blynk.run
            now= datetime.now()
            current_time = now.strftime("%H:%M:%S")
            x=chan.voltage-0.5
            temperature=x/0.1
            print("Time      Sys Timer  Temp") #spaces of 4 between words
            print(current_time,end="")
            print("  00:00:00",end="")
            print("{:-8.1f} C".format(temperature))
            count=1
            print("now 1")
            printit()
            
          if count==1:
            print("logging has stopped")
            time.sleep(4)
            clear()              
            print("Logging has stopped you can now exit the program")
            time.sleep(15)
#           count=1;
#           print("logging started")
#           now= datetime.now()
#           current_time = now.strftime("%H:%M:%S")
#           x=chan.voltage-0.5
#           temperature=x/0.1
#           print("Time      Sys Timer  Temp") #spaces of 4 between words
#           print(current_time,end="")
#           print("  00:00:00",end="")
#           print("{:-8.1f} C".format(temperature))
#           printit()
#         elif(GPIO.input(16)) and count==1:
#           print("logging has stopped")
#           time.sleep(2)
#           clear()
#           sys.exit()
            
pressBtn()
