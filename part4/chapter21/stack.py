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


stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
item = stack.pop()
print(item)
print(stack.is_empty())

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())

stack_string = Stack()
for c in "Hello":
    stack_string.push(c)

reverse = ""
while stack_string.size():
    reverse += stack_string.pop()

print(reverse)
