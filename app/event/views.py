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

mod = Blueprint('event', __name__, url_prefix='/termine')

@mod.route('/')
def index():
    events = db.session.query(Event).filter_by(user_id=current_user.id).all()
    
