class Queue:
    def __init__(self) -> None:
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

a_queue = Queue()
print(a_queue.is_empty())

for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())

while a_queue.size():
    print(a_queue.dequeue())

print()
print(a_queue.size())


