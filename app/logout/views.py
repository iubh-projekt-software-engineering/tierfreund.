#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    url_for,
    redirect
)
from flask_login import logout_user

mod = Blueprint('logout', __name__)


@mod.route('/logout', methods=['GET', 'POST'])
def index():
    logout_user()
    return redirect(url_for('login.index'))
