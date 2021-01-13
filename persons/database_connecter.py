"""
Code taken from https://github.com/navjordj/TIN100_API/blob/main/02_Databaser
"""

import sqlite3  # Biblioteket vi skal bruke for å kommunisere med sqlite-databasen
from sqlite3 import Error


def connect_to_database():
    connection = sqlite3.connect("database.db")

    if connection is not None:  # Sjekker om opprettelsen av databasen var en suksess

        # Kommando for å lage en tabell som heter sensordata
        # 2 kolonner:
        # id (som er et integer og er primary key)
        # value (som er et desimaltall og må være oppgitt)

        sql_create_table = "CREATE TABLE IF NOT EXISTS user_data (id integer PRIMARY KEY, " \
                           "food real NOT NULL, " \
                           "cloth real NOT NULL, " \
                           "travel real NOT NULL, " \
                           "payments real NOT NULL, " \
                           "buffer real NOT NULL, " \
                           "freetime real NOT NULL); "
        try:
            c = connection.cursor()
            c.execute(sql_create_table)  # Utfører opprettelsen av en tabell
        except Error as e:
            print(e)  # Printer eventuelle feil

    connection.close()  # Viktig å lukke databasen før programmet avslutter


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
            "database.db")  # Kobler til databasen vi opprettet i 1_lage_database.py

        c = connection.cursor()

        # Setter inn flere rader med en for-løkke
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
            "database.db")  # Kobler til databasen vi opprettet i 1_lage_database.py
        c = connection.cursor()

        print("----------- \n Wanted data:")

        sql_query = f"SELECT * from user_data WHERE id={self.id}"

        c.execute(sql_query)

        rows = c.fetchall()

        connection.close()

        return rows[0]


if __name__ == "__main__":
    data = StoreInDatabase(2)
    data.get_data()
