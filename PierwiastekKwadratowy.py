

def bisekcja(liczba, prawa = None, lewa = 0, eps = 0.01):
    if prawa == None:
        prawa = liczba
    srodek = (prawa + lewa)/2
    wynik = srodek **2

    roznica = abs(wynik - liczba)
    if roznica < eps:
        return srodek
    
    if wynik > liczba:
        return bisekcja(liczba, srodek, lewa, eps)
    if wynik < liczba:
        return bisekcja(liczba, prawa, srodek, eps)

print(bisekcja(100))
