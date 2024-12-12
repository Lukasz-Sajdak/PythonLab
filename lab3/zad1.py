def multiply_matrices(matrix_a, matrix_b):
    # Sprawdzenie zgodności wymiarów macierzy
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Liczba kolumn macierzy A musi być równa liczbie wierszy macierzy B.")

    # Inicjalizacja macierzy wynikowej
    result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]

    # Mnożenie macierzy
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][k] += matrix_a[i][k] * matrix_b[k][j]

    return result


# Przykład użycia
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(matrix_a, matrix_b)

print("Macierz wynikowa:")
for row in result:
    print(row)
