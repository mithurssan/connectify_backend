# from decouple import config
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bcrypt import Bcrypt
from datetime import timedelta
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = environ.get("KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
app.config["JWT_SECRET_KEY"] = environ.get("KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

SQLALCHEMY_TRACK_NOTIFICATIONS = False
SQLALCHEMY_ECHO = True

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from application.models import User
from application.models import Business
from application.models import Holiday

from application.routes import (
    UsersRoutes,
    CompaniesHouseProxy,
    BusinessesRoutes,
    HolidayRoutes,
)


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})


@app.route("/profile")
def my_profile():
    res_body = {"name": "Panda", "about": "I love Romeo"}

    return res_body


app.register_blueprint(UsersRoutes.user, url_prefix="/users")
app.register_blueprint(CompaniesHouseProxy.proxy, url_prefix="/api")
app.register_blueprint(BusinessesRoutes.business, url_prefix="/businesses")
app.register_blueprint(HolidayRoutes.holiday, url_prefix="/bookings")
