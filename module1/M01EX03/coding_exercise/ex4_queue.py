class Queue:
    # circular queue implementation because of pre-defined capacity
    def __init__(self, cap):
        self._elements = [None] * cap
        self._capacity = cap
        self._start = -1
        self._end = -1

    def is_empty(self):
        return self._start == -1

    def is_full(self):
        return (self._end + 1) % self._capacity == self._start

    def enqueue(self, x):
        if self.is_full():
            return False

        if self.is_empty():
            self._start = 0

        self._end = (self._end + 1) % self._capacity
        self._elements[self._end] = x

    def dequeue(self):
        if self.is_empty():
            return None
        res = self._elements[self._start]

        if self._start == self._end:
            self._start = -1
            self._end = -1
        else:
            self._start = (self._start + 1) % self._capacity

        return res

    def front(self):
        if self.is_empty():
            return None
        return self._elements[self._start]

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        elements = []
        i = self._start
        while True:
            elements.append(str(self._elements[i]))
            if i == self._end:
                break
            i = (i + 1) % self._capacity
        return "Queue contents: " + ", ".join(elements)


def ex4():
    q = Queue(5)

    while not q.is_full():
        q.enqueue(q._end + 1)
        print(q)

    print(f'Try to enqueue... {q.enqueue(100)}. Is queue full? {q.is_full()}')

    print(f'Front: {q.front()}')
    print(f'Dequeue: {q.dequeue()}')
    print(f'Front: {q.front()}')

    while not q.is_empty():
        print(f'Dequeue: {q.dequeue()}')
        print(q)

    print(q)


