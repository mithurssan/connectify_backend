from flask import Flask, jsonify

# from decouple import config
from flask_login import LoginManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = environ.get("KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
app.config["APP_SETTINGS"] = environ.get("APP_SETTINGS")
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from application.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


from application.routes import UsersRoutes


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})


app.register_blueprint(UsersRoutes.user, url_prefix="/users")
