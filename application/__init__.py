from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = environ.get("KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DB_URL")
db = SQLAlchemy(app)

from application.models import Business, Holiday, User
from application.routes import UsersRoutes

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})

app.register_blueprint(UsersRoutes.user, url_prefix= "/users")


