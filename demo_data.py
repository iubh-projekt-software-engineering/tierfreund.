#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    from app import db
    from app.user.models import User
    from app.animal.model import Animal

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
    })

    docs = ({
        'name': 'Dr. Test1',
        'street': 'Teststraße1',
        'zip': '51427',
        'city': 'Teststadt',
        'phonenumber': '0123 456 78 09',
        'email': 'info@muster-dr.de',
        'user_id': new_user.id,
    }, {
        'name': 'Dr. Test2',
        'street': 'Teststraße2',
        'zip': '51427',
        'city': 'Teststadt',
        'phonenumber': '0123 456 78 09',
        'email': 'info@muster-dr.de',
        'user_id': new_user.id,
    }, {
        'name': 'Dr. Test3',
        'street': 'Teststraße3',
        'zip': '51427',
        'city': 'Teststadt',
        'phonenumber': '0123 456 78 09',
        'email': 'info@muster-dr.de',
        'user_id': new_user.id,
    })

    for animal in animals:
        try:
            new_animal = Animal(**animal)
            db.session.add(new_animal)
            db.session.commit()
            new_animal = Animal(**animal)
            db.session.add(new_animal)
            db.session.commit()
        except Exception as e:
            print(e)
            pass
