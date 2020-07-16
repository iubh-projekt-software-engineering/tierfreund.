#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template
)
from flask_login import login_required, current_user
from app import db
from app.animal.model import Animal

mod = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@mod.route('/')
@login_required
def index():
    animals = db.session.query(Animal).filter_by(user_id=current_user.id).all()
    return render_template('dashboard/index.html', animals=animals)
