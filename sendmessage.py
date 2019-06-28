import time
import datetime
import sys
import io
import os
import ConfigParser #config parser for loading local settings
import argparse

#import telepot #telegram support with telepot module

import logging #logging module

""" Setting up the main pathing """
this_dir, this_filename = os.path.split(__file__)
LOGGING_PATH = os.path.join(this_dir, "logfile.log")
CONFIG_PATH = os.path.join(this_dir, "config.conf")


""" Setting up logging
    all messages processed by this script will be stored in a log file for easy review at another place """

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(LOGGING_PATH)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

""" Setting System arguments """

parser = argparse.ArgumentParser(description='TungZi Notification Script - BETA')
parser.add_argument('-t','--telegram', help='Use Telegram for your notification', action='store_true')
parser.add_argument('-e','--email',help='Use Email for your notification', action='store_true')
parser.add_argument('--queue',help='Add your message to the queue and send it later', action='store_true')

opts, usr_input_message = parser.parse_known_args()
check_opts = vars(opts)
print parser.parse_known_args()
print opts
print check_opts

""" Getting usr_input_messagetem arguments """

def check_input_message():
    if usr_input_message: 
        print('Your input message is: %s' % usr_input_message)
        logger.info('User input message: %s' % usr_input_message)
        return True
    else: 
        print ('No message so I am sending a random gif')
        logger.info('No message so I am sending a random gif')
        return False
    

#initialising Config parser
config = ConfigParser.ConfigParser()
config

""" INSERT CHECK IF THERE IS ANYTHING IN THE CONFIG.INI AND IF THERE IS ONE AT ALL """

config.read(CONFIG_PATH) #read config file
config.sections() #getting sections

#print sections for debug
logger.debug('Config File Contains: {}' .format(config.sections()))

# Helper function ConfigSectionMap to write a dictionary config_dict1 from config.ini into python

def ConfigSectionMap(section):
    config_dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            config_dict1[option] = config.get(section, option)
            if config_dict1[option] == -1:
                logger.debug("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            config_dict1[option] = None
    return config_dict1
   
""" Function to compare User Input with Config Sections, to ensure that selected service is 
    configured
"""

common = []
not_common = []

def config_comparator():
    for k,v in check_opts.iteritems():
        if v == True and k in config.sections():
            common.append(k)
        else:
            not_common.append(k)
    return common and not_common

""" Functions to get the options selected by the user 
"""

def check_queue():
    if opts.queue:
        import addqueue
        addqueue.addqueue(usr_input_message)
        print ('Adding to queue')
        return True
    #elif opts.sendqueue
    else:
        print ('not adding to queue')
        return False

def get_services():
        if any(check_opts.values()) == True:
            print ('At least one service is selected')
            logger.debug('At least one service is selected, so let\'s check which one')
            logger.info('Got following arguments from system input: {}' .format(opts)) #send the system arguments directly to the log file
            config_comparator()
            print common
            #print not_common
            return True
        else: 
            print ('All services are selected')
            logger.debug('No user input argument, so all services are selected')
            return False

""" testing validity of function """


""" Comparing User Input with config sections, 
making sure all requested services are properly configured """

def send_now():
    if common.__contains__('telegram') or all_serv == True:
        from services import sendtelegram
        logger.debug('Sending Message via Telegram. User Input: {} . Configurations in Following lines'.format(usr_input_message))
        logger.debug('Config File Telegram Token{}' .format(ConfigSectionMap("telegram")['token']))
        logger.debug('Config File Telgram Chatid {}' .format(ConfigSectionMap("telegram")['chatid']))
        sendtelegram.notification(ConfigSectionMap("telegram")['token'], ConfigSectionMap("telegram")['chatid'], sendtelegram.formatter(usr_input_message))
    if common.__contains__('email') or all_serv == True:
        from services import sendemail
        logger.debug('Sending Message via Email. User Input: {} . Configurations in Following lines'.format(usr_input_message))
        logger.debug('Config File Email SMTP {}' .format(ConfigSectionMap("email")['smtpserver']))
        logger.debug('Config File Email Port {}' .format(ConfigSectionMap("email")['port']))
        logger.debug('Config File Email From {}' .format(ConfigSectionMap("email")['from']))
        logger.debug('Config File Email Password {}' .format(ConfigSectionMap("email")['password']))
        logger.debug('Config File Email Recipient {}' .format(ConfigSectionMap("email")['recipient']))
        sendemail.notification(ConfigSectionMap("email")['smtpserver'], ConfigSectionMap("email")['port'], ConfigSectionMap("email")['from'], ConfigSectionMap("email")['password'], ConfigSectionMap("email")['recipient'], usr_input_message)
        
        
check_input_message()
all_serv = False

if check_queue() == False:
    if get_services() == False:
        all_serv = True
        print ('Yes, I am sending to all')
    else:
        print ('I am sending to {}' .format(opts))
    send_now()
else:
    print ("Added to queue: {}" .format(usr_input_message))


