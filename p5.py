import threading
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

#chanel on pin 1
chan1= AnalogIn(mcp,MCP.P1)

print("Raw ADC Value: ", chan.value)
print("ADC Voltage: " + str(chan.voltage) + "V")
x=chan.voltage-0.5
temperature=x/0.01
print("Runtime    Temp Reading    Temp") #spaces of 4 between words
print("0s    {:-10d} {:-15.1f} C".format(chan1.value,temperature))
start=time.time()
btn_pressed=False
#global count
count=0
interval=[1,5,10]
#global 
s=10 #initially
#s=interval[count]
# if btn_pressed:
#     s=interval[count]
def get_press():
        while True:           
            if(GPIO.input(15)):
                    btn_pressed = True
                    if s==10:
                        s=1
                    elif s==1:
                        s=5
                    else:
                        s=10
                    print(s)
                        
            else:
                btn_pressed=False
                    
                #print("not pressed")
#             if btn_pressed:
#                 global s
#                 print("Pressed")
#                 print(s)
#                 #get_interval()
                             
                
#                 if s==10:
#                         s=1
#                 if s==1:
#                         s=5
#                 if s==5:
#                         s=10
#                 print(s)
        
        
def get_interval():
        
   # global s
    while btn_pressed:

                global s
                
                if s==10:
                        s=1
                if s==1:
                        s=5
                if s==5:
                        s=10
                print(s)
    return s
get_press()
    
def start_helper_thread():
    try:
        thread.start_new_thread(get_press,())
    except:
        print("thread error")
    
def printit():

            
       start_helper_thread()     
       thread = threading.Timer(s, printit).start()   
       x=chan.voltage-0.5
       temperature=x/0.01
       time.sleep(s)
       end=time.time()
       duration=end-start
       sec=round(duration)
        #sec=round(time.perf_counter())
       
       print("{:2d}s".format(sec),end='')
       print("{:-13d} {:-15.1f} C".format(chan1.value,temperature))
        
                    

#printit()
