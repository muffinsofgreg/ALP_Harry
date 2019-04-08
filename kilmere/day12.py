import datetime
from collections import namedTuple


class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not
                        value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait: '{trait}'")
            return
        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}")

    def says(self, words):
        return f"{self._name} says {words}"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name},"
                f"birthyear: {self.birthyear})")


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str,
                 house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        if house is not None:
            self.house = house

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration',
                   'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int,
                 house: str = None):
        super().__init__(name, birthyear, sex)

        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492, 'House of Courage')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death:"
                f" {self.year_of_death})")


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str,
                 start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
            'Broomstick Flying': False,
            'Art': False,
            'Magical Theory': False,
            'Foreign Magical Systems': False,
            'Charms': False,
            'Defence Against Dark Magic': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Potions': False,
            'Transfiguration': False}

        self._friends = []

    @classmethod
    def cleon(cls):
        return cls('Cleon Bery', 2008, 'male', 'House of Courage',
                   2018, ('Cotton', 'owl'))

    @classmethod
    def flynn(cls):
        return cls('Flynn Gibbs', 2008, 'male', 'House of Courage',
                   2018, ('Twiggles', 'owl'))

    @classmethod
    def cassidy(cls):
        return cls('Cassidy Ambergem', 2007, 'female', 'House of Courage',
                   2018, ('Ramses', 'cat'))

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def friends(self):
        return f"{self._name}'s current friends are:" \
               f"{[person.name for person in self._friends]}"

    @property
    def elms(self):
        return self._elms

    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items:
                             subject and grade")

        passed = self.passed(grade)

        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so no ELM was awarded!')

    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this students' ELM's! ")
        print("You should only do that if she/he dropped out of school",
              "without passing any exam!")
        del self._elms

    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """

        grades = {
            'E': True,
            'Exceptional': True,
            'G': True,
            'Good': True,
            'A': True,
            'Acceptable': True,
            'P': False,
            'Poor': False,
            'H': False,
            'Horrible': False,
        }

        return grades.get(grade, False)

    def befriend(self, person):
        """Adds another person to your list of friends"""

        if (person.__class__.__name__ != 'CastleKilmereMember'
                and self.house != 'House of Ambtion'
                and person.house == 'House of Ambition'):

            print("Are you sure you want to be friends with someone from House \
                  Ambition?")

        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear},
                   house: {self.house})")


class Charm:
    """Creates a Charm"""

    def __init__(self, incantation: str, difficulty: str, effect: str):
        self.incantation = incantation
        self.difficulty = difficulty
        self.effect = effect

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def stuporus_ratiato(cls):
        return cls('Stuporous Ratiato', 'simple', 'Makes objects fly')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.incantation},"\
               f"{self.difficulty}, {self.effect})"


if __name__ == "__main__":
    now = 1993
    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959,
                                  sex='male')

    cleon = Pupil(name='Cleon Bery', birthyear=2008, sex='male',
                  house='House of Courage', start_year=2018)
    print('Cleon: ', cleon)
    print('Current age of cleon: ', cleon.age)
    print("Cleon's elms: ", cleon.elms)

    cleon.elms = ('Potions', 'P')
