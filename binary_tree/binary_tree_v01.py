# coding: utf-8
# Prosta implementacja drzewa binarnego w oparciu o dodatkowa klase Node
# Nie ma zaimplementowanego wstawwiania -  to jest zalezna od zastosowan
# Prosze to samemu uzupelnic o inne operacje na drzewie
# Michal Baczynski (AiSD wyklad)

#importujemy plik z naszą klasa kolejki FIFO (np. opartej na liscie dowiazanej)
import FIFO_queue_ver_02_linked_list_poprawne

#importujemy plik z naszą klasa kolejki LIFO/ stosu (np. opartej na tablicy)
import stos_tablica

# dla ułatienia odwolania się do naszych kolejek tworzymy aliasy
Kolejka = FIFO_queue_ver_02_linked_list_poprawne.Queue
Stos = stos_tablica.Stack_01

class Node:
    """Klasa Node - do pamietania pojedynczego wezla w drzewie"""
    def __init__(self, dane=None, left=None, right=None):
        # konstruktor
        # pole "dane" bedzie zawieralo nasze dane np. liczby, napisy lub inne rekordy badz klasy
        # left_node bedzie wskazywalo na lewy wezel
        # right_node bedzie wskazywalo na prawy wezel
        self.dane = dane
        self.left_node  = left
        self.right_node = right

class binaryTree:
    """Klasa drzewo binarne - istotna dana jest tylko korzen"""
    def __init__(self):
        self.korzen = None

    def _preorder(self,drzewo):
        #Wypisywanie drzewa w sposob preorder - procedura wewnetrzna
        if drzewo is not None:
            print(drzewo.dane)
            self._preorder(drzewo.left_node)
            self._preorder(drzewo.right_node)

    def preorder(self):
        #Wypisywanie w porzadku preorder dla korzenia - procedura zeewnetrzna
        self._preorder(self.korzen)

    def _inorder(self,drzewo):
        #Wypisywanie drzewa w sposob inorder - procedura wewnetrzna
        if drzewo is not None:
            self._inorder(drzewo.left_node)
            print(drzewo.dane)
            self._inorder(drzewo.right_node)

    def inorder(self):
        #Wypisywanie w porzadku inorder dla korzenia - procedura zeewnetrzna
        self._inorder(self.korzen)


    def _postorder(self,drzewo):
        # Wypisywanie w porzadku postorder dla korzenia - procedura wewnetrzna
        if drzewo is not None:
            self._postorder(drzewo.left_node)
            self._postorder(drzewo.right_node)
            print(drzewo.dane)

    def postorder(self):
        #Wypisywanie w porzadku postorder dla korzenia - procedura zeewnetrzna
        self._postorder(self.korzen)


    def _breadthFirst(self,drzewo):
        # Wypisywanie metoda przeszukiwania wszerz - procedura wewnetrzna
        # korzystamy z kolejki FIFO (nieistotne jak zaimplementowanej!)
        q = Kolejka()
        # wkladamy do naszej kolejki FIFO korzen
        q.enqueue(drzewo)
        # odwiedzamy kazdy wezel w drzewie
        while not q.isEmpty():
            # wypisujemy i usuwamy to co jest na poczatku kolejki
            node = q.first()
            q.dequeue()
            print(node.dane)
            # i dodajemy dzieci tego wezla do kolejki o ile nie sa puste (czyli "None")
            if node.left_node is not None:
                q.enqueue(node.left_node)
            if node.right_node is not None:
                q.enqueue(node.right_node)

    def breadthFirst(self):
        # Wypisywanie metoda przeszukiwania wszerz - procedura zewnetrzna
        self._breadthFirst(self.korzen)

    def _deepFirst(self,drzewo):
        # Wypisywanie metoda przeszukiwania w głąb - procedura wewnetrzna
        # korzystamy z kolejki LIFO / stosu (nieistotne jak zaimplementowanej!)
        s = Stos()
        # wkladamy do naszej kolejki LIFO korzen
        s.push(drzewo)
        # odwiedzamy kazdy wezel w drzewie
        while not s.isEmpty():
            # wypisujemy i usuwamy to co jest na szczycie stosu
            node = s.top()
            s.pop()
            print(node.dane)
            # i dodajemy dzieci tego wezla do stosu o ile nie sa puste (czyli "None")
            if node.right_node is not None:
                s.push(node.right_node)
            if node.left_node is not None:
                s.push(node.left_node)
            

    def deepFirst(self):
        # Wypisywanie metoda przeszukiwania w głab - procedura zewnetrzna
        self._deepFirst(self.korzen)

    def _waga(self,drzewo):
        if drzewo is None:
            return 0
        return 1+self._waga(drzewo.left_node)+self._waga(drzewo.right_node)

    def waga(self):
        return self._waga(self.korzen)

    def _lb_lisci(self,drzewo):
        if drzewo is None:
            return 0
        if drzewo.left_node is None and drzewo.right_node is None:
            return 1
        return self._lb_lisci(drzewo.left_node)+self._lb_lisci(drzewo.right_node)

    def lb_lisci(self):
        return self._lb_lisci(self.korzen)

    def _wysokosc(self,drzewo):
        if drzewo is None:
            return -1
        return 1+max(self._wysokosc(drzewo.left_node), self._wysokosc(drzewo.right_node))

    def wysokosc(self):
        return self._wysokosc(self.korzen)

# Przykladowe drzewo
#r1 = binaryTree()
#r1.korzen = Node("T")
#r1.korzen.left_node =Node("X")
#r1.korzen.left_node.left_node =Node("B")
#r1.korzen.left_node.right_node=Node("G")
#r1.korzen.left_node.right_node.left_node=Node("Z")
#r1.korzen.right_node =Node("C")
#r1.korzen.right_node.left_node =Node("J")
#r1.korzen.right_node.right_node =Node("R")
#r1.korzen.right_node.right_node.left_node =Node("K")
#r1.korzen.right_node.right_node.left_node.left_node =Node("A")
#r1.korzen.right_node.right_node.right_node=Node("M")

r1 = binaryTree()
r1.korzen = Node("A")
r1.korzen.left_node = Node("B")
r1.korzen.right_node = Node("C")
r1.korzen.left_node.left_node = Node("D")
r1.korzen.left_node.right_node = Node("E")
r1.korzen.right_node.left_node = Node("F")
r1.korzen.right_node.right_node = Node("G")

print("Porzadek Preorder")
r1.preorder()

print("Porzadek Inorder")
r1.inorder()

print("Porzadek Postorder")
r1.postorder()

print("Waga")
print(r1.waga())

print("Liczba lisci")
print(r1.lb_lisci())

print("wysokosc")
print(r1.wysokosc())

print("Przeszukiwanie wszerz")
r1.breadthFirst()

print("Przeszukiwanie w głąb")
r1.deepFirst()
