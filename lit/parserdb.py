import pymysql as ps
import pymysql.cursors
import time
from config import host, user, db_name, password


class Database(object):

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

    def create_data_base(self, name: str):
        with self.connection.cursor() as cursor:
            sql_m = """USE `parser_db`;
            CREATE TABLE `tele_db` (
            `user_id` SMALLINT(10) NOT NULL,
            `last_inquiry` VARCHAR(30) NULL,
            PRIMARY KEY (`user_id`)
            );"""
            cursor.execute(sql_m)

    def append_data_base(self, values: tuple):
        sql_m = f"""INSERT INTO `parser` (`good_name`, `good_cost`) VALUES ('{values[0]}', {values[1]});"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()

    def find_in_db(self, name:str):
        sql_m = f"""SELECT * FROM parser_db.parser WHERE good_name LIKE '%{name}%';"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()
            return cursor.fetchall()

    def delete_from_db(self, id: tuple):
        if not id:
            sql_m = """DELETE FROM `parser`;"""
        else:
            sql_m = f"""DELETE FROM `parser` WHERE `id` in {id};"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()

    def add_column(self, data=time.strftime('%m', time.localtime())):
        sql_m = f"ALTER TABLE `parser` ADD COLUMN `cost_change_{data}` VARCHAR(255) NOT NULL"
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()

    """not work now"""
    def append_data_base_c(self, value: str, data=time.strftime('%m', time.localtime())):
        sql_m = f"""UPDATE parser_db.parser SET `cost_change_03` = '{data}' where id = 7592;"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()


if __name__ == "__main__":
    my_bd = Database()
    try:
        my_bd.add_column()
    except pymysql.err.OperationalError:
        print("It almost in table")

    my_bd.append_data_base_c()