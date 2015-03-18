import lcm
import time
import menu
from lilylcm import *

lc = lcm.LCM()


'''Menu Definitions
Define Menu structure and what functions are called.
'''
#Main Menu
mainMenu = menu.Menu('Lilypad Module Tester')
options = [{"name":'StateMachine',"function":1},
        {"name":'DataTransmission',"function":2},
        {"name":'Antenna',"function":3},
        {"name":'I2C',"function":4},
        {"name":'Docking',"function":5},
        {"name":'Charger',"function":6},
        {"name":'Anchoring',"function":7}]
mainMenu.addOptions(options)
if __name__ == '__main__':
    mainMenu.open()
