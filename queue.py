'''
This Python project creates a new class to implement a Queue. This is a common data structure in computer science when you need to handle First-In-First-Out (FIFO) scenarios, such as message queues, CPU tasks, etc.
'''
class Queue:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return f'Queue object: data={self.items}'

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeque(self):
        return self.items.pop(0)    

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]                    

if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue('First')
    q.enqueue('Second')
    print(q)
    print(q.dequeque())
    print(q)
    print(q.size())
    print(q.peek())