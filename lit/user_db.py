import pymysql as ps
import pymysql.cursors

from config import tele_db, host, user, password, db_name


class UserDB(object):
    def __init__(self):
        try:
            self.connection = ps.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            print("Correct connection")

        except Exception as ex:
            print("Connection refused....")
            print(ex)

    def create_db(self, user_name: str):
        sql_m = f"""CREATE TABLE `user_{user_name}` (
                `last_inquiry` VARCHAR(30) NULL
                );"""
        #print(sql_m, 5)
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)

    def append_data_base(self, user_name: str, msg: str):
        sql_m = f"""INSERT INTO `user_{user_name}` (`last_inquiry`) VALUES ('{msg}');"""
        #print(sql_m, 2)
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()

    def delete_from_db(self, user_name: str, id: tuple):
        if not id:
            sql_m = f"""DELETE FROM `user_{user_name}`;"""
        else:
            sql_m = f"""DELETE FROM `user_{user_name}` WHERE `id` in {id};"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()


if __name__ == "__main__":
    bd = UserDB()
