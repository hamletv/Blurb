from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy # import, create instances of database and migration engine
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models  # models to define structure of db
