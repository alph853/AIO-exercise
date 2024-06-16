class Stack:
    def __init__(self, cap):
        self._capacity = cap
        self._elements = []

    def is_empty(self):
        return len(self._elements) == 0

    def is_full(self):
        return len(self._elements) == self._capacity

    def push(self, element):
        if self.is_full():
            return False
        self._elements.append(element)
        return True

    def pop(self):
        if self.is_empty():
            return None
        return self._elements.pop()

    def top(self):
        if self.is_empty():
            return None
        return self._elements[-1]

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        return "Stack contents: " + ", ".join(map(str, self._elements))


def ex3():
    s = Stack(5)

    while not s.is_full():
        s.push(s.top() + 1 if not s.is_empty() else 0)
        print(s)

    while not s.is_empty():
        s.pop()
        print(s)
