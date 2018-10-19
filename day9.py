"""
File: day_9.py
Author: Anna-Lena Popkes
Email: popkes@gmx.net
Github: https://github.com/zotroneneis
Description: all code for day 6 of my new coding habit
Link to blog post with explanations: http://www.alpopkes.com/posts
/2018/07/coding-challenge-day-6/
"""

import datetime


class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value
                       in self._traits.items() if value]
        false_traits = [trait for trait, value
                        in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}.")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait\
                    called {trait}")

        if value:
            print(f"Yes, {self._name} is {trait}!")

        else:
            print(f'No, {self._name} is not {trait}')

    def says(self, words):
        return f"{self._name} says {words}"

    @property
    def age(self):
        # now = datetime.datetime.now().year
        return now - self.birthyear

    @property
    def name(self):
        return self._name

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore',
                              1881, 'male')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name},\
                  birthyear: {self.birthyear})"


class Professor(HogwartsMember):
    """
    Creates a Hogwarts professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str,
                 house: str = None):

        super().__init__(name, birthyear, sex)
        self.subject = subject
        if house is not None:
            self.house = house

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration',
                   'Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', 'Slytherin')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str,
                 year_of_death: int, house: str = None):

        super().__init__(name, birthyear, sex)

        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, "
                f"year of death: {self.year_of_death})")


class Pupil(HogwartsMember):
    """
    Create a Hogwarts Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str,
                 start_year: int, pet: tuple = None):

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
            'Defence Against the Dark Arts': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Muggle Studies': False,
            'Potions': False,
            'Transfiguration': False}

        self._friends = []

    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Griffindor', 1991,
                   ('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronald Bilius Weasley', 1980, 'male', 'Griffindor', 1991,
                   ('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        return cls('Hermione Jean Granger', 1979, 'female', 'Griffindor', 1991,
                   ('Crookshanks', 'cat'))

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def owls(self):
        return self._owls

    @property
    def friends(self):
        return (f"{self._name}'s current friends are: "
                f"{[person.name for person in self._friends]}")

    @owls.setter
    def owls(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items:\
                             subject and grade")

        passed = self.passed(grade)

        if passed:
            self._owls[subject] = True
        else:
            print('The exam was not passed so no OWL was awarded!')

    @owls.deleter
    def owls(self):
        print("Caution, you are deleting this students' OWL's! "
              "You should only do that if she/he dropped out of school"
              "without passing any exam!")
        del self._owls

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
            'P': False,
            'Poor': False,
            'D': False,
            'Dreadful': False,
            'T': False,
            'Troll': False, }

        return grades.get(grade, False)

    def befriend(self, person):
        """Adds another person to your list of friends"""
        if (person.__class__.__name__ != 'HogwartsMember'
                and self.house != 'Slytherin'
                and person.house == 'Slytherin'):

            print("Are you sure you want to be friends with someone"
                  "from Slytherin?")

        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear},"
                f"house: {self.house})")


class Charm:
    """Creates a charm"""

    def __init__(self, incantation: str, difficulty: str = None,
                 effect: str = None):
        self.incantation = incantation
        self.difficulty = difficulty
        self.effect = effect

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def lumos(cls):
        return cls('Lumos', 'simple', 'Illuminates the wand tip')

    @classmethod
    def wingardium_leaviosa(cls):
        return cls('Wingardium Leviosa', 'simple', 'Makes objects fly')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.incantation}, "
                f"{self.difficulty}, {self.effect}.)")


if __name__ == "__main__":
    now = 2018
    hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1958, sex='male')

    harry = Pupil(name='Harry James Potter', birthyear=1990, sex='male',
                  house='Griffindor', start_year=2001)

    ron = Pupil.ron()

    harry.befriend(hagrid)
    harry.befriend(ron)
    print(harry.friends)
    print()

    lumos = Charm.lumos()
    lumos.cast()

    hagrid.add_trait('Kind')
    hagrid.add_trait('monster-loving')
    hagrid.add_trait('impatient', value=False)

    hagrid.print_traits()
