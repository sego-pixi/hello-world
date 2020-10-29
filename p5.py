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
# if(GPIO.input(15)):
#     btn_pressed = True
# else:
#     btn_pressed = False
    
#         #print("BUtton pressed")
    
# while True:
#     if(GPIO.input(15)):
#         #print("BUtton pressed")
#         btn_pressed = True
#         #GPIO.output(16,1)
#     else:
#         #print("False")
# #         #GPIO.output(16,0)
#         btn_pressed = False
# #         time.sleep(1)


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)


# create the mcp object
mcp = MCP.MCP3008(spi, cs)
1
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

#chanel on pin 1
chan1= AnalogIn(mcp,MCP.P1)

print("Raw ADC Value: ", chan.value)
print("ADC Voltage: " + str(chan.voltage) + "V")
x=chan.voltage-0.5
temperature=x/0.01
print("Runtime    Temp Reading    Temp") #spaces of 4 between words
#print("0s     ",chan1.value,temperature)
print("0s    {:-10d} {:-15.1f} C".format(chan1.value,temperature))
start=time.time()
btn_pressed=False
count=0
interval=[1,5,10]
#global s
if btn_pressed:
    s=interval[count]
def printit():
        
       if(GPIO.input(15)):
            btn_pressed = True
       else:            
            btn_pressed = False
       count=0
       interval=[1,5,10]
       if btn_pressed:
              s=interval[count]
              count+=1
              if count==3:
                     count=0 
       thread = threading.Timer(10, printit).start()   
       x=chan.voltage-0.5
       temperature=x/0.01
       time.sleep(10)
       end=time.time()
       duration=end-start
       sec=round(duration)
        #sec=round(time.perf_counter())
       print(global s)
       print("{:2d}s".format(sec),end='')
       print("{:-13d} {:-15.1f} C".format(chan1.value,temperature))
        
                    

printit()
