import time
#from __future__ import print_function
#import random
import datetime
#from telepot.loop import MessageLoop
#import config
import ConfigParser #config parser for loading local settings
import sys
import io
import telepot
#from telepot.loop import MessageLoop

#initialising Config parser
config = ConfigParser.ConfigParser()
config

""" INSERT CHECK IF THERE IS ANYTHING IN THE CONFIG.INI AND IF THERE IS ONE AT ALL """

config.read("config.ini") #read config file
config.sections() #getting sections

print "Config File Contains:" 
print config.sections() #print sections for debug

# Helper function ConfigSectionMap to write a dictionary config_dict1 from config.ini into python

def ConfigSectionMap(section):
    config_dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            config_dict1[option] = config.get(section, option)
            if config_dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            config_dict1[option] = None
    return config_dict1
    print config_dict1
   
    
telegram_token = ConfigSectionMap("Telegram")['token']
telegram_chatid = ConfigSectionMap("Telegram")['chatid']
#Just some testing of output for debugging
print "Token is %s. Chatid is %s" % (telegram_token, telegram_chatid)
        
telegrambot = telepot.Bot(telegram_token)

telegrambot.sendMessage(telegram_chatid,str(datetime.datetime.now()))