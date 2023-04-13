from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv('USER')
password = os.getenv('DATAPASSKEY')

uri = f"mongodb+srv://{username}:{password}@clipsurf.upczxaf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

def add_mail(name, email):
    try:
        client.admin.command('ping')
    except Exception as e:
        return "Error"

    db = client["Email_data"]
    collection = db['Emails']

    document = {
        'name': name,
        'email' : email
    }
    result = collection.insert_one(document)
    return result