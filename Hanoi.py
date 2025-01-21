def hanoi(n, A, B, C):
    # n - liczba krążków
    # A - pręt źródłowy
    # B - pręt docelowy
    # C - pręt pomocniczy
    if n == 1:
        print(f"({A}, {B})")  # Przenosimy jeden krążek
    else:
        hanoi(n-1, A, C, B)  # Przenosimy n-1 krążków z A na C, używając B
        print(f"({A}, {B})")  # Przenosimy największy krążek z A na B
        hanoi(n-1, C, B, A)  # Przenosimy n-1 krążków z C na B, używając A

# Główna część programu
n = 4
hanoi(n, 'A', 'B', 'C')  # Wywołujemy funkcję rekurencyjną
