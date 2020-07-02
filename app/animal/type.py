class Animal:
    dog = {
        'label': 'Hund',
        'id': 1
    }

    cat = {
        'label': 'Katze',
        'id': 2
    }

    @staticmethod
    def getTypes():
        return (Animal.dog, Animal.cat)

class Gender:
    @staticmethod
    def getGender():
        return (
            {
                'label': 'männlich',
                'id': 1
            }, {
                'label': 'weiblich',
                'id': 2
            }
        )