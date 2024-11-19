class Node:
    def __init__(self, dane = None, prio = None, next = None):
        self.dane = dane
        self.prio = prio
        self.next = next

class Queue:
    def __init__(self):
         self.prawa = None
         self.lewa = None
         self.size = 0
         self.max_size = 5
    
    def isEmpty(self):
        return self.size == 0
    
    def add(self, dane, prio):
        nowy = Node(dane, prio)
        if self.size < self.max_size:
            if self.isEmpty():
                self.prawa = nowy
            else:
                self.lewa.next = nowy
            self.lewa = nowy
            self.size += 1
            return
        rowny = None
        aktualny = self.prawa
        while aktualny != None:
            if aktualny.prio == prio and rowny == None:
                rowny = aktualny
            if aktualny.prio < prio:
                aktualny.dane = dane
                aktualny.prio = prio
                return
            aktualny = aktualny.next
        if rowny != None:
            rowny.dane = dane
            rowny.prio = prio
        else:
            print("Za niski priorytet by dodać do kolejki:", dane,"|prio:", prio)
    def sub(self):
        self.size -= 1
        self.prawa = self.prawa.next

    def ret_all(self):
        ret = []
        aktualny = self.prawa
        while aktualny != None:
            ret.append((aktualny.dane, aktualny.prio))
            aktualny = aktualny.next
        print(ret[::-1])

    

a = Queue()
a.add("a", 1)
a.add("b", 1)
a.add("c", 1)
a.add("d", 1)
a.add("e", 1)
a.add("x", 2)
a.add("y", 2)
a.add("z", 2)
a.add("x", 2)
a.add("y", 2)
a.add("z", 2)
a.add("z", 1)
print(a.size)
a.ret_all()