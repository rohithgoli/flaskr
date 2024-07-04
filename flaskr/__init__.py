from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8db447af15aaeb8af3f4a0d347bef8a' # env. variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

with app.app_context():
    db = SQLAlchemy(app)

from flaskr import routes
