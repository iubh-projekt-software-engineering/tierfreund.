from app import db
from app.user.models import Animal
from app.doc.models import Doc


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship(Animal, foreign_keys=[animal_id])
    doc_id = db.Column(db.Integer, db.ForeignKey('doc.id'))
    doc = db.relationship(Doc, foreign_keys[doc_id])
