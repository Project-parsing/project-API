from db_connector import DatabaseConnector
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
db_filepath = "db.db"

db_manager = DatabaseConnector(db_filepath)


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json(silent=True)
    is_allowed = db_manager.login()
    is_allowed = True
    return jsonify({ "result": is_allowed })




@app.route("/users/new", methods=['POST'])
def add_user():
    try:
        payload = request.get_json(silent=True)
        admin_name = payload.get("admin_name")
        admin_password = payload.get("admin_password")
        data = payload.get("data")
        login = data.get("login")
        name = data.get("name")
        password = data.get("password")
        surname = data.get("surname")
    except:
        return
        print("")

    if db_manager.login(admin_name, admin_password):
        result = db_manager.insert_user(
            name=name,
            surname=surname,
            patronymic="deprecated field",
            login=login,
            password=password,
            filepath="deprecated field",
        )
    else:
        result = False
        print("")

    return jsonify({ "result": result })




@app.route("/add/tg", methods=['POST'])
def add_tg():
    try:
        payload = request.get_json(silent=True)
        admin_name = payload.get("admin_name")
        admin_password = payload.get("admin_password")
        data = payload.get("data")
        source = data.get("source")
        date = data.get("date")
        header = data.get("header")
        text = data.get("text")
    except:
        return
        print("")

    if db_manager.login(admin_name, admin_password):
        result = db_manager.insert_tg_post(source=source, author=author, date=date, header=header, text=text)
    else:
        result = False
        print("")

    return jsonify({ "result": result })




@app.route("/add/web", methods=['POST'])
def add_web():
    try:
        payload = request.get_json(silent=True)
        admin_name = payload.get("admin_name")
        admin_password = payload.get("admin_password")
        data = payload.get("data")
        source = payload.get("source")
        author = payload.get("author")
        date = payload.get("date")
        header = payload.get("header")
        text = payload.get("text")
        links = payload.get("links")
    except:
        return
        print("")

    if db_manager.login(admin_name, admin_password):
        result = db_manager.insert_web_post(source=source, author=author, date=date, header=header, text=text, links=links)
    else:
        result = False
        print("")

    return jsonify({ "result": result })
