import lcm
import time

#import LCM type

#Define Variables
IDLE = 1
SURFACE = 2
WAIT = 3
BEGIN = 4
READY = 5
DOCKED = 6
CHARGING = 7

initTime = time.time()*1000000
startTime = 60*10 #in seconds  currently: 10 minutes
depth = 100
pingReceived = False
dockingReady = False
docked = False


#Define starting State

currentState = 0


#Define Transition State
def transIdle():
    x =1



#Main Loop
try:
    print 'State Machine Start and Running'
    #while True:
        #update with input
    #    lc.handle()
        #Case Switch
    #    currentState = transitionModel(currentState)
        #State Iteration

        #publish State

        #Pet Watchdog

except Keyboardinterrupt:
    pass


