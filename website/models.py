from .import db
from flask_login import UserMixin #type:ignore
from sqlalchemy.sql import func #type:ignore

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(32),nullable=False)
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    content=db.Column(db.String(600),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.user_id'))


class User(db.Model,UserMixin):
    user_id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(40),nullable=False)
    user_email=db.Column(db.String(100),nullable=False,unique=True)
    user_password=db.Column(db.String(20),nullable=False)
    notes=db.relationship('Note')