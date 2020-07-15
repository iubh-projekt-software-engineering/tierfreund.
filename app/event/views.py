from flask import (
    Blueprint,
    request,
    render_template,
    url_for,
    redirect,
    flash
)
from flask_login import current_user
from app import db
from app.event.model import Event
from app.animal.model import Animal
from app.doc.model import Doc

mod = Blueprint('event', __name__, url_prefix='/termine')

@mod.route('/')
def index():
    events = db.session.query(Event).filter_by(user_id=current_user.id).all()
    create_url = url_for('event.create')
    return render_template(
        '/events/index.html',
        events=events,
        create_url=create_url
    )

@mod.route('/erstellen', methods=['GET', 'POST'])
def create():
    return render_template('/events/create.html')
