import threading
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO

#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# def button_callback(channel):
#     print("Button was pushed!")
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BCM) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
# message = input("Press enter to quit\n\n") # Run until someone presses enter
# GPIO.cleanup() # Clean up


# btn=10
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
# while True: # Run forever
#     if GPIO.input(10) == GPIO.HIGH:
#         print("Button was pushed!")

GPIO.setmode(GPIO.BCM)
btn=16
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
  buttonState = GPIO.input(buttonPin)
  if buttonState == False:
#     GPIO.output(ledPin, GPIO.HIGH)
    print("Nothing")
  else:
    print("button pressed")
#     GPIO.output(ledPin, GPIO.LOW)

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
def printit():
      
        thread = threading.Timer(10, printit).start()
#         thread.daemon=True
#         thread.start()
        
        x=chan.voltage-0.5
        temperature=x/0.01
        
        time.sleep(10)
        end=time.time()
        duration=end-start
        sec=round(duration)
        #sec=round(time.perf_counter())
        print("{:2d}s".format(sec),end="")
        print("{:-13d} {:-15.1f} C".format(chan1.value,temperature))
        
                    

printit()
