#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    session,
    redirect,
    flash
)
from flask_login import login_user
from app import db
from app.user.models import User

mod = Blueprint('register', __name__, url_prefix='/register')


@mod.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            new_user = User(
                username=request.form.get('username'),
                email=request.form.get('email')
            )
            new_user.hash_password(request.form.get('password'))
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            flash('Der Nutzer konnte leider nicht angelegt werden.')
            return redirect(url_for('register.index'))

        login_user(new_user)
        return redirect(url_for('dashboard.index'))

    return render_template('/register/index.html')
