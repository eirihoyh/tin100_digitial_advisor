"""
Moste of the code taken from https://github.com/navjordj/TIN100_API/blob/main/02_Databaser
"""

import sqlite3
from sqlite3 import Error


def connect_to_database():
    connection = sqlite3.connect("database.db")

    if connection is not None:
        sql_create_table = "CREATE TABLE IF NOT EXISTS user_data (id integer PRIMARY KEY, " \
                           "food real NOT NULL, " \
                           "cloth real NOT NULL, " \
                           "travel real NOT NULL, " \
                           "payments real NOT NULL, " \
                           "buffer real NOT NULL, " \
                           "freetime real NOT NULL); "
        try:
            c = connection.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)

    connection.close()


class StoreInDatabase:
    def __init__(self, id: int = None):
        if id == None:
            self.id = -1
        else:
            self.id = id

        connect_to_database()

    @staticmethod
    def insert_data(food, cloth, travel, payments, buffer, freetime):
        connection = sqlite3.connect(
            "database.db")

        c = connection.cursor()

        sql_insert = f'INSERT INTO user_data (food, cloth, travel, payments, buffer, freetime) ' \
                     f'VALUES ({round(food, 2)},' \
                     f' {round(cloth, 2)}, ' \
                     f'{round(travel, 2)}, ' \
                     f'{round(payments, 2)}, ' \
                     f'{round(buffer, 2)}, ' \
                     f'{round(freetime, 2)})'
        c.execute(sql_insert)

        connection.commit()
        connection.close()

    def get_data(self):
        connection = sqlite3.connect(
            "database.db")
        c = connection.cursor()

        print("----------- \n Wanted data:")
        if self.id == -1:
            sql_query = f"SELECT * from user_data ORDER BY id DESC LIMIT 1"
        else:
            sql_query = f"SELECT * from user_data WHERE id={self.id}"

        c.execute(sql_query)

        rows = c.fetchall()

        connection.close()

        return rows[0]


if __name__ == "__main__":
    data = StoreInDatabase()
    print(data.get_data())
