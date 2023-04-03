from pymongo import MongoClient
from A4utils import connectPort
#Q1: Find the ids and names of each songwriter that
# has at least one recording and the number of
#recordings by each such songwriter

def Q1():
    client = connectPort()
    db = client['A4dbNorm']
    swCol = db['songwriters']

    results = swCol.find({"recordings" : {"$not" :{"$size":0}}},{"songwriter_id" : 1, "name" : 1 , "num_recordings" : {"$size" : "$recordings"}})
    for i in list(results):
        print(i)


Q1()