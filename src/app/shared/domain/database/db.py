from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import MetaData
from src.app.app import db as app_db, ma as marshmallow

db = app_db
ma = marshmallow
Base = declarative_base()
meta = MetaData()

class BaseModel:
    __table_args__ = {'extend_existing': True}
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()
    @classmethod
    def get_by_id(cls, id):
        return db.session.query(cls).get(id)
    @classmethod
    def simple_filter(cls, **kwargs):
        return db.session.query(cls).filter_by(**kwargs).all()