import pymongo
from pymongo import MongoClient
__client = MongoClient('mongodb://localhost:27017')
attribute =__client.AI.attribute
