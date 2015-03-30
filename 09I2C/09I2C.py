import smbus
import time 
from HIH6130.io import HIH6130
from  Adafruit_I2C import Adafruit_I2C
from Adafruit_ADS1x15 import ADS1x15
import lcm
#Import LCMTypes


from lilylcm import L07Humidity
from lilylcm import L08Temperature 
from lilylcm import L09Voltage
lc = lcm.LCM('udpm://239.255.76.67:7667?ttl=1')



#Address of devices

adcAddress = 0x48
tempAddress = 0x27
humidityAdress = 0x27

#Initiate I2C instances
humidityI2C = HIH6130()
adcI2C   = ADS1x15(adcAddress)
tempI2C  = HIH6130()

'''How to Use i2c 
Writing a list of Byte to a register on device. you can also just put in a single byte
yourI2C.writeList(register,listOfData)

Reading a number of byte from a register on a device.
yourI2C.readList(register,numberOfBytes)

There are also various read and write types like for just a single bit (Remember that a byte consist of 8 bits.)  And also always search for 3rd party codes.  If you can get 3rd party code that does the i2C readout for you, do it!
'''

delay = 5
while (True):
    print 'running'
    '''  Humidity  '''
    humidityI2C.read()
    msg = L07Humidity()
    msg.humidity = float(humidityI2C.rh) 
    print msg.humidity
    print lc.publish("09I2C_HUMIDITY", msg.encode())

    '''ADC'''
    msg = L09Voltage()
    pga = 6144
    spa = 8
    msg.analogValue = [adcI2C.readADCDifferential01(pga, spa), 1.1, 2.2, 3.3, 1.1, 2.2, 3.3, 4.4]
    # print msg.analogValue
    lc.publish("09I2C_ADC", msg.encode())

    '''Temp'''
    tempI2C.read()
    msg = L08Temperature()
    msg.temperature = float(tempI2C.t)
    # print msg.temperature 
    lc.publish("09I2C_TEMP", msg.encode())
    
    #time.sleep(delay)
    
