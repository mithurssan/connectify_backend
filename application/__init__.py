# from decouple import config
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = environ.get("KEY")

if environ.get("USE_MOCK_DB") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
# app.config.from_object(config("APP_SETTINGS"))

SQLALCHEMY_TRACK_NOTIFICATIONS = False
SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from application.models import User, Business, Holiday, Journal

from application.routes import (
    UsersRoutes,
    CompaniesHouseProxy,
    BusinessesRoutes,
    HolidayRoutes,
    JournalRoutes
)

with app.app_context():
    db.create_all()
    print("Database tables created.")

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})

app.register_blueprint(UsersRoutes.user, url_prefix="/users")
app.register_blueprint(CompaniesHouseProxy.proxy, url_prefix="/api")
app.register_blueprint(BusinessesRoutes.business, url_prefix="/businesses")
app.register_blueprint(HolidayRoutes.holiday, url_prefix="/bookings")
app.register_blueprint(JournalRoutes.entry, url_prefix="/entries")
