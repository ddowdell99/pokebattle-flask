from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User, Team, TeamPokemonJoin, Pokemon
from flask_login import LoginManager

from .auth.routes import auth

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)

app.register_blueprint(auth)


db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)

login.login_view = 'auth.logMeIn'

from . import routes
from . import models