import BlynkLib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setwarnings(False)

BLYNK_AUTH='a6fj-_7TkJ3rY5KNaptlE7f5hVBEcljg'
blynk=BlynkLib.Blynk(BLYNK_AUTH)

@blynk.VIRTUAL_WRITE(1)
def write_to_pin(pin,value):
  GPIO.output(3,1)
  print('Current V1 value: {}'.format(value))
  
while True:
  blynk.run()
    
  
  #sensor_data=20
  #blynk.virtual_write(1,sensor_data)
  #blynk.virtual_write(pin,25)
# @blynk.VIRTUAL_READ(2)
# def my_user_task():
#     # this widget will show some time in seconds..
#     blynk.virtual_write(2, 45)
#     blynk.virtual_write(3, 50)
# blynk.set_user_task(my_user_task,3000)
