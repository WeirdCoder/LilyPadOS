import RPi.GPIO as GPIO
import time

stop = time.time() + 30
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT) #This will be the enter button
GPIO.setup(17, GPIO.OUT) #Decrease button
GPIO.setup(27, GPIO.OUT) #Increase button
GPIO.setup(22, GPIO.OUT) #Battery type 

GPIO.output(26, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)


button = "Start"

while button != "Stop":
    button = input("Press a button: ")
    if button == "E":
        GPIO.output(26, GPIO.HIGH)
	time.sleep(1) # delays for 5 seconds
        GPIO.output(26, GPIO.LOW)
    if button == "D":
        GPIO.output(17, GPIO.HIGH)
	time.sleep(1) # delays for 5 seconds
        GPIO.output(17, GPIO.LOW)
    if button == "I":
        GPIO.output(27, GPIO.HIGH)
	time.sleep(1) # delays for 5 seconds
        GPIO.output(27, GPIO.LOW)
    if button == "B": 
        GPIO.output(22, GPIO.HIGH)
	time.sleep(1) # delays for 5 seconds
	GPIO.output(22, GPIO.LOW)


 
GPIO.output(26, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
