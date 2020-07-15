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
        'user_id': new_user.id
    }, {
        'name': 'Susanne',
        'type': 2,
        'color': 'rgba(247, 113, 97, 1)',
        'user_id': new_user.id
    }, {
        'name': 'Ben',
        'type': 3,
        'color': 'rgba(32, 171, 98, 1)',
        'user_id': new_user.id
    }, {
        'name': 'Frank',
        'type': 4,
        'color': 'rgba(214, 86, 15, 1)',
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

    
