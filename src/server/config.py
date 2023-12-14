from os import getcwd
from os.path import abspath, join

from dotenv import dotenv_values

config = dict(dotenv_values(abspath(join(getcwd(), "..", "development.env"))))

PROJECT_NAME = config.get('PROJECT_NAME', 'FAST Template Service')
LOGTAIL_TOKEN = config.get('LOGTAIL_TOKEN', 'xxxxx')
HOST = config.get('NODE_HOST', 'localhost')
PORT = int(config.get('NODE_PORT', 8091))
PORT_ALT = int(config.get('NODE_PORT_ALT', 8091))

MYSQL_HOST = config.get('MYSQL_HOST', 'localhost')
MYSQL_PORT = config.get('MYSQL_PORT', 3306)
MYSQL_USERNAME = config.get('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = config.get('MYSQL_PASSWORD', 'Hamza1575')
MYSQL_DB_NAME = config.get('MYSQL_DB_NAME', 'pokemon')

MONGO_DATABASE = config.get('MONGO_DATABASE', 'pokemon')
MONGO_HOST = config.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(config.get('MONGO_PORT', 27017))
