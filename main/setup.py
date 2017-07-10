""" Setup File

"""

import time
#from __future__ import print_function
#import random
import datetime
#from telepot.loop import MessageLoop
#import config
import ConfigParser #config parser for storing local settings
import sys
import io
import telepot
from telepot.loop import MessageLoop

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
        telegram_token = raw_input("Please enter your Telegram Token")
        cfgfile = open("config.ini",'w')
        #config.add_section('Telegram')
        config.set('Telegram','token',telegram_token)
        #Config.set('Person','Age', 50)
        config.write(cfgfile)
        cfgfile.close()
        
# Helper Function to listen to command /register, this will return the chat ID and store it in the config file
        
def get_chatid(msg):
    telegram_chat_id = msg['chat']['id']
    command = msg['text']
    telegram_bot = telepot.Bot(telegram_token)

    print 'Got command: %s' % command

    if command == '/register':
        telegram_bot.sendMessage(telegram_chat_id, "Successfully Registered")
        print "Chat ID is %s" % telegram_chat_id
        #print msg
        cfgfile = open("config.ini",'w')
        #config.add_section('Telegram')
        config.set('Telegram','chatid',telegram_chat_id)
        #Config.set('Person','Age', 50)
        config.write(cfgfile)
        cfgfile.close()
        #get_chatid_status = True
        return True
    
    elif command != '/register':
        telegram_bot.sendMessage(telegram_chat_id, "Not registered")
        #get_chatid_status = False
        return False
    else:
        #get_chatid_status = False
        return False        

# main function to check if there is a chatID

def telegram_chatid_configuration():
    telegram_bot = telepot.Bot(telegram_token)
    telegram_chatid = ConfigSectionMap("Telegram")["chatid"]
    if len(telegram_chatid) > 1:
        print "ChatID is %s." % (telegram_chatid)
        return True
    else:
        print "ChatID is not set"
        MessageLoop(telegram_bot, get_chatid).run_as_thread()
        print('Type /register to your Telegram Bot. I am listening for 10 seconds')
        time.sleep(10)
        print "Time is up"

telegram_token_configuration()
telegram_chatid_configuration()

""" Check if Chat ID Config worked or not
if telegram_chatid_configuration() != True:
    print "retry"
    telegram_chatid_configuration()
    
    """
    


