from flask import Flask
from flask_cors import CORS
from app.utils import config_app
from app.models import db
from app.views import api

app = Flask(__name__)
config_app(app)
CORS(app)
db.init_app(app)
app.register_blueprint(api)
