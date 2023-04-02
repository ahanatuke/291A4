import sys
from pymongo import MongoClient


def connectPort():
    portNum = sys.argv[1].strip()
    try:
        int(portNum)
    except:
        print("invalid port number")
        return

    port = 'mongodb://localhost:' + portNum + '/'

    return MongoClient(port)