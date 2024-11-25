import random

numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Liczby przed sortowaniem: {numbers}")


# metoda 1:
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# metoda 2:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


bubble = bubble_sort(numbers.copy())
print(f"Bubble Sort: {bubble}")

selection = selection_sort(numbers.copy())
print(f"Selection Sort: {selection}")

sorted = sorted(numbers)
print(f"Liczby posortowane wbudowana funkcja: {sorted}")
