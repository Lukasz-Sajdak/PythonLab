import json

class Person:

    def __init__(self, first_name, last_name, adress, post_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.post_code = post_code
        self.pesel = pesel

    def to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__,file)

    @classmethod
    def from_json(cls,filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(**data)

person = Person("Jan", "Kowalski", "ul.testowa", "12-345", "12345678900")

jsonfile = "person.json"

person.to_json(jsonfile)



print(f"Person:  {person.__dict__}")

loaded_person = Person.from_json(jsonfile)
print(f"Loaded from {jsonfile}:  {loaded_person.__dict__}")
