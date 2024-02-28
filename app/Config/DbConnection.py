from pymongo.mongo_client import MongoClient

def dbConnection():
    uri = "mongodb+srv://pratiyush:mj2nwiVgwDXIU0zx@cluster0.v8w7csn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)




