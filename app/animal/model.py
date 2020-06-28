from app import db


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    type = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    race = db.Column(db.String(200))
    birthdate = db.Column(db.String(20))
    weight = db.Column(db.Float)
    notes = db.Column(db.Text)