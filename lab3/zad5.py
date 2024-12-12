class State:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}  # Przejścia w formacie {input: next_state}

    def add_transition(self, input_value, next_state):
        self.transitions[input_value] = next_state


class MooreMachine:
    def __init__(self, start_state):
        self.current_state = start_state

    def process_input(self, input_sequence):
        outputs = [self.current_state.output]
        for input_value in input_sequence:
            if input_value in self.current_state.transitions:
                self.current_state = self.current_state.transitions[input_value]
                outputs.append(self.current_state.output)
            else:
                raise ValueError(f"Nieznane wejście '{input_value}' dla stanu {self.current_state.name}")
        return outputs


# Przykład użycia
if __name__ == "__main__":
    # Definiowanie stanów
    q0 = State("q0", "A")
    q1 = State("q1", "B")
    q2 = State("q2", "C")

    # Dodanie przejść między stanami
    q0.add_transition(0, q0)
    q0.add_transition(1, q1)
    q1.add_transition(0, q2)
    q1.add_transition(1, q1)
    q2.add_transition(0, q0)
    q2.add_transition(1, q1)

    # Tworzenie automatu
    moore_machine = MooreMachine(q0)

    # Przetwarzanie sekwencji wejść
    input_sequence = [1, 0, 1, 0, 0, 1]
    outputs = moore_machine.process_input(input_sequence)

    print("Sekwencja wejść:", input_sequence)
    print("Sekwencja wyjść:", outputs)
