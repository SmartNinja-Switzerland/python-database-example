from flask import Flask, jsonify, render_template

from addressbook import initialize_database, add_database_records, read_database_records, get_database_item

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", contacts=read_database_records())


@app.route("/person/<int:person_id>", methods=["GET"])
def details(person_id):
    return render_template("details.html", person=get_database_item(person_id))


@app.route("/person/<int:person_id>", methods=["POST"])
def update(person_id):
    person = get_database_item(person_id)
    # TODO: update in the database
    print(f"TODO: update {person.firstname} {person.lastname} in the database")
    # Easy solution: show all contacts after updating
    return index()


@app.route("/edit/<int:person_id>")
def edit(person_id):
    return render_template("edit.html", person=get_database_item(person_id))


@app.route("/json")
def json():
    contacts = read_database_records()
    data = [dict(person) for person in contacts]
    return jsonify(data)


if __name__ == '__main__':
    initialize_database()
    add_database_records()

    app.run()
