#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

mod = Blueprint('index', __name__)


@mod.route('/')
def index():
    if hasattr(current_user, 'id'):
        return redirect(url_for('dashboard.index'))
    return render_template('/home/index.html')
