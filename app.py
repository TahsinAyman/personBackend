import json
from urllib import response
from flask import *
from models import *


def login_required(func):
    def wrapper(*args, **kwargs):
        if request.cookies.get("token") and Authentication.query.filter_by(token=request.cookies.get("token")).first():
            return func(*args, **kwargs)
        else:
            abort(401, "Not Authorized")
    return wrapper


@app.route("/", methods=["GET"])
@login_required
def index():
    return jsonify({"result": True, "status": 202, "message": "PersonBackendAPI"}), 202


@app.route("/auth/", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        try:
            data = request.get_json(force=True)
            auth = Authentication.query.filter_by(
                token=data.get("token")).first()
            if auth:
                response = make_response(
                    jsonify({"result": True, "status": 202, "message": "Authenticated"})), 202
                response.set_cookie("token", data.get("token"))
                return response
            else:
                raise Exception
        except Exception:
            abort(401, "Couldn't Authorize")
    else:
        try:
            token = request.args.get("token")
            auth = Authentication.query.filter_by(token=token).first()
            print(auth)
            if auth:
                response = make_response(
                    jsonify({"result": True, "status": 202,
                            "message": "Authenticated"}), 202
                )
                response.set_cookie("token", token)
                return response
            else:
                raise Exception
        except Exception as e:
            abort(401, "Couldn't Authorize")


@login_required
@app.route("/person/show/", methods=["GET"])
def show():
    if not request.args:
        result = [json.loads(str(i)) for i in Person.query.all()]
        return jsonify(result), 202
    else:
        id = request.args.get("id")
        result = [json.loads(str(i)) for i in Person.query.filter_by(id=id)]
        return jsonify(result), 202


@login_required
@app.route("/person/add/", methods=["POST"])
def add():
    try:
        data = request.get_json(force=True)
        person = Person(id=data.get("id"), name=data.get(
            "name"), age=data.get("age"))
        db.session.add(person)
        db.session.commit()
        return jsonify({"result": True, "status": 202, "message": "Successfully Added"}), 202
    except Exception:
        abort(400, "Couldn't Add Person")


@login_required
@app.route("/person/delete/", methods=["DELETE"])
def delete():
    try:
        data = request.get_json(force=True)
        person = Person.query.filter_by(id=data.get("id")).first()
        db.session.delete(person)
        db.session.commit()
        return jsonify({"result": True, "status": 202, "message": "Successfully Deleted"}), 202
    except Exception:
        abort(400, "Couldn't Delete")


@login_required
@app.route("/person/update/<id>", methods=["PUT"])
def update(id):
    try:
        data = request.get_json(force=True)
        person = Person.query.filter_by(id=id).first()
        if person:
            if data.get("id"):
                person.id = data.get("id")
            if data.get("name"):
                person.name = data.get("name")
            if data.get("age"):
                person.age = data.get("age")
            db.session.commit()
            return jsonify({"result": True, "status": 202, "message": "Successfully Updated"}), 202
        else:
            raise Exception
    except Exception:
        abort(400, "Couldn't Update")


@app.errorhandler(400)
def error_404(error):
    return jsonify({"result": False, "status": 401, "message": "Couldn't Run The Operation", "error": str(error)}), 400


@app.errorhandler(401)
def error_401(error):
    return jsonify({"result": False, "status": 401, "message": "Not Authorized: Authorize at /auth/", "error": str(error)}), 401


@app.errorhandler(405)
def error_405(error):
    return jsonify({"result": False, "status": 401, "message": f"{request.method} method is not allowed", "error": str(error)}), 405


@app.errorhandler(404)
def error_404(error):
    return jsonify({"result": False, "status": 404, "message": f"{request.url} is not Valid", "error": str(error)}), 404


if __name__ == "__main__":
    with open("config.json") as file:
        data = json.load(file)
    if data.get("host") and data.get("port"):
        app.run(host="localhost", port=data["port"])
    elif data.get("host"):
        app.run(host=data["host"], port=80)
    elif data.get("port"):
        app.run(host="0.0.0.0", port=data["port"])
    else:
        app.run(host="localhost", port=80)
