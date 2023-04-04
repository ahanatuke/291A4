from pymongo import MongoClient
from A4utils import connectPort
# Q3: Find the sum of the length of all recordings
# for each songwriter along with the songwriter’s id.

def Q3():
    client = connectPort()

    db = client['A4dbEmbed']
    swCol = db['SongwritersRecordings']

    results = swCol.aggregate(
        [
            {
                '$unwind': '$recordings'
            },
            {
                '$group': {
                    '_id' : '$_id',
                    'total_length': {'$sum': '$recordings.length'},
                    'songwriter_id': {'$first': '$songwriter_id'}
                }
            }
        ]
    )

    for i in list(results):
        print(i)

    client.close()


Q3()