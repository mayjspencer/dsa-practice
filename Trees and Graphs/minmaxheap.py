import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        return heapq.heappop(self.heap)

    def __str__(self):
        return str(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, -1 * val)

    def get_max(self):
        return -self.heap[0]

    def extract_max(self):
        return (-1 * heapq.heappop(self.heap))

    def __str__(self):
        # Return max-heap as a normal list (not negated)
        return str([-x for x in self.heap])


# === ✅ Test Cases ===

def run_tests():
    print("Testing MinHeap...")
    min_heap = MinHeap()
    for num in [5, 3, 8, 1]:
        min_heap.insert(num)
    assert min_heap.get_min() == 1
    assert min_heap.extract_min() == 1
    assert min_heap.get_min() == 3
    print("MinHeap passed.")

    print("Testing MaxHeap...")
    max_heap = MaxHeap()
    for num in [5, 3, 8, 1]:
        max_heap.insert(num)
    assert max_heap.get_max() == 8
    assert max_heap.extract_max() == 8
    assert max_heap.get_max() == 5
    print("MaxHeap passed.")


if __name__ == "__main__":
    run_tests()
