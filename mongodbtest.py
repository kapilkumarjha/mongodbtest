import pymongo
client = pymongo.MongoClient("mongodb+srv://kapil:kapil@cluster.ah77vag.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name":"sudh",
    "email":"sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)