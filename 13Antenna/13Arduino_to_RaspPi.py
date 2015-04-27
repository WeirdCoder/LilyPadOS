print("Welcome to Javier's attempt to make the \nArduino talk to the RaspPi");

import serial
import time


# find the USB serial number
ser = serial.Serial('/dev/tty.usbserial', 9600)

while True:
	print ser.readline()







