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
from app.doc.model import Doc


mod = Blueprint('doc', __name__, url_prefix='/aerzte')


@mod.route('/')
def index():
    docs = db.session.query(Doc).filter_by(user_id=current_user.id).all()
    create_url = url_for('doc.create')
    return render_template(
        '/docs/index.html',
        docs=docs,
        create_url=create_url
    )


@mod.route('/erstellen', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            new_doc = Doc(
                user_id=current_user.id,
                name=request.form.get('name'),
                street=request.form.get('street'),
                zip=request.form.get('zip'),
                city=request.form.get('city'),
                phonenumber=request.form.get('phonenumber'),
                email=request.form.get('email')
            )
            db.session.add(new_doc)
            db.session.commit()
        except Exception as e:
            print(e)
            pass

        return redirect(url_for('doc.index'))

    return render_template('/docs/create.html')


@mod.route('/bearbeiten/<int:doc_id>', methods=['GET', 'POST'])
def update(doc_id):
    doc_or_none = db.session.query(Doc).filter_by(
        id=doc_id, user_id=current_user.id
    ).one_or_none()

    if doc_or_none is None:
        flash('Arzt wurde nicht gefunden.')
        return redirect(url_for('doc.details', doc_id=doc_id))

    if request.method == 'POST':
        try:
            doc_or_none.name = request.form.get('name')
            doc_or_none.street = request.form.get('street')
            doc_or_none.zip = request.form.get('zip')
            doc_or_none.city = request.form.get('city')
            doc_or_none.phonenumber = request.form.get('phonenumber')
            doc_or_none.email = request.form.get('email')
            db.session.commit()
        except Exception as e:
            print(e)
            return redirect(url_for('doc.update', doc_id=doc_id))

        return redirect(url_for('doc.details', doc_id=doc_id))

    return render_template('/docs/update.html', item=doc_or_none)


@mod.route('/details/<int:doc_id>')
def details(doc_id):
    doc_or_none = db.session.query(Doc).filter_by(
        id=doc_id, user_id=current_user.id
    ).one_or_none()

    if doc_or_none is None:
        flash('Der Arzt konnte leider nicht gefunden werden.')
        return redirect(url_for('doc.index'))

    return render_template(
        '/docs/details.html',
        item=doc_or_none
    )


@mod.route('/loeschen/<int:doc_id>', methods=['POST'])
def delete(doc_id):
    doc_or_none = db.session.query(Doc).filter_by(
        id=doc_id, user_id=current_user.id
    ).one_or_none()

    if doc_or_none is None:
        flash('Der Arzt konnte leider nicht gefunden werden.')

    try:
        db.session.delete(doc_or_none)
        db.session.commit()
    except Exception as e:
        print(e)
        flash('Der Arzt konnte leider nicht gelöscht werden.')

    flash('Arzt erfolgreich gelöscht.')
    return redirect(url_for('doc.index'))
