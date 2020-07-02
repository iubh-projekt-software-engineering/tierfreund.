from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user
from app import db
from app.animal.model import Animal
from app.animal.type import Animal as AnimalTypes


mod = Blueprint('animal', __name__, url_prefix='/tiere')


@mod.route('/')
def index():
    animals = db.session.query(Animal).filter_by(user_id=current_user.id).all()
    create_url = url_for('animal.create')
    return render_template(
        '/animals/index.html',
        animals=animals,
        create_url=create_url
    )

@mod.route('/erstellen', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        try:
            new_animal = Animal(
                user_id=current_user.id,
                type=request.form.get('type'),
                name=request.form.get('name'),
                race=request.form.get('race'),
                color=request.form.get('color'),
                birthdate=request.form.get('birthdate'),
                weight=request.form.get('weight'),
                notes=request.form.get('notes')
            )
            db.session.add(new_animal)
            db.session.commit()
        except Exception as e:
            print(e)
            pass

        return redirect(url_for('animal.index'))

    types = [ {
        'value': animal['id'],
        'label': animal['label']
    } for animal in AnimalTypes.getTypes()]
    colors = ('#6067EE', '#20AB62', '#F77161', '#FE9055', '#FDBB45')
    return render_template('/animals/create.html', colors=colors, types=types)

@mod.route('/details/<int:animal_id>')
def details(animal_id):
    animal_or_none = db.session.query(Animal).filter_by(
        id=animal_id, user_id=current_user.id
    ).one_or_none()

    if animal_or_none is None:
        flash('Das Tier konnte leider nicht gefunden werden.')
        return redirect(url_for('animal.index'))

    return render_template('/animals/details.html', item=animal_or_none)
