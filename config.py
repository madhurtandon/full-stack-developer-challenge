from os import environ
from pymysql.cursors import DictCursor
from challenge.constants import DB_HOST, DB_USER, DB_NAME, DB_PASS

HOST = environ.get('HOST', 'localhost')
PORT = environ.get('PORT', 8080)

MDB_CONFIG = {
    "user": DB_USER,
    "host": DB_HOST,
    "db": DB_NAME,
    "passwd": DB_PASS,
    "use_unicode": True,
    "charset": "utf8mb4",
    "cursorclass": DictCursor
}


