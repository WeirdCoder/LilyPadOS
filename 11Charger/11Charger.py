import RPi.GPIO as GPIO
import time
import lcm
import os
from lilylcm import L16ChargerCommand

lc = lcm.LCM()

top = time.time() + 30
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
   


'''This is Parallel Manual control'''
#import Tkinter as tk
#ef keypress(event):
#   if event.keysym == 'Escape':
#       root.destroy()
#   x = event.char
#   if x == "e":
#       GPIO.output(26, GPIO.HIGH)
#       time.sleep(1) # delays for 5 seconds
#       GPIO.output(26, GPIO.LOW)
#   
#   elif x == "i":
#       GPIO.output(27, GPIO.HIGH)
#       time.sleep(1) # delays for 5 seconds
#       GPIO.output(27, GPIO.LOW)
#      
#   elif x == "d":
#       GPIO.output(17, GPIO.HIGH)
#       time.sleep(1) # delays for 5 seconds
#       GPIO.output(17, GPIO.LOW)
#      
#   elif x == "b":
#       GPIO.output(22, GPIO.HIGH)
#       time.sleep(1) # delays for 5 seconds
#       GPIO.output(22, GPIO.LOW)


#   elif x == "c":
#       GPIO.output(26, GPIO.HIGH)
#       time.sleep(10) # delays for 5 seconds
#       GPIO.output(26, GPIO.LOW)

#   else:
#       pass 

#oot = tk.Tk()
#oot.bind_all('<Key>', keypress)
# don't show the tk window



#root.withdraw()
#oot.mainloop() # you must press escape to exit the key mode

#ef myhandler(channel, data):
#   print("Received message from 02")
#   msg = L16ChargerCommand.decode(data) #Input Msg from StateMachine
#   lc.publish("03CITIRUS", msg.encode())

#ubscription = lc.subscribe("16CHARGERCOMMAND", myhandler)

# lc.publish("03CITIRUS", msg.encode())

#try:
#  while True:
#     lc.handle()
#  except Keyboardinterrupt:
#     pass

#f msg == "START":
#   GPIO.output(26, GPIO.HIGH)
#   time.sleep(2) # delays for 5 seconds
#   GPIO.output(26, GPIO.LOW)
#lif msg == "STOP":
#   GPIO.output(26, GPIO.HIGH)
#   time.sleep(1) # delays for 5 seconds
#   GPIO.output(26, GPIO.LOW)
#lse: 
#   pass       
'''buzzer Interrupt'''
#buzzerPin = 1 #TODO define buzzer Pin
#def buzzer_callback(gpio_id, value):
    #gpio_id that is triggered.
    #value is 1 for on(5V) and 0 for off (GND).
#    x = value #TODO Do something
#def watch_buzzer():
#    #Start watching the pin, it will report every time the buzzer is turned on, and the next time waiting for 1 second.
#    RPIO.add_interrupt_callback(buzzerPin, buzzer_callback, edge='rising',debounce_timeout_ms = 1000)

#def unwatch_buzzer():
#    RPIO.del_interrupt_callback(buzzerPin)

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
#oot.withdraw()
#oot.mainloop() # you must press escape to exit the key mode


