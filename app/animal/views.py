from flask import (
    Blueprint,
    request,
    render_template,
    url_for,
    redirect,
    flash
)
from flask_login import current_user
from app import db
from app.animal.model import Animal
from app.animal.type import Animal as AnimalTypes, animal_labels


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
            flash('Tier wurde erfolgreich erstellt.')
        except Exception as e:
            print(e)
            flash('Tier konnte nicht erstellt werden')
            pass

        return redirect(url_for('animal.index'))

    types = [ {
        'value': animal['id'],
        'label': animal['label']
    } for animal in AnimalTypes.get_types()]
    colors = ('#6067EE', '#20AB62', '#F77161', '#FE9055', '#FDBB45')
    return render_template('/animals/create.html', colors=colors, types=types)


@mod.route('/bearbeiten/<int:animal_id>', methods=['GET', 'POST'])
def update(animal_id):
    animal_or_none = db.session.query(Animal).filter_by(
        id=animal_id, user_id=current_user.id
    ).one_or_none()

    if animal_or_none is None:
        flash('Tier wurde nicht gefunden.')
        return redirect(url_for('animal.details', animal_id=animal_id))

    if request.method == 'POST':
        try:
            animal_or_none.type = request.form.get('type')
            animal_or_none.name = request.form.get('name')
            animal_or_none.race = request.form.get('race')
            animal_or_none.color = request.form.get('color')
            animal_or_none.birthdate = request.form.get('birthdate')
            animal_or_none.weight = request.form.get('weight')
            animal_or_none.notes = request.form.get('notes')
            db.session.commit()
        except Exception as e:
            print(e)
            return redirect(url_for('animal.update', animal_id=animal_id))


        return redirect(url_for('animal.details', animal_id=animal_id))

    types = [ {
        'value': animal['id'],
        'label': animal['label']
    } for animal in AnimalTypes.get_types()]
    colors = ('#6067EE', '#20AB62', '#F77161', '#FE9055', '#FDBB45')
    return render_template('/animals/update.html', colors=colors, types=types, item=animal_or_none)

@mod.route('/details/<int:animal_id>')
def details(animal_id):
    animal_or_none = db.session.query(Animal).filter_by(
        id=animal_id, user_id=current_user.id
    ).one_or_none()

    if animal_or_none is None:
        flash('Das Tier konnte leider nicht gefunden werden.')
        return redirect(url_for('animal.index'))

    return render_template(
        '/animals/details.html',
        item=animal_or_none,
        animal_labels=animal_labels
    )


@mod.route('/loeschen/<int:animal_id>', methods=['POST'])
def delete(animal_id):
    animal_or_none = db.session.query(Animal).filter_by(
        id=animal_id, user_id=current_user.id
    ).one_or_none()

    if animal_or_none is None:
        flash('Das Tier konnte leider nicht gefunden werden.')

    try:
        db.session.delete(animal_or_none)
        db.session.commit()
    except Exception as e:
        print(e)
        flash('Das Tier konnte leider nicht gelöscht werden.')

    flash('Tier erfolgreich gelöscht.')
    return redirect(url_for('animal.index'))
