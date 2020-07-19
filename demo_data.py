#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    from app import db
    from app.user.models import User
    from app.animal.model import Animal
    from app.doc.model import Doc
    from app.event.model import Event
    from datetime import datetime

    new_user = User(
        username='demo',
        email='demo@demo.de'
    )
    new_user.hash_password('demo')

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    animals = ({
        'name': 'Struppy',
        'type': 1,
        'color': 'rgba(253, 187, 69, 1)',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Susanne',
        'type': 2,
        'color': 'rgba(247, 113, 97, 1)',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Ben',
        'type': 3,
        'color': 'rgba(32, 171, 98, 1)',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Frank',
        'type': 4,
        'color': 'rgba(214, 86, 15, 1)',
        'race': 'Mischling',
        'weight': 70,
        'birthdate': '10.10.2010',
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Henry',
        'type': 1,
        'color': 'rgba(253, 187, 69, 1)',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Carl',
        'type': 2,
        'color': 'rgba(247, 113, 97, 1)',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Mai',
        'type': 3,
        'color': 'rgba(32, 171, 98, 1)',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Lydia',
        'type': 4,
        'color': 'rgba(214, 86, 15, 1)',
        'race': 'Mischling',
        'weight': 70,
        'birthdate': '10.10.2010',
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    })

    docs = ({
        'name': 'Dr. Langer',
        'street': 'Teststraße',
        'zip': '51427',
        'city': 'Refrath',
        'phonenumber': '01234565',
        'email': 'langer-vet@docmail.de',
        'user_id': new_user.id
    }, {
        'name': 'Dr. Vogel',
        'street': 'Teststraße2',
        'zip': '51503',
        'city': 'Rösrath',
        'phonenumber': '012345657',
        'email': 'vogel-vet@docmail.de',
        'user_id': new_user.id
    })

    for animal in animals:
        try:
            new_animal = Animal(**animal)
            db.session.add(new_animal)
            db.session.commit()
        except Exception as e:
            print(e)
            pass

    for doc in docs:
        try:
            new_doc = Doc(**doc)
            db.session.add(new_doc)
            db.session.commit()
        except Exception as e:
            print(e)
            pass

    time = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    time_new = datetime.strptime(time, '%Y-%m-%d %H:%M')

    events = ({
        'time': time_new,
        'topic': 'Impfung',
        'animal_id': new_animal.id,
        'doc_id': new_doc.id
    }, {
        'time': time_new,
        'topic': 'Vorsorge',
        'animal_id': new_animal.id,
        'doc_id': new_doc.id
    }, {
        'time': time_new,
        'topic': 'Operation',
        'animal_id': new_animal.id,
        'doc_id': new_doc.id
    },{
        'time': time_new,
        'topic': 'Impfung',
        'animal_id': new_animal.id,
        'doc_id': new_doc.id
    },{
        'time': time_new,
        'topic': 'Vorsorge',
        'animal_id': new_animal.id,
        'doc_id': new_doc.id
    },{
        'time': time_new,
        'topic': 'Operation',
        'animal_id': new_animal.id,
        'doc_id': new_doc.id
    },)

    for event in events:
        try:
            new_event = Event(**event)
            db.session.add(new_event)
            db.session.commit()
        except Exception as e:
            print(e)
            pass
