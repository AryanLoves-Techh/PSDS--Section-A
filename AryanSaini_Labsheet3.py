class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"Push: {value}")

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        removed = self.head.value
        self.head = self.head.next
        print(f"Pop: {removed}")

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print(f"Enqueue: {value}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Enqueue: {value}")

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return
        removed = self.head.value
        self.head = self.head.next
        print(f"Dequeue: {removed}")

stack = Stack()
stack.push(10)
stack.push(20)
stack.pop()

queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.dequeue()
