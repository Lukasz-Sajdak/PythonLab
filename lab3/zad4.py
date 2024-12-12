class TrieNode:
    def __init__(self):
        # Dzieci (słownik znaków do węzłów)
        self.children = {}
        # Lista wzorców (słowa) kończących się w tym węźle
        self.output = []
        # Wskaźnik do węzła fail (węzeł przejścia, jeśli nie ma dopasowania)
        self.fail = None


def build_automaton(patterns):
    # Tworzymy korzeń drzewa trie
    root = TrieNode()

    # Dodawanie wzorców do drzewa trie
    for pattern in patterns:
        node = root
        for char in pattern:
            # Jeśli węzeł dla danego znaku nie istnieje, tworzymy nowy
            if char not in node.children:
                node.children[char] = TrieNode()
            # Przechodzimy do następnego węzła
            node = node.children[char]
        # Po zakończeniu wzorca dodajemy go do listy output w końcowym węźle
        node.output.append(pattern)

    # Kolejka do przetwarzania węzłów
    queue = []
    for node in root.children.values():
        queue.append(node)
        # Ustawiamy fail dla bezpośrednich dzieci korzenia
        node.fail = root

    # Budowanie wskaźników fail dla wszystkich węzłów
    while queue:
        current_node = queue.pop(0)
        # Przechodzimy przez dzieci węzła
        for char, next_node in current_node.children.items():
            queue.append(next_node)
            # Przeszukujemy łańcuch fail dla odpowiedniego przejścia
            fail_node = current_node.fail
            while fail_node and char not in fail_node.children:
                fail_node = fail_node.fail
            # Jeśli fail_node istnieje, ustawiamy fail na odpowiedni węzeł
            next_node.fail = fail_node.children[char] if fail_node else root
            # Łączymy outputy węzłów (dziedziczymy output z fail)
            next_node.output += next_node.fail.output

    return root


def search_text(text, patterns):
    # Budujemy automat dla wzorców
    root = build_automaton(patterns)
    # Inicjalizujemy wynik (słownik z listami pozycji dla każdego wzorca)
    result = {pattern: [] for pattern in patterns}

    # Rozpoczynamy przeszukiwanie tekstu
    current_node = root
    for i, char in enumerate(text):
        # Szukamy dopasowania do bieżącego znaku
        while current_node and char not in current_node.children:
            current_node = current_node.fail

        # Jeśli nie znaleźliśmy dopasowania, wracamy do korzenia
        if not current_node:
            current_node = root
            continue

        # Przechodzimy do następnego węzła
        current_node = current_node.children[char]
        # Dodajemy wyniki (pozycje) dla każdego dopasowanego wzorca
        for pattern in current_node.output:
            result[pattern].append(i - len(pattern) + 1)

    return result


# Testowanie algorytmu
if __name__ == '__main__':
    # Przykładowy tekst
    text = "to jest test"
    # Wzorce do wyszukania
    patterns = ['je', 'o', ' o', 'est', 'kk']
    # Przeszukiwanie tekstu
    result = search_text(text, patterns)
    print(result)
