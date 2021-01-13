"""
Code taken from https://github.com/navjordj/TIN100_API/blob/main/02_Databaser
"""

import sqlite3  # Biblioteket vi skal bruke for å kommunisere med sqlite-databasen
from sqlite3 import Error

import random


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


def insert_data():
    connection = sqlite3.connect(
        "database.db")  # Kobler til databasen vi opprettet i 1_lage_database.py

    c = connection.cursor()

    # Setter inn flere rader med en for-løkke
    for i in range(9):
        sql_insert = f'INSERT INTO user_data (food, cloth, travel, payments, buffer, freetime) ' \
                     f'VALUES ({round(random.random(), 2)}, {round(random.random(), 2)}, {round(random.random(), 2)}, {round(random.random(), 2)}, {round(random.random(), 2)}, {round(random.random(), 2)})'
        c.execute(sql_insert)

    connection.commit()
    connection.close()


def get_data():
    connection = sqlite3.connect(
        "database.db")  # Kobler til databasen vi opprettet i 1_lage_database.py

    print("----------- \n All data:")

    sql_query = "SELECT * from user_data"  # Spørring for å hente all data (* = alt)

    c = connection.cursor()
    c.execute(sql_query)  # Utfører kommandoen

    rows = c.fetchall()  # Henter ut resultatene fra spørringen

    # Printer ut en radene
    for row in rows:
        print(row)

    print("----------- \n Første 2 punkter i tabellen:")

    # Bruk LIMIT 2 for å bare hente ut de 2 første radene i tabellen
    sql_query = "SELECT * from user_data LIMIT 2"

    c.execute(sql_query)

    rows = c.fetchall()

    for row in rows:
        print(row)

    connection.close()

if __name__ == "__main__":
    connect_to_database()
    insert_data()
    get_data()
