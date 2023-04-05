from A4utils import connectPort
# Q2 :Write a query to get the average rhythmicality
# for all recordings that have a recording_id beginning
# with “70”.


def Q2():
    client = connectPort()

    db = client['A4dbNorm']
    rcCol = db['recordings']

    results = rcCol.aggregate(
        [
            {"$match":
                 {"recording_id" : {"$regex" :"^70"} }
             },
            {
            "$group" :
                {
                    "_id" : "" ,
                    "avg_rhythmicality" : {"$avg" : "$rhythmicality"},
                }
        }]
    )
    for i in list(results):
        print(i)

    client.close()

Q2()