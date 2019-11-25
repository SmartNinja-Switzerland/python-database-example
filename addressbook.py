"""
Addressbook example project showcasing SQLite and SQLAlchemy.
"""
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///:memory:')


class Person(db.Model):
    """A person in our database"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True)


def initialize_database():
    """Create a simple address database"""
    db.create_all()


def add_database_records():
    """Add some data to our database"""
    my_contacts = [
        Person(lastname="Example", firstname="Adrian", email="adrian@example.com"),
        Person(lastname="Example", firstname="Aman", email="aman@example.com"),
        Person(lastname="Example", firstname="Carina", email="carina@example.com"),
        Person(lastname="Example", firstname="Eduard", email="eduard@example.com"),
        Person(lastname="Example", firstname="Nibu", email="nibu@example.com"),
        Person(lastname="Example", firstname="Yann", email="yann@example.com"),
        Person(lastname="Example", firstname="Yolanda", email="yoxito@example.com"),
    ]

    for contact in my_contacts:
        db.add(contact)

    db.commit()


def read_database_records():
    """Read the data we have stored in our database"""
    contacts = db.query(Person).all()

    for person in contacts:
        print(f"Send email to: {person.firstname} {person.lastname} <{person.email}>")


def main():
    """Our program starts here"""
    initialize_database()
    add_database_records()
    read_database_records()


if __name__ == '__main__':
    main()
