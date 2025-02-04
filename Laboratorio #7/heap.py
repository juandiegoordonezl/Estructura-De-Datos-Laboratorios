class HEAP:
    def __init__(self, capacity):
        self.A = [None] * capacity  
        self.size = 0              

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < self.size and self.A[l] > self.A[largest]:
            largest = l
        if r < self.size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def build_max_heap(self, B):
        self.A = B[:]
        self.size = len(B)
        for i in range(self.size // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap(self.A)
        for i in range(self.size - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.size -= 1
            self.max_heapify(0)
        return self.A
