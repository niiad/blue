import os

from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api

from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize plugins
    database.init_app(app)

    # Register Blueprints or API namespaces
    from app.routes.users import api as users_api
    api = Api(app)
    api.add_namespace(users_api, path='/users')

    return app
