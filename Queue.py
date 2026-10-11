from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

#    def sort(self):
#        self.queue = deque(sorted(self.queue))

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", list(self.queue))


arr = [12, 13, 14, 32, 43, 65, 71, 33, 16]

q = Queue()

for item in arr:
    q.enqueue(item)

q.display()

print("Dequeued:", q.dequeue())

print("Queue after dequeue:")
q.display()