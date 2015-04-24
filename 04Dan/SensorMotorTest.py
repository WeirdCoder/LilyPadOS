import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
##GPIO.setup(18, GPIO.OUT) ##servo
##GPIO.setup(22, GPIO.OUT) motor
GPIO.setup(16, GPIO.IN) ##button

##pwm = GPIO.PWM(18, 100)
##pwm.start(5)

port = serial.Serial("/dev/ttyACM0", baudrate=9600)

try:
  while True:
    i = GPIO.input(16)
    ##print port.readline()
    port.write(str(i))
    '''
    if i == 0:
      pwm.ChangeDutyCycle(20.0 / 10.0 + 2.5)
    else:
      pwm.ChangeDutyCycle(100.0 / 10.0 + 2.5)
    '''
    time.sleep(0.05)
    
except KeyboardInterrupt:
  GPIO.cleanup()
