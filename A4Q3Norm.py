from pymongo import MongoClient
from A4utils import connectPort
# Q3: Find the sum of the length of all recordings
# for each songwriter along with the songwriter’s id.

def Q3():
    #client = connectPort()
    client = MongoClient() #todo fix me for hand in

    db = client['A4dbNorm']
    swCol = db['songwriters']

    '''  results = swCol.aggregate(
        [
            {"$match":
                 {"recordings" : {"$not" : {"$size" : 0}} }
             },
            {
            "$project" :
                {
                    "_id" : "$_id" ,
                    "total_length" : {"$sum" : "$recordings"},
                   # "songwriter_id" : {"$first" : "$songwriter_id"},
                    #"songwriter": {"$first": "$name"},
                    "num_records": {"$size":"$recordings"},
                    "recordings":1

                }
                $lookup:
    #{
    #    from: <collection to join>,
    #    localField: <field from the input documents>,
    #     foreignField: <field from the documents of the "from" collection>,
    #    as: <output array field>
    #   }
        }]
    )'''

    results = swCol.aggregate(
        [{
            "$unwind" :
                {"$recordings"}
        },
        {
            "$lookup" : {
                "from" : "recordings" ,
                "localField" : "recordings",
                "foreignField" : "recording_id",
                "as" : "recordings"
            }
        },
        {
            "$group" :
                {
                    "_id" : "$songwriter_id",
                    #"songwriter_id" : {"$first" : "$songwriter_id"},
                    "total_length" : {"$sum" : "$recordings.length"},
                    "plsplspls" : {"$first" : "$recordings.length"}
                }
        }]
    )


    for i in list(results):
        print(i)


Q3()