# coding: utf-8
# Prosta implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# stos zaimplementowany jako tablica (lista w j. Python)
# brak obslugi bledow (np. kiedy stos jest pusty lub braku pamieci na nowy element)
# materialy do wykladu AiSD, Michal Baczynski

class Stack_01:
    """Implementacja stosu za pomoca listy Pythona, czyli klasycznej tablicy"""
    def __init__(self):
        """inicjalizacja"""
        self.tablica = []
    def isEmpty(self):
        """sprawdzenie czy stos jest pusty"""
        return self.tablica == []
    def push(self, item):
        """wlozenie elementu na (szczyt) stos"""
        self.tablica.append(item)
        return
    def pop(self):
        """sciagniecie elementu ze (szczytu) stosu"""
        # Brak obslugi bledow
        self.tablica.pop()
        return
    def top(self):
        """zwrocenie elementu ze (szczytu) stosu"""
        return self.tablica[len(self.tablica)-1]
    def size(self):
        """zwrocenie rozmiaru stosu"""
        return len(self.tablica)

