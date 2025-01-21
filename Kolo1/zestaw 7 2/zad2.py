class Node:
    def __init__(self, dane = None, prio = None, next = None):
        self.dane = dane
        self.prio = prio
        self.next = next

class prioQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.maxSize = 5

    def isEmpty(self):
        return self.size == 0
    
    def add(self, dane, prio):
        
        nowy = Node(dane, prio)
        if self.isEmpty() == True:
            self.head = nowy
            self.tail = nowy
            self.size += 1
            return
        elif self.size < self.maxSize and self.size != 0:
            self.tail.next = nowy
            self.tail = nowy
            self.size += 1
            return
        elif self.size == self.maxSize:
            akt = self.head
            while akt != None:
                if akt.prio < prio:
                    akt.dane = dane
                    akt.prio = prio
                    return
                akt = akt.next
            akt = self.head
            while akt != None:
                if akt.prio == prio:
                    akt.dane = dane
                    akt.prio = prio
                    return
                akt = akt.next
        print("Za niski priorytet węzła", dane, prio)
    def ret_all(self):
        akt = self.head
        ret = []
        while akt != None:
            ret.append([akt.dane, akt.prio])
            akt = akt.next
        print(ret)

a = prioQueue()
a.add(1,1)
a.add(2,1)
a.add(3,1)
a.add(4,1)
a.add(5,1)
a.add(6,1)
a.add(7,0)
a.ret_all()