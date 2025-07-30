class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
