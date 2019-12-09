from flask import Flask, jsonify, render_template

from addressbook import initialize_database, add_database_records, read_database_records

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", contacts=read_database_records())


@app.route("/json")
def json():
    contacts = read_database_records()
    data = [dict(person) for person in contacts]
    return jsonify(data)


if __name__ == '__main__':
    initialize_database()
    add_database_records()

    app.run()
