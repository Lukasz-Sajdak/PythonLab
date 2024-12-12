import json
from dataclasses import dataclass


@dataclass
class PersonalData:
    first_name: str
    last_name: str
    address: str
    postal_code: str
    pesel: str

    def to_dict(self):
        """Konwertuje obiekt na słownik."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "postal_code": self.postal_code,
            "pesel": self.pesel,
        }

    @staticmethod
    def from_dict(data):
        """Tworzy obiekt na podstawie słownika."""
        return PersonalData(**data)

    def save_to_json(self, file_path):
        """Zapisuje dane obiektu do pliku JSON."""
        with open(file_path, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @staticmethod
    def load_from_json(file_path):
        """Wczytuje dane z pliku JSON i tworzy obiekt klasy."""
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
