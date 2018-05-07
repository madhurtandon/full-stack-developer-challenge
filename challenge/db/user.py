from challenge.db.db import DB


class User(DB):

    def create_table(self, cursor):
        sql = "CREATE TABLE  IF NOT EXISTS users(user_id int NOT NULL AUTO_INCREMENT, " \
              "name varchar(255), " \
              "PRIMARY KEY (user_id))"

        cursor.execute(sql)
