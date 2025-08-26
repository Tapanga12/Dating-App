import datetime
from typing import List, Optional

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from model import db, User, Match, BlockedUser  # Import models from model.py


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datingapp.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)  # Initialize SQLAlchemy with the Flask app


 


if __name__ == '__main__':
    with app.app_context():  # Makes sure to be in app context when calling db.create_all()
        db.create_all()  # Create the tables defined in model
    app.run(debug=True) 
