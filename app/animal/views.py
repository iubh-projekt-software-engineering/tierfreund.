from flask import Blueprint, request, render_template


mod = Blueprint('animal', __name__, url_prefix='/tiere')


@mod.route('/')
def index():
    return render_template('/animals/index.html')