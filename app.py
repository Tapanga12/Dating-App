import datetime
from typing import List, Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from model import db, User, Match, BlockedUser  # Import models from model.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datingapp.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# import routes (if in a separate file)
import routes  

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
