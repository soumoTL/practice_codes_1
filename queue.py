class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def front(self):
        if not self.is_empty():
            return self.items[0]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Queue", queue.items)
print("Front", queue.front())
print("dequeue", queue.dequeue())
print("Queue", queue.items)
print("Is Empty", queue.is_empty())
print("Size", queue.size())
