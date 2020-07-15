from app import db
from app.user.models import User
from app.doc.models import Doc


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, foreign_keys=[user_id])
    doc_id = db.Column(db.Integer, db.ForeignKey('doc.id'))
    doc = db.relationship(Doc, foreign_keys[doc_id])
