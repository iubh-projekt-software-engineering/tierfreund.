from app import db
from app.user.models import User


class Event(db.Model):
    __tablename__ = 'events'
