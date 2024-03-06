import pymysql

from base.utils.settings import SettingKeys, Settings


def connect():
    return


class Database:
    def __init__(self):
        self.settings = Settings()


class DataBaseController(Database):
    def __init__(self):
        Database.__init__(self)

    @staticmethod
    def insert_data(data=""):
        cursor = db.cursor()
        query = "".format(data)
        cursor.execute(query)
        db.close()