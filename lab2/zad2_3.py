import time
import matplotlib.pyplot as plt
import multiprocessing
import random


# Funkcja sortująca przekazany fragment danych
def sort_chunk(chunk):
    return sorted(chunk)


# Sortowanie równoległe
def parallel_sort(data, num_processes):
    # Podział danych na fragmenty odpowiadające liczbie procesów
    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Równoległe sortowanie fragmentów
    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(sort_chunk, chunks)

    # Scalanie i końcowe sortowanie danych
    merged_data = [item for chunk in sorted_chunks for item in chunk]
    return sorted(merged_data)


# Funkcja testująca sortowanie równoległe
def run_sort_tests():
    test_sizes = [10, 50, 100]  # Rozmiary danych testowych
    process_counts = [1, 2, 4]  # Liczby procesów
    results = []

    # Testowanie dla różnych rozmiarów danych i różnej liczby procesów
    for size in test_sizes:
        data = [random.randint(1, 10000) for _ in range(size)]
        for process_count in process_counts:
            start_time = time.time()
            parallel_sort(data, process_count)
            end_time = time.time()
            results.append((size, process_count, end_time - start_time))

    return results


# Wizualizacja wyników testów
def plot_results(results, test_sizes, process_counts):
    plt.figure()
    for size in test_sizes:
        times = [result[2] for result in results if result[0] == size]
        plt.plot(process_counts, times, label=f'Rozmiar: {size}')
    plt.xlabel('Ilość procesów')
    plt.ylabel('Czas')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test_results = run_sort_tests()
    test_sizes = [10, 50, 100]
    process_counts = [1, 2, 4]
    plot_results(test_results, test_sizes, process_counts)
