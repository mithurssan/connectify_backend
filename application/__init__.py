from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bcrypt import Bcrypt
from datetime import timedelta
from flask_jwt_extended import JWTManager, unset_jwt_cookies, create_access_token
from flask_mail import Mail, Message

app = Flask(__name__)

CORS(app, origins=["https://connectifysite.netlify.app"])

app.config["SECRET_KEY"] = environ.get("KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
app.config["JWT_SECRET_KEY"] = environ.get("KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = environ.get("EMAIL")
app.config["MAIL_PASSWORD"] = environ.get("EMAIL_PASSWORD")


if environ.get("USE_MOCK_DB") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")


SQLALCHEMY_TRACK_NOTIFICATIONS = False
SQLALCHEMY_ECHO = True

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

mail = Mail(app)


from application.models import User, Business, Holiday, Journal


from application.routes import (
    UsersRoutes,
    CompaniesHouseProxy,
    BusinessesRoutes,
    HolidayRoutes,
    JournalRoutes,
    RotaRoutes,
    PostRoutes,
    CommentRoutes
)

with app.app_context():
    db.create_all()
    print("Database tables created.")


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})


@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


app.register_blueprint(UsersRoutes.user, url_prefix="/users")
app.register_blueprint(CompaniesHouseProxy.proxy, url_prefix="/api")
app.register_blueprint(BusinessesRoutes.business, url_prefix="/businesses")
app.register_blueprint(HolidayRoutes.holiday, url_prefix="/bookings")
app.register_blueprint(JournalRoutes.entry, url_prefix="/entries")
app.register_blueprint(RotaRoutes.rota, url_prefix="/rotas")
app.register_blueprint(PostRoutes.post, url_prefix="/posts")
app.register_blueprint(CommentRoutes.comment, url_prefix="/comments")
