import telepot
from telepot.loop import MessageLoop
from telegram.ext import Updater
from telegram.ext import CommandHandler

def token_checker(token):
    if len(token) > 1:
        return True
    else:
        return False

def chatid_checker(chatid):
    if len(chatid) > 1:
        return True
    else:
        return False

def token_set():
    print('telegram Token is not defined')
    #logger.debug("Telegram Token is not defined")
    token = input("Please enter your Telegram Token: ")
    #logger.debug("User Input: %s." % (telegram_token))
    return token

def token_replace(token):
    print("Token is currently set to: %s." % (token) )
    #logger.debug("Token is currently set to %s." % (telegram_token))
    confirm = input("Do you want to change the token? [yes/no] \n")
    if confirm == 'yes':
        token = input('Please Enter your new token: \n')
        return token
    else:
        return token #telling us that telegram token is configured and should be unchanged
    return token


# Helper Function to listen to command /register, this will return the chat ID and return it

def register(bot, update):
    #logger.debug("Telegram Bot is running and waiting for register command")
    bot.send_message(chat_id=update.message.chat_id, text="You have successfully registered")
    #logger.debug("Telegram registration successful, got following chatid: %s." % (update.message.chat_id))
    global register_checker
    register_checker = False
    global telegram_chatid
    telegram_chatid = update.message.chat_id
    return register_checker

def chatid_register(token):
    telegram_token = token
    telegram_updater = Updater(token=telegram_token)
    telegram_dispatcher = telegram_updater.dispatcher
    telegram_register_handler = CommandHandler('register', register)
    telegram_dispatcher.add_handler(telegram_register_handler)
    global register_checker
    register_checker = True
    print('Type /register to your Telegram Bot \n Telegram is listening for 10 seconds')
    #logger.debug("Prompting user to register at Telegram Bot")
    while register_checker:
        telegram_updater.start_polling()
    print ("You have successfully registered. \n Please wait...")
    telegram_updater.stop()
    print ("Telegram is now ready!")
    global telegram_chatid
    return telegram_chatid

def main(token="", chatid=""):
    print ('\n=== Configuring Telegram ===\n')
    if not token_checker(token) == True and not chatid_checker(chatid) == True: #if no token is defined and no chatid, then create through user
    #if len(token) < 0 and len(chatid) < 0: #if no token is defined and no chatid, then create through user
        print ("No token and no chatid")
        token = token_set()
        chatid = chatid_register(token)
    elif token_checker(token) == True or chatid_checker == True: #if a token or a chatid is defined ask user to change
        token = token_replace(token)
        chatid = chatid_register(token)
    return token, chatid

if __name__ == '__main__':
    main()
else:
    pass
