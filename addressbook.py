"""
Addressbook example using SQLAlchemy
"""
import sqlite3


def initialize_database():
    """"""
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("""\
        CREATE TABLE person (
            id INTEGER,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255)
        )
        """)
