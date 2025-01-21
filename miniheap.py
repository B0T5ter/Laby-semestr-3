class Node:
    def __init__(self, var):
        self.var = var
        self.left = None
        self.right = None

class miniHeap:
    def __init__(self):
        self.root = None

    def insert(self, var):
        if not self.root:
            self.root = Node(var)
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if current.left is None:
                    current.left = Node(var)
                    self._heapify_up(current.left)
                    return
                if current.right is None:
                    current.right = Node(var)
                    self._heapify_up(current.right)
                    return
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
    
    def _heapify_up(self, node):
        parent = self._get_parent(node)
        if parent.var > node.var:
            parent.var, node.var = node.var, parent.var
            if parent != self.root:
                self._heapify_up(parent)

    def _get_parent(self, node):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left == node or current.right == node:
                return current
            queue.append(current.left)
            queue.append(current.right)
    
    def get_root(self):
        root_val = self.root.var
        if self.root.left is None and self.root.right is None:
            self.root = None
            return root_val
        
        last_val = self.get_last()
        self.root.var = last_val
        self._heapify_down(self.root)
        return root_val
    
    def get_last(self):
        queue = [self.root]
        last = None
        while queue:
            last = queue.pop(0)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        
        parent = self._get_parent(last)
        if parent:
            if parent.right == last:
                parent.right = None
            elif parent.left == last:
                parent.left = None
        
        return last.var
    
    def _heapify_down(self, node):
        smallest = node
        if node.left and node.left.var < smallest.var:
            smallest = node.left
        if node.right and node.right.var < smallest.var:
            smallest = node.right
    
        if smallest != node:
            node.var, smallest.var = smallest.var, node.var
            self._heapify_down(smallest) 

heap = miniHeap()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
print(heap.root.var)
print(heap.root.left.var) 
print(heap.root.right.var)  
print(heap.root.left.left.var) 
print("root:", heap.get_root())
print(heap.root.var)
print(heap.root.left.var) 
print(heap.root.right.var)  
heap.insert(6)
print(heap.root.left.left.var) 