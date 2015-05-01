import RPi.GPIO as GPIO
import json
import socket
import time

HOST = '18.111.46.178'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

dic = {'Thing1': 0, 'Thing2': 0}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN)
#GPIO.setup(27, GPIO.IN)

try:
	while True:
		dic['Thing1'] = GPIO.input(22)
		if GPIO.input(22) == 1:
			dic['Thing2'] = 'herp'
		else:
			dic['Thing2'] = 'derp'
		s.send(json.dumps(dic))
		time.sleep(0.05)
except:
	s.close()
