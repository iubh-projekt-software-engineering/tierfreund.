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
from datetime import datetime
from app.event.model import Event
from app.animal.model import Animal
from app.doc.model import Doc

mod = Blueprint('event', __name__, url_prefix='/termine')


@mod.route('/')
def index():
    upcoming_events = db.session.query(Event,
                                       Animal,
                                       Doc).join(Doc).join(Animal).filter(
        Animal.user_id == current_user.id,
        Event.time >= datetime.now()
    ).all()
    past_events = db.session.query(Event,
                                   Animal,
                                   Doc).join(Doc).join(Animal).filter(
        Animal.user_id == current_user.id,
        Event.time < datetime.now()
    ).all()
    create_url = url_for('event.create')
    return render_template(
        '/events/index.html',
        upcoming_events=upcoming_events,
        past_events=past_events,
        create_url=create_url
    )


@mod.route('/erstellen', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            time = request.form.get('time')
            time_old = time.replace('T', ' ')
            time_new = datetime.strptime(time_old, '%Y-%m-%d %H:%M')
            new_event = Event(
                animal_id=request.form.get('animal_id'),
                doc_id=request.form.get('doc_id'),
                time=time_new,
                topic=request.form.get('topic'),
                notes=request.form.get('notes'),
            )
            db.session.add(new_event)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('Das Event konnte leider nicht erstellt werden.')
            return redirect(url_for('event.create'))

        return redirect(url_for('event.index'))
    animals = [
        {
            'value': animal.id,
            'label': animal.name
        }
        for animal
        in db.session.query(Animal).filter_by(user_id=current_user.id).all()
    ]
    docs = [
        {
            'value': doc.id,
            'label': doc.name
        }
        for doc
        in db.session.query(Doc).filter_by(user_id=current_user.id).all()
    ]
    return render_template('/events/create.html', animals=animals, docs=docs)


@mod.route('/bearbeiten/<int:event_id>', methods=['GET', 'POST'])
def update(event_id):
    event_or_none = db.session.query(Event).join(Animal).filter(
        Event.id == event_id, Animal.user_id == current_user.id
    ).one_or_none()

    if event_or_none is None:
        flash('Event wurde nicht gefunden.')
        return redirect(url_for('event.index'))

    if request.method == 'POST':
        try:
            time = request.form.get('time')
            time_old = time.replace('T', ' ')
            time_new = datetime.strptime(time_old, '%Y-%m-%d %H:%M')

            event_or_none.time = time_new
            event_or_none.topic = request.form.get('topic')
            event_or_none.notes = request.form.get('notes')
            event_or_none.doc_id = request.form.get('doc_id')
            event_or_none.animal_id = request.form.get('animal_id')
            db.session.commit()
        except Exception:
            flash('Das Event konnte leider nicht bearbeitet werden.')
            return redirect(url_for('event.update', event_id=event_id))

        return redirect(url_for('event.details', event_id=event_id))
    animals = [
        {
            'value': animal.id,
            'label': animal.name
        }
        for animal
        in db.session.query(Animal).filter_by(user_id=current_user.id).all()
    ]
    docs = [
        {
            'value': doc.id,
            'label': doc.name
        }
        for doc
        in db.session.query(Doc).filter_by(user_id=current_user.id).all()
    ]

    # convert time back
    time = event_or_none.time
    time_old = datetime.strftime(time, '%Y-%m-%d %H:%M')
    time_new = time_old.replace(' ', 'T')

    event_or_none.time = time_new

    return render_template(
        '/events/update.html',
        item=event_or_none,
        animals=animals,
        docs=docs
    )


@mod.route('/details/<int:event_id>')
def details(event_id):
    event_or_none = db.session.query(Event,
                                     Animal,
                                     Doc).join(Animal).join(Doc).filter(
        Event.id == event_id, Animal.user_id == current_user.id
    ).one_or_none()

    if event_or_none is None:
        flash('Das Event konnte leider nicht gefunden werden.')
        return redirect(url_for('event.index'))

    print('event: {}'.format(event_or_none))

    return render_template(
        '/events/details.html',
        item=event_or_none
    )


@mod.route('/loeschen/<int:event_id>', methods=['POST'])
def delete(event_id):
    event_or_none = db.session.query(Event).join(Animal).join(Doc).filter(
        Event.id == event_id, Animal.user_id == current_user.id
    ).one_or_none()

    if event_or_none is None:
        flash('Das Event konnte leider nicht gefunden werden.')
        return redirect(url_for('event.details', event_id=event_id))

    try:
        db.session.delete(event_or_none)
        db.session.commit()
        flash('Event erfolgreich gelöscht.')
    except Exception as e:
        print(e)
        flash('Das Event konnte leider nicht gelöscht werden.')
        return redirect(url_for('event.details', event_id=event_id))
    return redirect(url_for('event.index'))
