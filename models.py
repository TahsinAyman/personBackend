from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///person.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Authentication(db.Model):
    token = db.Column(db.String(1000), nullable=False, primary_key=True)
    name = db.Column(db.String(50))

    def __str__(self):
        return json.dumps(obj={"token": self.token, "name": self.name}, indent=4)


class Person(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return json.dumps(obj={"id": self.id, "name": self.name, "age": self.age}, indent=4)


def main():
    db.create_all()
    # db.drop_all()


if __name__ == '__main__':
    main()
