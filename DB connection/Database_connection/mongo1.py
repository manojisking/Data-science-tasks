import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://admin:admin@cluster0-k4yhk.mongodb.net/globalwarming?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]

print('Database conected sucessfully')

post1 = {"dt":"1855-05-01", "AverageTemperature":25.544, "AverageTemperatureUncertainty":1.171, "State":"Acre", "Country":"Brazil"}
post2 = {"dt":"1855-06-01", "AverageTemperature":24.228, "AverageTemperatureUncertainty":1.103, "State":"Acre", "Country":"Brazil"}


collection.insert_many([post1, post2]) 

print('data updated sucessfully')







#collection.insert_one(post1) 

#results = collection.find({"Country":"United States"})
#for result in results:
#    print(result)

#result = collection.delete_one({"dt":"1855-05-01"})

#result = collection.update_one({"dt":"1855-06-01"}, {"$set":{"AverageTemperature":50}})


