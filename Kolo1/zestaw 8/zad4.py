
def hanoi(n, poczatek = "A", koniec = "B", pomocniczy = "C"):
    if n == 1:
        print(poczatek, koniec)
        return
    hanoi(n - 1, poczatek, pomocniczy, koniec)
    # Przenieś największy krążek na pręt docelowy
    print(poczatek , koniec)
    # Przenieś n-1 krążków na pręt docelowy
    hanoi(n - 1, pomocniczy, koniec, poczatek)

hanoi(3)