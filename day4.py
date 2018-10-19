import datetime


class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """
    location = 'England'

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"

    @property
    def age(self):
        return (lambda x, y: x - y)(datetime.datetime.now().year, self.birthyear)

    def says(self, words):
        return f"{self._name} says {words}"

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881,
                              sex='m')


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._owls = {
            'Study of Ancient Runes': False,
            'Arithmancy': False,
            'Astronomy': False,
            'Care of Magical Creatures': False,
            'Charms': False,
            'Defence against the Dark Arts': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Muggle Studies': False,
            'Potions': False,
            'Transfiguration': False}

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, house: {self.house})")

    @property
    def owls(self):
        return self._owls

    @owls.setter
    def owls(self, subject_and_grade):
        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass an iterable with two items: subject and grade")

        passed = self.passed(grade)

        if passed:
            self._owls[subject] = True
        else:
            print('The exam was not passed so no OWL was awarded!')

    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
            'O': True,
            'Ordinary': True,
            'P': True,
            'Passed': True,
            'A': True,
            'Acceptable': True,
            'p': False,
            'poor': False,
            'D': False,
            'Dreadful': False,
            'T': False,
            'Troll': False}

        return grades.get(grade, False)

    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Griffindor', start_year=1991,
                   pet=('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronal Bilius Weasley', 1980, 'male', 'Griffindor', 1991,
                   pet=('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        return cls('Hermione Granger', 1979, 'female', 'Griffindor', 1991,
                   pet=('Crookshanks', 'cat'))


class Professor(HogwartsMember):
    """
    Creates a Hogwarts Professor
    """

    def __init__(self, name, birthyear, sex, subject, house=None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', house='Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', house='Slytherin')


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts Ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, "
                f"year of death: {self.year_of_death})")


if __name__ == "__main__":
    hagrid = HogwartsMember('Rubeus Hagris', 1928, 'male')
    harry = Pupil('Harry James Potter', 1980, 'male', 'Gryffindor', 1991,
                  ('Hedwig', 'owl'))
    headmaster = harry.school_headmaster()

    mcgonagall = Professor.gmcgonagall()
    snape = Professor.snape()
    ron = Pupil.ron()
    hermione = Pupil.hermione()
