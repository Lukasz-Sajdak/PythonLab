class Fibonacci:
    def __init__(self, steps):
        self.steps = steps  # Liczba kroków
        self.a, self.b = 0, 1  # Początkowe wartości ciągu Fibonacciego
        self.current_step = 0  # Aktualny krok

    def __iter__(self):
        return self  # Zwraca iterator

    def __next__(self):
        if self.current_step >= self.steps:  # Jeśli osiągnięto liczbę kroków -> StopIteration
            raise StopIteration
        else:
            self.current_step += 1
            self.a, self.b = self.b, self.a + self.b  #kolejne liczby w ciągu Fibonacciego
            return self.a  # Zwracamy aktualny wyraz ciągu Fibonacciego


# Testowanie iteratora
fibonacci = Fibonacci(10)  # Tworzymy iterator Fibonacciego na 10 wyrazów
for number in fibonacci:
    print(number)
