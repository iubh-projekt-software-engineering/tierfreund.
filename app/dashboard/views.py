#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template
)
from flask_login import login_required, current_user
from app import db
from app.animal.model import Animal
from app.doc.model import Doc
from app.event.model import Event

mod = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@mod.route('/')
@login_required
def index():
    animals = db.session.query(Animal).filter_by(user_id=current_user.id).all()
    events = db.session.query(Event).filter_by(animal_id=Animal.id, doc_id=Doc.id).all()
    return render_template('dashboard/index.html', animals=animals, events=events)
