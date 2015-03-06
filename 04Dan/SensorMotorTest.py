import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
##GPIO.setup(18, GPIO.OUT) servo
##GPIO.setup(22, GPIO.OUT) motor
GPIO.setup(16, GPIO.IN) ##button

try:
  while True:
    i = GPIO.input(16)
    print(i)
    delay(1000)
except Keyboardinterrupt:
  GPIO.cleanup()
