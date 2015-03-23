import lcm
import time
import menu
from lilylcm import *
import threading
lc = lcm.LCM()
'''Success + Failure Dialogue Box
A quick dialogue box that will
'''
#Success Menu
successMenu = menu.Menu('Test Success!  Message Received and correctly typed!')

#Message Sent Menu
messageSentMenu = menu.Menu('Test Message sent')

#Failure Menu
failureMenu = menu.Menu('Message not Received.  Please test if you are broadcasting at the right Channel')

'''LCM Channel listener Function
A function To test whether a LCM data is broadcasted, using multithreading.
'''
def lcmListenTest(channelName, lcmType, pauseSeconds):
    #Setting up multiThreading
    thisLock = threading.Lock()
    thisLock.acquire()
    received = dict()
    received['Received?'] = False
    received['lock'] = thisLock
    def lcmHandler(channel,data):
        try:
            print "Received Data"
            msg = lcmType.decode(data)
            print "decode Successful"
            received['Received?'] = True
            received['lock'].release()
        except Exception:
            return
    subscription = lc.subscribe(channelName, lcmHandler)
    lcmHandleThread = threading.Thread(target=lc.handle)
    lcmHandleThread.setDaemon(True)
    lcmHandleThread.start()
    timerThread = threading.Timer(pauseSeconds, thisLock.release)
    timerThread.start()
    #Begin the wait
    print "Commense wait for %f seconds" % pauseSeconds
    with thisLock:
        if received['Received?']:
            timerThread.cancel()
            successMenu.open()
        else:
            msg = lcmType()
            lc.publish(channelName,msg.encode())
            failureMenu.open()
    lc.unsubscribe(subscription)
'''Menu Definitions
Define Menu structure and what functions are called.
'''
mainMenu = menu.Menu('Lilypad Module Tester')
#StateMachine Menu
stateMachineMenu = menu.Menu('StateMachine Menu')
options = [{"name":'return to Main Menu',"function":mainMenu.open}]
stateMachineMenu.addOptions(options)
#DataTransmission Menu
dataTransferMenu = menu.Menu('DataTransfer Menu')
options = [{"name":'Fetch Data from Plane',"function":1},
        {"name":'Push Mission Data',"function":2},
        {"name":'return to Main Menu',"function":mainMenu.open}]
dataTransferMenu.addOptions(options)
#Antenna Menu
antennaMenu = menu.Menu('Anetenna Box Menu')
options = [{"name":'Test GPS Signal',"function":lambda : lcmListenerTest('POD_GPS',L11GPS,5)},
        {"name":'Test Wind Sensor Signal',"function":lambda : lcmListenerTest('POD_Wind',L13Wind,5)},
        {"name":'return to Main Menu',"function":mainMenu.open}]
antennaMenu.addOptions(options)
#I2C Menu
i2cMenu = menu.Menu('I2C Menu')
options = [{"name":'Test ADC Signal',"function":lambda : lcmListenerTest('POD_Volt', L09Voltage, 5)},
        {"name":'Test Temp and Humidity Sensor Signal',"function":lambda : lcmListenerTest('POD_Temp',L08Temperature,5)},
        {"name":'return to Main Menu',"function":mainMenu.open}]
i2cMenu.addOptions(options)
#Docking Menu
dockingMenu = menu.Menu('Docking Menu')
options = [{"name":'Test Magnet',"function":1},
        {"name":'Test LED',"function":2},
        {"name":'Test Dock Detection Signal',"function":lambda : lcmListenTest('POD_DockDetect',L21DockDetect,5)},
        {"name":'return to Main Menu',"function":mainMenu.open}]
dockingMenu.addOptions(options)
#Charger Menu
chargerMenu = menu.Menu('Charger Menu')
options = [{"name":'Start Charging',"function":1},
        {"name":'Test Completion Signal',"function":2},
        {"name":'return to Main Menu',"function":mainMenu.open}]
chargerMenu.addOptions(options)
#Anchoring Menu
anchoringMenu = menu.Menu('Anchoring Menu')
options = [{"name":'Test Depth Signal Receive',"function":lambda  : lcmListenTest('POD_Depth',L06Depth,5)},
        {"name":'Test Servo',"function":2},
        {"name":'return to Main Menu',"function":mainMenu.open}]
anchoringMenu.addOptions(options)
#Main Menu
options = [{"name":'StateMachine',"function":stateMachineMenu.open},
        {"name":'DataTransmission',"function":dataTransferMenu.open},
        {"name":'Antenna',"function":antennaMenu.open},
        {"name":'I2C',"function":i2cMenu.open},
        {"name":'Docking',"function":dockingMenu.open},
        {"name":'Charger',"function":chargerMenu.open},
        {"name":'Anchoring',"function":anchoringMenu.open},
        {"name":'Exit',"function":exit}]
mainMenu.addOptions(options)

#Success Menu
options = [{"name":'Back to Main Menu',"function":mainMenu.open}]
successMenu.addOptions(options)
#Message Sent Menu
messageSentMenu.addOptions(options)
#Failure Menu
failureMenu.addOptions(options)


if __name__ == '__main__':
    mainMenu.open()
    #lcmListenTest('05EBOLA',L05Ebola,10)
