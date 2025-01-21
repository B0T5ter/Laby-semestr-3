class Node:
    def __init__(self, dane = None, next = None):
        self.dane = dane
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, dane):
        self.size += 1
        nowy = Node(dane)
        if self.tail == None:
            self.head = nowy
        else:
            self.tail.next = nowy
        self.tail = nowy
    
    def sub(self, dane = None):
        if dane == None:
            self.head = self.head.next
            self.size -= 1
        else:
            if self.head.dane == dane:
                self.head = self.head.next
                self.size -= 1
            else:
                poprzednie = self.head
                aktualne = poprzednie.next
                while aktualne.next != None:
                    if aktualne.dane == dane:
                        poprzednie.next = aktualne.next
                        self.size -= 1
                        return
                    poprzednie = aktualne
                    aktualne = poprzednie.next
                if aktualne.dane == dane:
                    poprzednie.next = aktualne.next
                    self.size -= 1
                    return
            print("brak danych")

    def top(self):
        return self.head.dane

    
    def ret_all(self):
        akt = self.head
        ret = []
        while akt != None:
            ret.append(akt.dane)
            akt = akt.next
        print(ret)

a = Queue()
a.add(1)
a.add(2)
a.add(3)
print(a.top())
a.sub()
a.ret_all()