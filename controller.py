import sqlite3


def database_creation():
    data_base = sqlite3.connect('pupils.db')
    data_base.execute(
        'CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, ferst_name TEXT)')