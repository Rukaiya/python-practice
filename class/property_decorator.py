from pprint import pprint

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('Age must be positive')
        self._age = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name cannot be blank')
        self._name = value


person = Person('Rukaiya', 27)

print(person.name)
print(person.age)

pprint(Person.__dict__)