import pymysql as ps
import pymysql.cursors

from config import tele_db, host, user, password, db_name


class TeleDB(object):
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

    def create_db(self):
        with self.connection.cursor() as cursor:
            sql_m = """CREATE TABLE `tele_db` (
                    `user_id` SMALLINT(10) NOT NULL,
                    `last_inquiry` VARCHAR(30) NULL
                    );"""
            # устрарел
            cursor.execute(sql_m)

    def append_data_base(self, ip: str):
        sql_m = f"""INSERT INTO `{tele_db}` (`user_id`) VALUES ('{ip}');"""
        #print(sql_m, "   jkl   ", tele_db, ip)
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()

    def delete_from_db(self, id: tuple):
        if not id:
            sql_m = f"""DELETE FROM `{tele_db}`;"""
        else:
            sql_m = f"""DELETE FROM `{tele_db}` WHERE `id` in {id};"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql_m)
            self.connection.commit()

    def check_element_in_table(self, user_name: str):
        sql_m = f"""SELECT * FROM parser_db.tele_db WHERE `user_id` = {user_name};"""
        with self.connection.cursor() as cursor:
            return cursor.execute(sql_m)
            # result = cursor.fetchone()




if __name__ == "__main__":
    bd = TeleDB()
    bd.delete_from_db(())