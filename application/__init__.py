from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = environ.get("KEY")
# app.config['SECRET_KEY'] = 'aa33b0f675c295360356133e54a39370'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DB_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fxfzdiel:RySMYhg_JfSgic6qfB-xaDaYRSwGN-sS@horton.db.elephantsql.com/fxfzdiel'

db = SQLAlchemy(app)

from application.routes import UsersRoutes

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})

app.register_blueprint(UsersRoutes.user, url_prefix= "/users")

