import os
import datetime
import json

""" add error handling """

""" Setting up the main pathing """

def pathing():
    this_dir, this_filename = os.path.split(__file__)
    LOGGING_PATH = os.path.join(this_dir, "logfile.log")
    QUEUE_PATH = os.path.join(this_dir, "queue.json")
    return QUEUE_PATH


def addqueue(usrinput):
    stampdate = datetime.datetime.now().strftime('%Y-%m-%d')
    stamptime = datetime.datetime.now().strftime('%H:%M:%S')
    print ("Trying to open queue file")
    try:
        with open(pathing(), 'r') as f:
            queue = json.load(f)
            print ("Success! Queue file containts: {}" .format(queue))
    except:
        print ("Cannot find Queue File or queue file is empty, creating new one")
        with open(pathing(), 'w') as f:
            json.dump({}, f)
        with open(pathing(), 'r') as f:
            queue = json.load(f)
            print queue
    try:
        queue[stampdate].append({stamptime:usrinput})
        print ("Current date already in JSON, adding new entry")
    except:
        new_entry = {stampdate: [{stamptime:usrinput}]}
        queue.update(new_entry)
        print ("Nothing for today, so I am making a new date entry: {}" .format(new_entry))
    with open(pathing(), 'w') as f:
        json.dump(queue, f, indent=4)
        print ("Saving queue")


def getqueue():
    try:
        with open(pathing(), 'r') as f:
            queue = json.load(f)
            print ("Success! Queue file contains: {}" .format(queue))
            """ Unpack Queue """
            myprint(queue)
            return queue
    except:
        print ("Cannot find Queue File or queue file is empty.")    
        return False


def clearqueue():
    with open(pathing(), 'w') as f:
        json.dump({}, f)
    print ("Queue File cleared")
    return True

def myprint(d):
    for k, v in d.iteritems():
        if isinstance(v, dict):
            myprint(v)
        else:
            print "{0} : {1}".format(k, v)
    
    
#print getqueue()
#print clearqueue()

#usrinput = ["Hello, this is a set of strings", "Two to be exact."]

#addqueue(usrinput)
#print ("Returning Queue:")
#print getqueue()
#import services.sendemail
#my_queue = getqueue()
print getqueue()
#services.sendemail.queue_formatter(my_queue)
#print clearqueue()


#OOP Later: full send class

#class send:
    
#    def __init__(self,service,usrinput):
        

    