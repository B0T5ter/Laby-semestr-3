import FIFO_queue_ver_02_linked_list_poprawne
import stos_tablica
Kolejka = FIFO_queue_ver_02_linked_list_poprawne.Queue
Stos = stos_tablica.Stack_01
class Node:
    def __init__(self, dane):
        self.dane = dane
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    #Left root right
    def inOrder(self):
        self._inOrder(self.root)
        
    def _inOrder(self, x):
        if x != None:
            self._inOrder(x.left)
            print(x.dane)
            self._inOrder(x.right)

    #left right root
    def postOrder(self):
        self._postOrder(self.root)
    
    def _postOrder(self, x):
        if x != None:
            self._postOrder(x.left)
            self._postOrder(x.right)
            print(x.dane)
            
    def preOrder(self):
        self._preOrder(self.root)
    
    #Root left right
    def _preOrder(self, x):
        if x != None:
            print(x.dane)
            self._preOrder(x.left)
            self._preOrder(x.right)

    def weight(self):
        return self._weight(self.root)

    def _weight(self, x):
        if x == None:
            return 0
        return 1 + self._weight(x.right) + self._weight(x.left)
    
    def leefs(self):
        return self._leafs(self.root)
    
    def _leafs(self, x):
        if x == None:
            return 0
        if x.left == None and x.right == None:
            return 1
        return self._leafs(x.right) + self._leafs(x.left)

    def height(self):
        return self._height(self.root)
    
    def _height(self, x):
        if x == None:
            return -1
        return 1 + max(self._height(x.left), self._height(x.right))
    
    def breadthFirst(self):
        kol = Kolejka()
        kol.enqueue(self.root)

        while not kol.isEmpty():
            node = kol.first()
            kol.dequeue()
            print(node.dane)
            if node.left != None:
                kol.enqueue(node.left)
            if node.right != None:
                kol.enqueue(node.right)
        
    def deepFirst(self):
        sto = Stos()
        sto.push(self.root)

        while not sto.isEmpty():
            node = sto.top()
            sto.pop()
            print(node.dane)
            if node.right is not None:
                sto.push(node.right)
            if node.left is not None:
                sto.push(node.left)

a = BinaryTree((Node("A")))
a.root.left = Node("B")
a.root.right = Node("C")
a.root.left.left = Node("D")
a.root.left.right = Node("E")
a.root.right.left = Node("F")
a.root.right.right = Node("G")
a.preOrder()
print("---")
a.inOrder()
print("---")
a.postOrder()
print("---")
wagaa = a.weight()
print(wagaa)
leafss = a.leefs()
print(leafss)
wysokosc = a.height()
print(wysokosc)
print("---")
a.breadthFirst()
print("---")
a.deepFirst()