class MaxHeap:
    def __init__(self):
        self.heap = []
        self.length = 0

    # Add the data to the heap
    def push(self, data):
        self.heap.append(data)

        self.length += 1
        index = self.length - 1
        self._heapify_up(index)
        return data

    # Remove and return the maximum element from the heap
    def pop(self):
        if not self.heap:
            return None

        if self.length == 1:
            self.length -= 1
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.length -= 1
        self._heapify_down(0)
        return root

    # Maintain the heap property starting from the given index (from leaf to root)
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    # Maintain the heap property starting from the given index (from root to leaf)
    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < self.length and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < self.length and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    # Constructs a heap from a list of elements,
    # arranging them to satisfy the heap property by using _heapify_down for each non-leaf node.
    def build_heap(self, lst):
        if not isinstance(lst, list):
            return

        self.heap = lst
        for i in range(len(lst) // 2 - 1, -1, -1):
            self._heapify_down(i)


maxheap = MaxHeap()
maxheap.push(10)
maxheap.push(8)
maxheap.push(11)
maxheap.push(5)
maxheap.push(14)
maxheap.push(2)
print(maxheap.heap)
