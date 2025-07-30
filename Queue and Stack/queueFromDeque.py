from collections import deque
import time
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """
        Add item to the back of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return item from the front of the queue.
        Raise an error if the queue is empty.
        """
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def peek(self):
        """
        Return the item at the front without removing it.
        Raise an error if the queue is empty.
        """
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue[0]

    def is_empty(self):
        """
        Return True if the queue is empty, else False.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the number of items in the queue.
        """
        return len(self.queue)


# Queue with list
lst = []
start = time.time()
for i in range(100000):
    lst.append(i)     # enqueue
for i in range(100000):
    lst.pop(0)        # dequeue: slow
print("List queue time:", time.time() - start)

# Queue with deque
dq = deque()
start = time.time()
for i in range(100000):
    dq.append(i)
for i in range(100000):
    dq.popleft()      # fast
print("Deque queue time:", time.time() - start)
