import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из БД')
        return []

    def add_post(self, name, price, data_limit, call_minutes, validity_period):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO mobile_plans VALUES(NULL, ?, ?, ?, ?, ?, ?)",
                               (name, price, data_limit, call_minutes, validity_period, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления данных:', str(e))
            return False
        return True

    def get_post(self, post_id):
        try:
            self.__cur.execute(
                "SELECT name, price, data_limit, call_minutes, validity_period FROM mobile_plans WHERE id = ?",
                (post_id,))
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения данных:', str(e))
        return False, False, False, False, False

    def get_post_annonce(self):
        try:
            self.__cur.execute(
                "SELECT id, name, price, data_limit, call_minutes, validity_period FROM mobile_plans ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
                # return [{'id': row[0], 'name': row[1], 'price': row[2], 'data_limit': row[3], 'call_minutes': row[4],
                #          'validity_period': row[5]} for row in res]
        except sqlite3.Error as e:
            print('Ошибка получения данных:', str(e))
        return []
