#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template


mod = Blueprint('privacy', __name__, url_prefix='/datenschutz')


@mod.route('/')
def index():
    return render_template('/privacy/index.html')
