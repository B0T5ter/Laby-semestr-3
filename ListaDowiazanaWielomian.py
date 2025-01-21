class Node:
    def __init__(self, wartosc, potega):
        self.wartosc = wartosc
        self.potega = potega
        self.next_node = None

class Wielomian:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, wartosc, potega):
        nowy = Node(wartosc, potega)

        if self.head == None:
            self.head = nowy
            self.tail = nowy
            return 
        #Dodawanie gdy istnieje
        akt = self.tail
        while akt != None and potega <= akt.potega:
            if akt.potega == potega:
                akt.wartosc += wartosc
            akt = akt.next_node

        #Dodawanie gdy nieistnieje
        dodatkowy = Node(self.tail.wartosc, self.tail.potega)
        dodatkowy.next_node = self.tail
        self.tail = dodatkowy

        akt = self.tail.next_node
        while akt != None and akt.potega <= potega:
            akt.potega = akt.next_node.potega
            akt.wartosc = akt.next_nowe.potega
        akt.wartosc = wartosc
        akt.potega = potega


        

    def all(self):
        akt = self.tail
        while akt != None:
            print(akt.wartosc, akt.potega)
            akt = akt.next_node

a = Wielomian()
a.enqueue(2,3)
a.enqueue(3,2)
a.all()