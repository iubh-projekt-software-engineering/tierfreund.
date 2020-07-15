from app import db
from app.user.models import User


class Event(db.Model):
    __tablename__ = 'events'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, foreign_keys=[user_id])
