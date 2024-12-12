import heapq

def dijkstra(graph, start):
    # Inicjalizacja struktur danych
    distances = {node: float('inf') for node in graph}  # Dystanse do wierzchołków
    distances[start] = 0
    priority_queue = [(0, start)]  # Kolejka priorytetowa (koszt, wierzchołek)
    previous_nodes = {node: None for node in graph}  # Poprzedni wierzchołek na ścieżce

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jeśli znaleziono dłuższą ścieżkę, pomiń
        if current_distance > distances[current_node]:
            continue

        # Przeglądanie sąsiadów
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Aktualizacja dystansu, jeśli znaleziono lepszą ścieżkę
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Przykładowy graf jako słownik sąsiedztwa
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

# Wywołanie algorytmu Dijkstry
start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

# Wyniki
print("Najkrótsze dystanse od", start_node, ":", distances)
print("Trasa:", previous_nodes)
