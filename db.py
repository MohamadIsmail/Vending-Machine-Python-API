from flask_sqlalchemy import SQLAlchemy
from utils import app
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)
migrate=Migrate(app,db)