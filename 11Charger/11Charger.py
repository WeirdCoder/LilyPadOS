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



'''buzzer Interrupt'''
buzzerPin = 1 #TODO define buzzer Pin
def buzzer_callback(gpio_id, value):
    #gpio_id that is triggered.
    #value is 1 for on(5V) and 0 for off (GND).
    x = value #TODO Do something
def watch_buzzer():
    #Start watching the pin, it will report every time the buzzer is turned on, and the next time waiting for 1 second.
    RPIO.add_interrupt_callback(buzzerPin, buzzer_callback, edge='rising',debounce_timeout_ms = 1000)

def unwatch_buzzer():
    RPIO.del_interrupt_callback(buzzerPin)

'''Continue to button code'''

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
