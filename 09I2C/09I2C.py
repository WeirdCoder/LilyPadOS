import smbus
import time
from  Adafruit_I2C import Adafruit_I2C
import lcm
#Import LCMTypes
#TODO

#Address of devices
depthAddress = #TODO 
adcAddress = #TODO
tempAddress = #TODO

#Initiate I2C instances
depthI2C = Adafruit_I2C(depthAddress)
adcI2C   = Adafruit_I2C(adcAddress)
tempI2C  = Adafruit_I2C(tempAddress)

##How to Use i2c 
#Writing a list of Byte to a register on device. you can also just put in a single byte
#yourI2C.writeList(register,listOfData)

#Reading a number of byte from a register on a device.
#yourI2C.readList(register,numberOfBytes)


delay = 5
while(true)
    '''  Depth  '''
    msg = ##TODO

    lc.publish("09I2C_DEPTH", msg.encode())

    '''ADC'''
    msg = ##TODO
    
    lc.publish("09I2C_ADC", msg.encode())

    '''Temp/Humidity'''
    msg = ##TODO 

    lc.publish("09I2C_TEMP", msg.encode())

