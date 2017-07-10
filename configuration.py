""" Configuration File

"""

import time
#from __future__ import print_function
#import random
import datetime
#from telepot.loop import MessageLoop
#import config
import ConfigParser #config parser for storing local settings
import sys
import os
import io
import telepot
from telepot.loop import MessageLoop

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

# Helper function ConfigSectionMap to write a dictionary config_dict1 from config.conf into python

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
   
#Just some testing of output for debugging
    
telegram_token = ConfigSectionMap("Telegram")['token']
telegram_chatid = ConfigSectionMap("Telegram")['chatid']
print "Token is %s. Chatid is %s" % (telegram_token, telegram_chatid)
email_smtpserver = ConfigSectionMap("Email")['smtpserver']
print email_smtpserver

# Configuration function for telegram

def telegram_token_configuration():
    telegram_token = ConfigSectionMap("Telegram")["token"]
    if len(telegram_token) > 1:
        print "Token is %s." % (telegram_token) 
        #telegram_bot = telepot.Bot(telegram_token)
        return True #telling us that telegram is configured
    else:
        print 'Telegram Token is not defined'
        telegram_token = raw_input("Please enter your Telegram Token: ")
        cfgfile = open("config.ini",'w')
        #config.add_section('Telegram')
        config.set('Telegram','token',telegram_token)
        #Config.set('Person','Age', 50)
        config.write(cfgfile)
        cfgfile.close()
        
# Helper Function to listen to command /register, this will return the chat ID and store it in the config file
        
def handle(msg):
    command = msg['text']
    return command
    

# main function to check if there is a chatID

def telegram_chatid_configuration():
    telegram_bot = telepot.Bot(telegram_token)
    telegram_chatid = ConfigSectionMap("Telegram")["chatid"]
    if len(telegram_chatid) > 1:
        print "ChatID is %s." % (telegram_chatid)
        return True
    else:
        print "ChatID is not set"
        return False


telegram_token_configuration()
if telegram_chatid_configuration() == False:
    #MessageLoop(telegram_bot, get_chatid).run_as_thread()
    telegram_bot = telepot.Bot(telegram_token)
    print('Type /register to your Telegram Bot. I am listening for 20 seconds')
    MessageLoop(telegram_bot, handle).run_as_thread()
    time.sleep(20)
    #if command == '/register':
    #    telegram_chatid = msg['chat']['id']
    print "Time is up"

