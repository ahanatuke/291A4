import sys
from pymongo import MongoClient


def connectPort():
    if len(sys.argv) > 1:
        portNum = sys.argv[1].strip()
        try:
            int(portNum)
        except:
            print("invalid port number")
            return

    else:
        portNum = '27017'
    port = 'mongodb://localhost:' + portNum + '/'

    return MongoClient(port)