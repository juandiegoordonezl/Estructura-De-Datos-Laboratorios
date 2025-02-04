from heap import*

class PriorityQueue(HEAP):
    def __init__(self, capacity):
        super().__init__(capacity)

    def heap_maximum(self):
        if self.size < 1:
            raise Exception("Heap vacío")
        return self.A[0]

    def heap_extract_max(self):
        if self.size < 1:
            raise Exception("Heap vacío")
        max_val = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return max_val

    def max_heap_insert(self, key):
        if self.size >= len(self.A):
            raise Exception("Heap lleno")
        self.size += 1
        i = self.size - 1
        self.A[i] = key
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
            i = self.parent(i)
