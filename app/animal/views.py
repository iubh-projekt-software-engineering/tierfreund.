from flask import Blueprint, request, render_template, url_for
from flask_login import current_user
from app import db
from app.animal.model import Animal


mod = Blueprint('animal', __name__, url_prefix='/tiere')


@mod.route('/')
def index():
    animals = db.session.query(Animal).filter_by(user_id=current_user.id).all()
    create_url = url_for('animal.create')
    return render_template(
        '/animals/index.html',
        animals=animals,
        create_url=create_url
    )

@mod.route('/erstellen')
def create():
    return render_template('/animals/create.html')