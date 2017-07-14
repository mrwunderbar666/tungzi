"""Email module, supports only SSL connections, optimzed for GMail """

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def body_formatter(usrinput):
    email_body = ""
    for item in usrinput[1:]:
        email_body += item
        email_body += "\n"
    return email_body

def head_formatter(usrinput,fromaddr,toaddr):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = usrinput[0]
    msg.attach(MIMEText(body_formatter(usrinput), 'plain'))
    return msg

def notification(smtp, port, fromaddr, user_pass,toaddr, usrinput):
    server = smtplib.SMTP_SSL(smtp, port)
    server.ehlo()
    server.starttls
    server.ehlo()
    server.login(fromaddr, user_pass)
    text = head_formatter(usrinput, fromaddr, toaddr).as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

if __name__ == "__main__":
    pass