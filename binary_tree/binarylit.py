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
    
    def inOrder(self):
        stack = []
        node = self.root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.dane, end = " ")
            node = node.right
        print()

    #Left root right
    def preOrder(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.dane, end = " ")
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        print()

    def postOrder(self):
        if not self.root:
            return
        stack = []
        output = []
        stack.append(self.root)
        while stack:
            current = stack.pop()
            output.append(current.dane)  # Wypisujemy węzeł po przetworzeniu
            if current.left:  # Najpierw dodajemy lewe poddrzewo
                stack.append(current.left)
            if current.right:  # Potem dodajemy prawe poddrzewo
                stack.append(current.right)
        while output:  # Odwracamy kolejność (bo post-order to lewo, prawo, korzeń)
            print(output.pop(), end=" ")

a = BinaryTree((Node("A")))
a.root.left = Node("B")
a.root.right = Node("C")
a.root.left.left = Node("D")
a.root.left.right = Node("E")
a.root.right.left = Node("F")
a.root.right.right = Node("G")
a.preOrder()

a.inOrder()

a.postOrder()

