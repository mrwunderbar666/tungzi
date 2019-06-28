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

def queue_formatter(queue):
    datestamps = []
    dictlist = []
    print queue
    for d in queue.keys():
        #print d, v
        datestamps += [str(d)]
        print d
    print datestamps
    #for k,i in datestamps:
    #    print queue[k][i]
    print "Items: ", queue.items()
    print "Datestamps[0]: ", datestamps[0]
    print 'Queue[datestamps[0]]: ', queue[datestamps[0]]
    print 'Queue[datestamps[0]][0]: {}', str(queue[datestamps[0]][0])
    my_string = str(queue[datestamps[0]][0])
    print 'my_string: ', my_string
    for key, value in queue.iteritems():
            temp = [key,value]
            dictlist.append(temp)
    print dictlist    
    print 'another try'
    myprint(queue)
    print '---'
    print "Keys: ", queue.keys()
    print "Values: ", queue.values()


def myprint(d):
    for k, v in d.iteritems():
        if isinstance(v, dict):
            myprint(v)
        else:
            print "{0} : {1}".format(k, v)

if __name__ == "__main__":
    pass