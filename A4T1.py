import bson.json_util
from pymongo import MongoClient
import sys
import json
from A4utils import connectPort


def main():
    cli = connectPort()

    db = cli["A4dbNorm"]

    recordingsCol = db["recordings"]
    songwritersCol = db["songwriters"]

    with open("recordings.json", encoding='utf-8') as rFile:
        rFileData = rFile.read()
        recordingsFile = bson.json_util.loads(rFileData)

    with open("songwriters.json", encoding='utf-8') as sFile:
        sFileData = sFile.read()
        songwritersFile = bson.json_util.loads(sFileData)


    if isinstance(recordingsFile, list):
        recordingsCol.insert_many(recordingsFile)
    else:
        recordingsCol.insert_one(recordingsFile)

    if isinstance(songwritersFile, list):
        songwritersCol.insert_many(songwritersFile)
    else:
        songwritersCol.insert_one(songwritersFile)

    cli.close()



main()