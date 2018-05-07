import pymysql


class DB:
    def __init__(self, **db_config):
        self.db_config = db_config

    def __enter__(self):
        self.con = pymysql.connect(**self.db_config)
        return self.con.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.__exit__(exc_type, exc_val, exc_tb)
        self.con.close()

    def create_story_table(self, cursor):
        sql = "CREATE TABLE  IF NOT EXISTS stories(story_id int NOT NULL AUTO_INCREMENT, " \
              "title varchar(255), " \
              "description LONGTEXT, " \
              "status int," \
              "created_at int," \
              "updated_at int," \
              "PRIMARY KEY (story_id))"

        cursor.execute(sql)

        return True
