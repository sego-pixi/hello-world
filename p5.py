import threading
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

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
#print("new value: ",chan1.value)
voltage=chan.value*5
voltage/=1024.0
x= voltage-0.5
temperature=x/0.01
print("Runtime    Temp Reading    Temp") #spaces of 4 between words
def printit():
        threading.Timer(10, printit).start()
        sec=round(time.time())
        print("{:2d}s".format(sec),end="")
        print("{:-10d} {:-17.1f} C".format(chan.value,temperature))
        
                    

printit()
