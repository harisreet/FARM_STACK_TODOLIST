import pymongo
import certifi

MONGODB_URI = 'mongodb+srv://HARISREE:sree3135@cluster0.t5ahsvx.mongodb.net/todo?retryWrites=true&w=majority&appName=Cluster0'

client = pymongo.MongoClient(
    MONGODB_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    print(client.admin.command('ping'))
except Exception as e:
    print("Connection error:", e)
