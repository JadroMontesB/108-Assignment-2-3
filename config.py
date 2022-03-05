import pymongo
import certifi


mongo_url = "mongodb+srv://JAMB:sammy123@cluster0.25i0c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile = certifi.where())

db = client.get_database("StarWarsDataBase")