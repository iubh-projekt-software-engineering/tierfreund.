#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template
)
from flask_login import login_required

mod = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@mod.route('/')
@login_required
def index():
    return render_template('dashboard/index.html')
