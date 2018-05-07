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
