import telepot

# Formatting the User Input Message for Telegram

def formatter(usrinput):
    telegram_notification = ""
    for item in usrinput:
        telegram_notification += item
        telegram_notification += "\n"
    return telegram_notification

def notification(token, chatid, telegram_notification):
    print 'Telegram message is: %s' % (telegram_notification)
    telegrambot = telepot.Bot(token)
    telegrambot.sendMessage(chatid,str(telegram_notification))
    
if __name__ == "__main__":
    pass