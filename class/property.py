from pprint import pprint
import string
from unicodedata import name 

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError ('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age
    
    age = property(fset=set_age, fget=get_age)
        

pprint(Person.age)
pprint(Person.__dict__)

person = Person('Rukaiya', 27)
pprint(person.__dict__)
