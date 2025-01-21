class Node:
    def __init__(self, var):
        self.var = var
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self):
        self.head = None

    def insert(self, var):
        if self.head == None:
            self.head = Node(var)
        else:
            self._insert(self.head, var)
    
    def _insert(self, node, var):
       queue = [node]
       while queue:
           current = queue.pop(0)
           if current.left is None:
               current.left = Node(var)
               self._heapyfy_up(current.left)
               return
           elif current.right is None:
               current.right = Node(var)
               self._heapyfy_up(current.right)
               return
           else:
               queue.append(current.left)
               queue.append(current.right)

    def _heapyfy_up(self, node):
        while node and node != self.head:
            parent = self.get_parent(node)
            if parent.var < node.var:
                node.var, parent.var = parent.var, node.var
                node = parent
            else:
                break
    def get_parent(self, node):
        queue = [self.head]
        while queue:
            current = queue.pop(0)
            if current.left == node or current.right == node:
                return current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return None
    
    def get_root(self):
        if not self.head:
            return None
        ret = self.head.var
        if not self.head.left and not self.head.right:
            self.head = None
            return ret
        
        last_node = self._get_and_remove_last_node(self.head)
        self.head.var = last_node.var

        self._heapyfy_down(self.head)
        return ret

    def _heapyfy_down(self, node):
        largest = node
        if node.left and node.left.var > largest.var:
            largest = node.left
        if node.right and node.right.var > largest.var:
            largest = node.right
        if largest != node:
            node.var, largest.var = largest.var, node.var
            self._heapyfy_down(largest)
        
    def _get_and_remove_last_node(self, node):
        queue = [node]
        last_node = None
        while queue:
            last_node = queue.pop(0)
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        if last_node.right == last_node:
            last_node.right = None
        elif last_node.left == last_node:
            last_node.left = None

        return last_node
    
    def pre_order(self):
        if self.head:
            self._pre_order(self.head)
    
    def _pre_order(self, node):
        if node:
            print(node.var, end = " ")
            self._pre_order(node.left)
            self._pre_order(node.right)
    
    def post_order(self):
        if self.head:
            self._post_order(self.head)
    
    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.var, end = " ")

    def in_order(self):
        if self.head:
            self._in_order(self.head)
    
    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.var, end = " ")
            self._in_order(node.right)

    def deep_first(self):
        if not self.head:
            return None
        queue = [self.head]
        while queue:
            current = queue.pop(0)
            print(current.var, end = " ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
    def bfs(self):
        if not self.head:
            print("Kopiec jest pusty.")
            return

        # BFS - Poziomowe odwiedzanie węzłów
        queue = [self.head]
        while queue:
            node = queue.pop(0)
            print(node.var, end=" ")

            # Dodaj dzieci węzła do kolejki
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def print_heap(self):
        if not self.head:
            print("Kopiec jest pusty.")
            return

        # BFS - Poziomowe wypisywanie drzewa
        queue = [self.head]
        level = 0
        while queue:
            # Wypisz elementy na bieżącym poziomie
            level_size = len(queue)
            print(f"Poziom {level}: ", end="")
            for _ in range(level_size):
                node = queue.pop(0)
                print(node.var, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()  # Przejdź do nowej linii
            level += 1

# Przykładowe użycie:
heap = MaxHeap()
heap.insert(5)
heap.insert(6)
heap.insert(4)
heap.insert(1)
heap.insert(3)
heap.insert(2)


heap.print_heap()    
#print(heap.get_root())
heap.pre_order()
print()
heap.in_order()
print()
heap.post_order()
print()
heap.deep_first()
print()
heap.bfs()
print()
print(heap.head.left.var)