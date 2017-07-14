import telepot

# Formatting the User Input Message for Telegram

def formatter(usrinput):
    telegram_notification = ""
    for item in usrinput:
        telegram_notification += item
        telegram_notification += "\n"
    return telegram_notification

#Just some output for debugging (Telegram message content, token and chatid)
#logger.debug("Token is %s. Chatid is %s" % (telegram_token, telegram_chatid))
#logger.info('Sending this message via Telegram: %s' % (telegram_notification))
#User Feedback that message is being send

def notification(token, chatid, telegram_notification):
    print 'Telegram message is: %s' % (telegram_notification)
    telegrambot = telepot.Bot(token)
    telegrambot.sendMessage(chatid,str(telegram_notification))
    
if __name__ == "__main__":
    pass