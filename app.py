import os
from flask import Flask, jsonify
from flask_jwt import JWT
import click

from config import config
from api import api_bp
from views import home
from ext import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

    db.init_app(app)

    app.register_blueprint(api_bp)
    app.register_blueprint(home.home_bp)

    return app

app = create_app()