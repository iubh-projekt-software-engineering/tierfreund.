#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    session,
    redirect
)
from flask_login import login_user
from app import db
from app.user.models import User

mod = Blueprint('login', __name__, url_prefix='/login')


@mod.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_or_none = db.session.query(User).filter_by(
            username=request.form.get('username')
        ).one_or_none()

        if user_or_none is None or not user_or_none.verify_password(request.form.get('password')):
            flash('Nutzer konnte nicht verifiziert werden.')
            return redirect(url_for('login.index'))
        
        login_user(user_or_none)

        # todo implement dashboard url and redirect


    return render_template('/login/index.html')
