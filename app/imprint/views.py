#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

mod = Blueprint('imprint', __name__, url_prefix='/impressum')


@mod.route('/')
def index():
    return render_template('/imprint/index.html')
