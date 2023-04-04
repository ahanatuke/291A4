from pymongo import MongoClient
from A4utils import connectPort
import datetime
# Q4: For each recording that was issued after
# 1950-01-01, find the recording name, songwriter name
# and recording issue date.

def Q4():
    client = connectPort()

    db = client['A4dbEmbed']
    swCol = db['SongwritersRecordings']

    results = swCol.aggregate(
        [
            {
                '$unwind': '$recordings'
            },
            {
                '$match' : {
                    'recordings.issue_date': {'$gte': datetime.datetime(1950,1,1,0)}
                }
            },
            {
                '$group': {
                    '_id': '$_id',
                    'name': {'$first': '$name'},
                    'r_name' : {'$first' : '$recordings.name'},
                    'r_issue_date' : {'$first' : '$recordings.issue_date'}
                }
            }
        ]
    )

    for i in list(results):
        print(i)

    client.close()

Q4()