class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """Przeciążenie operatora dodawania"""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Przeciążenie operatora odejmowania"""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        """Reprezentacja liczby zespolonej w czytelnej postaci"""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"


# Przykład użycia
z1 = ComplexNumber(3, 4)  # 3 + 4i
z2 = ComplexNumber(1, -2)  # 1 - 2i

# Dodawanie
z3 = z1 + z2  # 4 + 2i
print(f"Dodawanie: {z1} + {z2} = {z3}")

# Odejmowanie
z4 = z1 - z2  # 2 + 6i
print(f"Odejmowanie: {z1} - {z2} = {z4}")
