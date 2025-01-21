class Node:
    def __init__(self, var):
        self.var = var
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, var):
        self.heap.append(var)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1)//2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def get_root(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.head.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest = index

        if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
            largest = right_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_up(largest)


    def print_heap(self):
    
        if not self.heap:
            print("Kopiec jest pusty.")
            return

        level = 0
        count = 0
        max_level = 0
        size = len(self.heap)

        # Oblicz maksymalny poziom na podstawie rozmiaru kopca
        while (1 << max_level) - 1 < size:
            max_level += 1

        while count < size:
            level_size = 1 << level  # Liczba elementów na danym poziomie
            start_index = count
            end_index = min(start_index + level_size, size)

            # Drukuj elementy na bieżącym poziomie z odpowiednią liczbą odstępów
            indent = " " * (2 ** (max_level - level) - 1)
            between = " " * (2 ** (max_level - level + 1) - 1)

            print(indent + between.join(map(str, self.heap[start_index:end_index])))

            level += 1
            count = end_index

heap = MaxHeap()
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(65)
heap.insert(40)
heap.insert(23)
heap.insert(51)
heap.insert(37)
heap.insert(21)
heap.print_heap()
heap.in_order()
