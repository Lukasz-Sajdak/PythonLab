import json


class PersonalData:
    def __init__(self, first_name, last_name, address, postal_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel

    def to_dict(self):  # obiekt na słownik
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "postal_code": self.postal_code,
            "pesel": self.pesel
        }

    @staticmethod
    def from_dict(data):  # obiekt na podstawie słownika
        return PersonalData(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            postal_code=data["postal_code"],
            pesel=data["pesel"]
        )

    def save_to_json(self, file_path):
        with open(file_path, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @staticmethod
    def load_from_json(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return PersonalData.from_dict(data)


# Przykład użycia
if __name__ == "__main__":
    # Tworzenie obiektu
    person = PersonalData(
        first_name="Jan",
        last_name="Kowalski",
        address="ul. Przykładowa 1, Warszawa",
        postal_code="00-001",
        pesel="12345678901"
    )
    # Zapis do JSON
    person.save_to_json("person_data.json")
    # Wczytanie z JSON
    loaded_person = PersonalData.load_from_json("person_data.json")
    print("Wczytane dane:")
    print(f"Imię: {loaded_person.first_name}")
    print(f"Nazwisko: {loaded_person.last_name}")
    print(f"Adres: {loaded_person.address}")
    print(f"Kod pocztowy: {loaded_person.postal_code}")
    print(f"PESEL: {loaded_person.pesel}")
