from pymysql.cursors import DictCursor
from challenge.db import DB
from challenge.constants import DB_HOST, DB_USER, DB_NAME, DB_PASS

MDB_CONFIG = {
    "user": DB_USER,
    "host": DB_HOST,
    "db": DB_NAME,
    "passwd": DB_PASS,
    "use_unicode": True,
    "charset": "utf8mb4",
    "cursorclass": DictCursor
}

if __name__ == '__main__':
    db = DB(**MDB_CONFIG)

    with db as cursor:
        db.create_story_table(cursor)
