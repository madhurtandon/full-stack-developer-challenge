from challenge.db.story import Story
from challenge.db.user import User
from config import MDB_CONFIG

if __name__ == '__main__':
    db = Story(**MDB_CONFIG)
    with db as cursor:
        db.create_table(cursor)

    db = User(**MDB_CONFIG)
    with db as cursor:
        db.create_table(cursor)
