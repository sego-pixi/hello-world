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
global s
#s=interval[count]
# if btn_pressed:
#     s=interval[count]
def get_press():
        while True:           
            if(GPIO.input(15)):
                    btn_pressed = True
            else:            
                    btn_pressed = False
                    print("not pressed")
            if btn_pressed:
                
                #global s
                global count
#                 #count=0
#                 #s=interval[count]
                count+=1
                time.sleep(5)
#                 #if count==3:                       
#                         #count=0
                print(count)
                #update_count()
                
                #count=0
                #get_interval(interval[0])
                
                        
                      
#                     s=interval[count]
#                     count+=1
#                     if count==3:
#                             count=0 
        
def update_count():
        global count
        while btn_pressed:
                
                count+=1
#                 if count==3:                        
#                         count=0
                
                        
        print(count)
        return count
        
        
def get_interval(s):
   # global s
    while btn_pressed:
        
        
        global count
        s=interval[count]
        count+=1
        if count==3:
                count=0
        print(s)
    #count+=1
        print(s)
    return s
get_press()
    
# def start_helper_thread():
#     try:
#         thread.start_new_thread(get_press,())
#     except:
#         print("thread error")
    
# def printit():

            
#        start_helper_thread()     
#        thread = threading.Timer(10, printit).start()   
#        x=chan.voltage-0.5
#        temperature=x/0.01
#        time.sleep(10)
#        end=time.time()
#        duration=end-start
#        sec=round(duration)
#         #sec=round(time.perf_counter())
       
#        print("{:2d}s".format(sec),end='')
#        print("{:-13d} {:-15.1f} C".format(chan1.value,temperature))
        
                    

# printit()
