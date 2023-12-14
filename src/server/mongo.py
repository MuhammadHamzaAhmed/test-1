from mongoengine import connect

from src.server.config import MONGO_DATABASE, MONGO_HOST, MONGO_PORT

connect(db=MONGO_DATABASE, host=MONGO_HOST, port=MONGO_PORT)

CONNECTION_STRING = 'Mongo Connected'
