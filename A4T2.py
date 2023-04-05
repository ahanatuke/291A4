import bson.json_util
from A4utils import connectPort


def main():
    cli = connectPort()

    cli.drop_database('A4dbEmbed')
    db = cli["A4dbEmbed"]


    songwritersCol = db["songwriterTemp"]
    recordingsCol = db['recordTemp']
    collection = db['SongwritersRecordings']

    with open("recordings.json", encoding='utf-8') as rFile:
        rFileData = rFile.read()
        recordingsFile = bson.json_util.loads(rFileData)

    with open("songwriters.json", encoding='utf-8') as sFile:
        sFileData = sFile.read()
        songwritersFile = bson.json_util.loads(sFileData)


    if isinstance(songwritersFile, list):
        songwritersCol.insert_many(songwritersFile)
    else:
        songwritersCol.insert_one(songwritersFile)

    if isinstance(recordingsFile, list):
        recordingsCol.insert_many(recordingsFile)
    else:
        recordingsCol.insert_one(recordingsFile)

    songwriters = songwritersCol.find()
    for i in songwriters:
        records = recordingsCol.find({'recording_id' : {'$in' : i['recordings']}})
        collection.insert_one({'songwriter_id' : i['songwriter_id'],
                               'fans' : i['fans'],
                               'name' : i['name'],
                               'reputation' : i['reputation'],
                               'recordings' : list(records)})


    songwritersCol.drop()
    recordingsCol.drop()

    cli.close()


main()