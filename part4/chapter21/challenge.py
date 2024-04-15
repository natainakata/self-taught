class Stack:
    def __init__(self) -> None:
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        last = len(self._items) - 1
        return self._items[last]

    def size(self):
        return len(self._items)

yesterday = Stack()

for c in "yesterday":
    yesterday.push(c)

reverse = ""
while yesterday.size():
    reverse += yesterday.pop()

print(reverse)

list = [1, 2, 3, 4, 5]
reverse_list = []

numbers = Stack()
for i in list:
    numbers.push(i)

while numbers.size():
    reverse_list.append(numbers.pop())

print(reverse_list)
