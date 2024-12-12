# Definicja dekoratora
def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Wywołanie oryginalnej funkcji
        if isinstance(result, str):  # Sprawdzenie, czy wynik to string
            return result.upper()  # Zamiana na wielkie litery
        return result
    return wrapper


# Funkcja z dekoratorem
@to_uppercase
def print_message():
    return "Hello, world!"


# Wywołanie funkcji
if __name__ == "__main__":
    print(print_message())  # Wypisze: "HELLO, WORLD!"
