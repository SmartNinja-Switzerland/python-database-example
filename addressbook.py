"""
Addressbook example project showcasing SQLite and SQLAlchemy.
"""
from pathlib import Path
from sqla_wrapper import SQLAlchemy


DATABASE_FILE = Path('addressbook.sqlite')

db = SQLAlchemy(f"sqlite:///{DATABASE_FILE.name}")


class Person(db.Model):
    """A person in our database"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def get_name(self):
        """Yield the complete name of the person"""
        return f"{self.firstname} {self.lastname}"


def initialize_database():
    """Create a simple address database"""
    if DATABASE_FILE.exists():
        DATABASE_FILE.unlink()

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
    return contacts


def get_database_item(person_id: int):
    """Return a single data item stored in our database"""
    person = db.query(Person).get(person_id)
    return person


def update_database_item(person):
    """Write changes to our database"""
    db.add(person)
    db.commit()
