from app import db


class Doc(db.Model):
    __tablename__ = 'docs'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100))
    zip = db.Column(db.String(100))
    city = db.Column(db.String(100))
    phonenumber = db.Column(db.String(100))
    email = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, foreign_keys=[user_id])