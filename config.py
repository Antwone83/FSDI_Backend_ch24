import pymongo
import certifi

mongo_url = "mongodb+srv://student:1234qwerASDF@cluster0.cmiux.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

# get the specific database
db  = client.get_database("eveandadamadultstore")