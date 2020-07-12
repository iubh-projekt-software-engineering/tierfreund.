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
        'type': 0,
        'color': 'blue',
        'user_id': new_user.id
    }, {
        'name': 'Susanne',
        'type': 0,
        'color': 'red',
        'user_id': new_user.id
    }, {
        'name': 'Peter',
        'type': 1,
        'color': 'black',
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

    
