class Animal:
    dog = {
        'label': 'Hund',
        'id': 1
    }

    cat = {
        'label': 'Katze',
        'id': 2
    }

    fish = {
        'label': 'Fisch',
        'id': 3
    }

    mouse = {
        'label': 'Maus',
        'id': 4
    }

    bird = {
        'label': 'Vogel',
        'id': 5
    }

    @staticmethod
    def get_types():
        return (
            Animal.dog,
            Animal.cat,
            Animal.fish,
            Animal.mouse,
            Animal.bird
        )


animal_labels = {
    item['id']: item['label']
    for item
    in Animal.get_types()
}


class Gender:
    @staticmethod
    def get_gender():
        return (
            {
                'label': 'männlich',
                'id': 1
            }, {
                'label': 'weiblich',
                'id': 2
            }
        )
