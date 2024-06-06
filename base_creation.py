import sqlite3

connection = sqlite3.connect('db_test.db')


with open('base_creation.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()