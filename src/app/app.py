from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

def create_app(settings_module):
  
  app = Flask(__name__)
  app.config.from_object(settings_module)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:password@127.0.0.1:3306/rebooks'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SHOW_SQLALCHEMY_LOG_MESSAGES'] = False
  app.config['PROPAGATE_EXCEPTIONS'] = True
  app.config['SECRET_KEY'] = 'My-custom-api-key'
  app.url_map.strict_slashes = False

  db.init_app(app)
  ma.init_app(app)

  db.create_all(app=app)
  return app