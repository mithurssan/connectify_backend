# from decouple import config
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = environ.get("KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
# app.config.from_object(config("APP_SETTINGS"))
db = SQLAlchemy(app)

from application.routes import UsersRoutes
from application.routes import CompaniesHouseProxy


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})


app.register_blueprint(UsersRoutes.user, url_prefix="/users")
app.register_blueprint(CompaniesHouseProxy.proxy, url_prefix="/api")
