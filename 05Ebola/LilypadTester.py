import lcm
import time
import menu
from lilylcm import *
import threading
lc = lcm.LCM()
'''Success + Failure Dialogue Box
A quick dialogue box that will
'''
'''LCM Channel listener Function
A function To test whether a LCM data is broadcasted, using multithreading.
'''
def lcmListenTest(channelName, lcmType, pauseSeconds):
    #Setting up multiThreading
    thisLock = threading.Lock()
    thisLock.acquire()
    received = False
    def lcmHandler(channel,data):
        try:
            print "Received Data"
            msg = lcmType.decode(data)
            print "decode Successful"
            received = True
            print "released"
            thislock.release()
            print "released"
        except Exception:
            return
        subscription = lc.subscribe(channelName, lcmHandler)
        lcmHandleThread = threading.Thread(target=lc.handle)
        lcmHandleThread.setDaemon(True)
        #lcmHandleThread.start()
        timerThread = threading.Timer(pauseSeconds, thisLock.release)
        timerThread.start()
        #Begin the wait
        print "Commense wait for %f seconds" % pauseSeconds
        with thisLock:
            lc.handle()
            if received:
                timerThread.cancel()
                print "success!"
            else:
                msg = lcmType()
                lc.publish(channelName,msg.encode())
                print "No Message?!"
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
                options = [{"name":'Test GPS Signal',"function":1},
                        {"name":'Test Wind Sensor Signal',"function":2},
                        {"name":'return to Main Menu',"function":mainMenu.open}]
                        antennaMenu.addOptions(options)
                        #I2C Menu
                        i2cMenu = menu.Menu('I2C Menu')
                        options = [{"name":'Test ADC Signal',"function":1},
                        {"name":'Test Temp and Humidity Sensor Signal',"function":2},
                        {"name":'return to Main Menu',"function":mainMenu.open}]
                        i2cMenu.addOptions(options)
                        #Docking Menu
                        dockingMenu = menu.Menu('Docking Menu')
                        options = [{"name":'Test Magnet',"function":1},
                                {"name":'Test LED',"function":2},
                                {"name":'Test Dock Detection Signal',"function":3},
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
                                options = [{"name":'Test Depth Signal',"function":1},
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
                                        if __name__ == '__main__':
                                            #mainMenu.open()
                                            print "hello"
                                            lcmListenTest('05EBOLA',L05Ebola,10)
