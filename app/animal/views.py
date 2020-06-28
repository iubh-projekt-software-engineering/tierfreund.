from flask import Blueprint, request, render_template
from flask_login import current_user
from app import db
from app.animal.model import Animal


mod = Blueprint('animal', __name__, url_prefix='/tiere')


@mod.route('/')
def index():
    animals = db.session.query(Animal).filter_by(user_id=current_user.id).all()
    return render_template('/animals/index.html', animals=animals)