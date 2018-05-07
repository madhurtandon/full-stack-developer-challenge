from challenge.db.db import DB


class Story(DB):
    STATUS_PUBLISHED = 1
    STATUS_DRAFT = 2

    def create_table(self, cursor):
        sql = "CREATE TABLE  IF NOT EXISTS stories(story_id int NOT NULL AUTO_INCREMENT, " \
              "title varchar(255), " \
              "description LONGTEXT, " \
              "status int," \
              "author_id int," \
              "PRIMARY KEY (story_id))"

        cursor.execute(sql)

    def get_status(self, status):
        status = status.lower()
        if status == 'draft':
            return self.STATUS_DRAFT
        elif status == 'published':
            return self.STATUS_PUBLISHED

        raise Exception('Invalid Status')


    def create_story(self, cursor, title, description, status, author_id):
        sql = "INSERT INTO stories (title, description, status, author_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, description, status, author_id))
