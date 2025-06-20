from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database object (SQLAlchemy ORM)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create tables if they don't exist
        return app
