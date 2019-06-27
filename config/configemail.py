
def main(server="", port="", sender="", password="", recipient=""):
    print ('\n=== Configuring Email ===\n')
    if len(server) < 1:
        server = input('Please enter the SMTP Server address.\n For example: \n GMail default is smtp.gmail.com \n Yahoo default is smtp.mail.yahoo.com \n If you don\'t know it, just check with a quick online search: your provider SMTP address \n SMTP Server Address: ')
    else:
        print ("SMTP Server is currently set to {}" .format(server))
        if input("Do you want to change it? \n [yes/no] \n") == "yes":
            server = input("Please enter your new SMTP Server address: \n")
            print ('You entered: {}') .format(server)

    if len(port) < 1:
        port = input('Please enter the port for your SMTP Server.\n Please note that currently only SSL connections are allowed. For example: \n GMail default port is 465 \n Yahoo default is 465 \n If you don\'t know it, just check with a quick online search: your provider SMTP port SSL \n SMTP Port: ')
    else:
        print ("Port is currently set to {}" .format(port))
        if input("Do you want to change it? \n [yes/no] \n") == "yes":
            port = input("Please enter your new SMTP Port: \n")
            print ('You entered: {}') .format(port)

    if len(sender) < 1:
        sender = input('Please enter the sender email address. \n This is the address your raspberry pi will send email from. \n Sender Address: ')
    else:
        print ("Sender email is currently set to {}" .format(sender))
        if input("Do you want to change it? \n [yes/no] \n") == "yes":
            sender = input("Please enter your new sender address: \n")
            print ('You entered: {}') .format(sender)

    if len(password) < 1:
        password = input('Please enter the account password. \n This is the password your raspberry pi uses to login to its email. \n Sender Password: ')
    else:
        print ("Sender password is currently set to {}" .format(password))
        if input("Do you want to change it? \n [yes/no] \n") == "yes":
            password = input("Please enter your new sender password: \n")
            print ('You entered: {}') .format(password)

    if len(recipient) < 1:
        recipient = input('Please enter the recipient email address. \n This is email which will receive notifications. \n Recipient: ')
    else:
        print ("Recipient address is currently set to {}" .format(recipient))
        if input("Do you want to change it? \n [yes/no] \n") == "yes":
            recipient = input("Please enter your new recipient address: \n")
            print ('You entered: {}') .format(recipient)

    return server, port, sender, password, recipient

if __name__ == '__main__':
    main()
else:
    pass
