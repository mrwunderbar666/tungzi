""" Configuration Assistant

"""

import time
#from __future__ import print_function
#import random
import datetime
#from telepot.loop import MessageLoop
#import config
import configparser as ConfigParser #config parser for storing local settings
import sys
import os
import io
import telepot
from telepot.loop import MessageLoop
from telegram.ext import Updater as telegram_Updater
from telegram.ext import CommandHandler as telegram_CommandHandler

import logging #logging module
from operator import contains

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
    logger.debug('Created configuration dictionary: {}' .format(config_dict1))
    return config_dict1

""" Telegram configuration functions """

def check_telegram():
    try:
        ConfigSectionMap('telegram')
        telegram_token = ConfigSectionMap('telegram')['token']
        telegram_chatid = ConfigSectionMap('telegram')['chatid']
        update_telegram(telegram_token, telegram_chatid)
    except Exception:
        new_telegram()

def new_telegram():
    from config import configtelegram
    telegram_token, telegram_chatid = configtelegram.main()
    config['telegram'] = {'token' : telegram_token, 'chatid' : telegram_chatid}
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)
    # cfgfile = open(CONFIG_PATH,'w')
    # config.add_section('telegram')
    # config.set('telegram','token',telegram_token)
    # config.set('telegram','chatid',telegram_chatid)
    # config.write(cfgfile)
    # cfgfile.close()

def update_telegram(telegram_token, telegram_chatid):
    from config import configtelegram
    new_telegram_token, new_telegram_chatid = configtelegram.main(telegram_token, telegram_chatid)
    config['telegram'] = {'token' : new_telegram_token, 'chatid' : new_telegram_chatid}
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)
    # config.set('telegram','token',new_telegram_token)
    # config.set('telegram','chatid',new_telegram_chatid)
    # config.write(cfgfile)
    # cfgfile.close()

""" Email configuration functions """

def check_email():
    try:
        ConfigSectionMap('email')
        email_smtp = ConfigSectionMap('email')['smtpserver']
        email_port = ConfigSectionMap('email')['port']
        email_from = ConfigSectionMap('email')['from']
        email_password = ConfigSectionMap('email')['password']
        email_recipient = ConfigSectionMap('email')['recipient']
        update_email(email_smtp, email_port, email_from, email_password, email_recipient)
    except Exception:
        print('Not found, calling new email function')
        new_email()

def new_email():
    from config import configemail
    email_smtp, email_port, email_from, email_password, email_recipient = configemail.main()
    cfgfile = open(CONFIG_PATH,'w')
    config.add_section('email')
    config.set('email','smtpserver',email_smtp)
    config.set('email','port',email_port)
    config.set('email','from',email_from)
    config.set('email','password',email_password)
    config.set('email','recipient',email_recipient)
    config.write(cfgfile)
    cfgfile.close()

def update_email(email_smtp, email_port, email_from, email_password, email_recipient):
    from config import configemail
    new_email_smtp, new_email_port, new_email_from, new_email_password, new_email_recipient = configemail.main(email_smtp, email_port, email_from, email_password, email_recipient)
    cfgfile = open(CONFIG_PATH,'w')
    config.set('email','smtpserver',new_email_smtp)
    config.set('email','port',new_email_port)
    config.set('email','from',new_email_from)
    config.set('email','password',new_email_password)
    config.set('email','recipient',new_email_recipient)
    config.write(cfgfile)
    cfgfile.close()

def main():

    welcome_message = "=== Welcome === \nWelcome to the TungZi Notification Configuration assistant \nI help you to configure the services that you need to get instant updates from your device. \n"
    available_service_msg = "Currently following Services are available:\n - Email\n - Telegram"
    closing_message = "Configuration complete! \nYou can now send a message by typing 'python sendmessage Test' \nRefer to the online manual for details.\n === Configuration Ends ==="

    print(welcome_message)
    print(available_service_msg)
    selection = input('Which services do you want to configure? \n Type the name of the service \n Your selection: ')
    if 'telegram' in selection.lower():
        check_telegram()
    if 'email' or 'mail' or 'e-mail' in selection.lower():
        check_email()

    print(closing_message)

if __name__ == '__main__':
    main()
else:
    pass
