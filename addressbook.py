"""
Addressbook example project showcasing SQLite and SQLAlchemy.
"""
import sqlite3

from pathlib import Path

DATABASE_FILE = Path('addressbook.sqlite')


def initialize_database():
    """Create a simple address database"""
    connection = sqlite3.connect(DATABASE_FILE.name)
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
    connection = sqlite3.connect(DATABASE_FILE.name)
    cursor = connection.cursor()

    cursor.execute("""\
        INSERT INTO person VALUES (
            0,
            'Heidi',
            'Ruegger',
            'heidi.ruegger@bluewin.ch'
        ),
        (
            1,
            'Reto',
            'Ruegger',
            'reto.ruegger@bluewin.ch'
        )
        """)

    connection.commit()
    connection.close()


def read_database_records():
    """Read the data we have stored in our database"""
    connection = sqlite3.connect(DATABASE_FILE.name)
    cursor = connection.cursor()

    cursor.execute("SELECT firstname, lastname, email FROM person")

    for row in cursor.fetchall():
        firstname, lastname, email = row
        print(f"Send email to: {firstname} {lastname} <{email}>")

    connection.close()


def main():
    """Our program starts here"""
    if DATABASE_FILE.exists():
        DATABASE_FILE.unlink()

    initialize_database()
    add_database_records()
    read_database_records()


if __name__ == '__main__':
    main()
