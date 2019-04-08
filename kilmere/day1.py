class CastleKilmereMember:
    """
    Creates a member of Castle Kilmere
    """

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def say(self, words):
        return f"{self._name} says {words}"


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    # class attribute
    location = 'England'

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
            'Broomstick FLying': False,
            'Art': False,
            'Magical Theory', False,
            'Foreign Magical Systems': False,
            'Charms': False,
            'Defense against dark magic': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Potions': False,
            'Transfiguration': False,
        }


class Professor(CastleKilmereMember):
    """
    Creates Castle Kilmere Professor
    """

    def __init__(self, name, birthyear, sex, subject, house=None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house


if __name__ == "__Main__":

    bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')
    print(bromley.says("Hello"))
    print(bromley.location)
    print(CastleKilmereMember.location)

    cleon = Pupil(name='Cleon Bery', birthyear=2008, sex='male',
                  house='House of Courage', start_year=2018,
                  pet=('Cotton', 'owl'))
