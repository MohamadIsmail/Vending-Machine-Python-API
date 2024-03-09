from flask_sqlalchemy import SQLAlchemy
from utils import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)
with app.app_context(): 
    # Create tables in the database
    db.create_all()