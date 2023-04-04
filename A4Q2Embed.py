from pymongo import MongoClient
from A4utils import connectPort
# Q2: Write a query to get the average rhythmicality
# for all recordings that have a recording_id beginning
# with “70”.


def Q2():
    client = connectPort()
    db = client['A4dbEmbed']
    collection = db['SongwritersRecordings']

    results = collection.aggregate(
        [
            {
                "$unwind" : "$recordings"
            },
            {"$match":
                 {"recordings.recording_id" : {"$regex" :"^70"} }
            },
            {
                "$group":
                    {
                        "_id": " ",
                        "avg_rhythmicality": {"$avg": "$recordings.rhythmicality"},
                    }
            }]
    )

    print(list(results))

    client.close()

Q2()