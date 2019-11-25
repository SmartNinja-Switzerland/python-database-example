"""
Addressbook example project showcasing SQLite and SQLAlchemy.
"""
import sqlite3


def initialize_database():
    """Create a simple address database"""
    connection = sqlite3.connect('addressbook.sqlite')
    cursor = connection.cursor()

    cursor.execute("""\
        CREATE TABLE person (
            id INTEGER,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255)
        )
        """)

    connection.commit()
    connection.close()


initialize_database()
