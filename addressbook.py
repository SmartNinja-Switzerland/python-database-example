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
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            email VARCHAR(255)
        )
        """)

    connection.commit()
    connection.close()


def add_database_records():
    """Add some data to our database"""
    connection = sqlite3.connect('addressbook.sqlite')
    cursor = connection.cursor()

    cursor.execute("""\
        INSERT INTO person VALUES (
            0,
            'Heidi',
            'Ruegger',
            'heidi.ruegger@bluewin.ch'
        )
        """)
    print(f"Heidi added.")

    connection.commit()
    connection.close()


def read_database_records():
    """Read the data we have stored in our database"""
    connection = sqlite3.connect('addressbook.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT firstname, lastname, email FROM person")
    all_rows = cursor.fetchall()
    print(f"Found {len(all_rows)} records.")

    for row in all_rows:
        print(row)

    connection.close()


initialize_database()
add_database_records()
read_database_records()
