
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from instance.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api

# from flask_mail import Mail
# from flask_restful import Api,Resource

app = Flask(__name__)
# main = Blueprint('main', __name__)
api = Api(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# mail = Mail(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'


# from game.api import api_bp

# Register the blueprint
# app.register_blueprint(api_bp, url_prefix='/auth')

app.app_context().push()

from game import routes


