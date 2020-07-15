from app import db
from app.animal.model import Animal
from app.doc.model import Doc


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    titel = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    topic = db.Column(db.String(100))
    notes = db.Column(db.String(200))
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship(Animal, foreign_keys=[animal_id])
    doc_id = db.Column(db.Integer, db.ForeignKey('doc.id'))
    doc = db.relationship(Doc, foreign_keys=[doc_id])
