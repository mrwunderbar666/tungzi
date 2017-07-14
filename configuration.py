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
from telegram.ext import Updater as telegram_Updater
from telegram.ext import CommandHandler as telegram_CommandHandler

import logging #logging module

""" Setting up the main pathing """
this_dir, this_filename = os.path.split(__file__)
CONFIG_PATH = os.path.join(this_dir, "config.conf")
LOGGING_PATH = os.path.join(this_dir, "logfile.log")


""" Setting up logging
    all messages processed by this script will be stored in a log file for easy review at another place """

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(LOGGING_PATH)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#initialising Config parser
config = ConfigParser.ConfigParser()
config

""" INSERT CHECK IF THERE IS ANYTHING IN THE CONFIG.INI AND IF THERE IS ONE AT ALL """


config.read(CONFIG_PATH) #read config file
config.sections() #getting sections

#print sections for debug
logger.debug('Config File Contains: {}' .format(config.sections()))

# Helper function ConfigSectionMap to write a dictionary config_dict1 from config.conf into python

def ConfigSectionMap(section):
    config_dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            config_dict1[option] = config.get(section, option)
            if config_dict1[option] == -1:
                logger.debug("skip: %s" % option)
        except:
            logger.debug("exception on %s!" % option)
            config_dict1[option] = None
    return config_dict1
    logger.debug('Created configuration dictionary: {}' .format(config_dict1))
   
#Just some testing of output for debugging
    
telegram_token = ConfigSectionMap("telegram")['token']
telegram_chatid = ConfigSectionMap("telegram")['chatid']
logger.debug("Token is %s. Chatid is %s" % (telegram_token, telegram_chatid))
email_smtpserver = ConfigSectionMap("Email")['smtpserver']
logger.debug("Email SMTP Server is: %s" % (email_smtpserver))

# Configuration function for telegram

def telegram_token_configuration():
    telegram_token = ConfigSectionMap("telegram")["token"]
    if len(telegram_token) > 1:
        print "Token is currently set to %s." % (telegram_token) 
        logger.debug("Token is currently set to %s." % (telegram_token))
        return True #telling us that telegram is configured
    else:
        print 'telegram Token is not defined'
        logger.debug("Telegram Token is not defined")
        telegram_token = raw_input("Please enter your Telegram Token: ")
        logger.debug("User Input: %s." % (telegram_token))
        cfgfile = open(CONFIG_PATH,'w')
        #config.add_section('Telegram')
        config.set('telegram','token',telegram_token)
        config.write(cfgfile)
        cfgfile.close()

# main function to check if there is a chatID

def telegram_chatid_configuration():
    telegram_chatid = ConfigSectionMap("telegram")["chatid"]
    if len(telegram_chatid) > 1:
        print "The ChatID is currently set to %s." % (telegram_chatid) 
        logger.debug("The ChatID is currently set to %s." % (telegram_chatid))
        return True
    else:
        print "ChatID is not set"
        logger.debug("The ChatID is not set")
        return False

telegram_token_configuration()

# Helper Function to listen to command /register, this will return the chat ID and store it in the config file


def telegram_register(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="You have successfully registered")
    logger.debug("Telegram registration successful, got following chatid: %s." % (update.message.chat_id))
    cfgfile = open(CONFIG_PATH,'w')
    config.set('telegram','chatid',update.message.chat_id)
    config.write(cfgfile)
    cfgfile.close()
    global register_checker
    register_checker = False
    telegram_chatid = update.message.chat_id
    return register_checker


if telegram_chatid_configuration() == False:
    telegram_token = ConfigSectionMap("telegram")['token']
    telegram_updater = telegram_Updater(token=telegram_token)
    telegram_dispatcher = telegram_updater.dispatcher
    telegram_register_handler = telegram_CommandHandler('register', telegram_register)
    telegram_dispatcher.add_handler(telegram_register_handler)
    register_checker = True
    print('Type /register to your Telegram Bot')
    logger.debug("Prompting user to register at Telegram Bot")
    while register_checker:
        telegram_updater.start_polling()
    print "You have successfully registered"
    telegram_updater.stop()
    print "Telegram is now ready!"
    logger.debug("Telegram Configuration complete")    
   
