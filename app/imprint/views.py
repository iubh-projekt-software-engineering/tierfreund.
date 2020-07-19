#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template


mod = Blueprint('imprint', __name__, url_prefix='/impressum')


@mod.route('/')
def index():
    return render_template('/imprint/index.html')
