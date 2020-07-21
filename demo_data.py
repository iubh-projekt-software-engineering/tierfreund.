#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    from datetime import datetime, timedelta
    import random

    from app import db
    from app.user.models import User
    from app.animal.model import Animal
    from app.doc.model import Doc
    from app.event.model import Event

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
        'color': '#fdbb45',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Susanne',
        'type': 2,
        'color': '#f77161',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Ben',
        'type': 3,
        'color': '#20ab62',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Frank',
        'type': 4,
        'color': '#d6560f',
        'race': 'Mischling',
        'weight': 70,
        'birthdate': '10.10.2010',
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Henry',
        'type': 1,
        'color': '#fdbb45',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Carl',
        'type': 2,
        'color': '#f77161',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Mai',
        'type': 3,
        'color': '#20ab62',
        'race': 'Mischling',
        'birthdate': '10.10.2010',
        'weight': 70,
        'user_id': new_user.id,
        'notes': 'Bekommt 3 mal täglich Aspirin Complex. Das hilt immer.'
    }, {
        'name': 'Lydia',
        'type': 4,
        'color': '#d6560f',
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

    events = ({
        'topic': 'Impfung',
        'notes': 'Es steht wieder eine Impfung an'
    }, {
        'topic': 'Wurmkur',
        'notes': 'Es findet eine Wurmkur statt'
    })

    created_animals = []
    for animal in animals:
        try:
            new_animal = Animal(**animal)
            db.session.add(new_animal)
            created_animals.append(new_animal)
            db.session.commit()
        except Exception as e:
            print(e)
            pass

    created_docs = []
    for doc in docs:
        try:
            new_doc = Doc(**doc)
            db.session.add(new_doc)
            db.session.commit()
        except Exception as e:
            print(e)
            pass
    now = datetime.now()

    for animal in created_animals:
        for event in events:
            new_event = Event(
                topic=event['topic'],
                notes=event['notes'],
                animal_id=animal.id,
                doc_id=1,
                time=(now + timedelta(days=+random.randint(100, 200)))
            )
            try:
                db.session.add(new_event)
                db.session.commit()
                print(new_event)
            except Exception as e:
                print(e)
                pass
        
        
