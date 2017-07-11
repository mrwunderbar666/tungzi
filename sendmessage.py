import time
import datetime
import sys
import io
import os
import sys
import ConfigParser #config parser for loading local settings

import telepot


#initialising Config parser
config = ConfigParser.ConfigParser()
config

""" INSERT CHECK IF THERE IS ANYTHING IN THE CONFIG.INI AND IF THERE IS ONE AT ALL """

this_dir, this_filename = os.path.split(__file__)
CONFIG_PATH = os.path.join(this_dir, "config.conf")

config.read(CONFIG_PATH) #read config file
config.sections() #getting sections

print "Config File Contains: " 
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

sys_notification = sys.argv[1:] #getting the system arguments from the command line

# Formatting the system argument for telegram

telegram_notification = ""

for item in sys_notification:
    telegram_notification += item
    telegram_notification += "\n"

#Just some testing of output for debugging
print "Token is %s. Chatid is %s" % (telegram_token, telegram_chatid)
print 'Message is: %s' % (telegram_notification)
        
telegrambot = telepot.Bot(telegram_token)

telegrambot.sendMessage(telegram_chatid,str(telegram_notification))