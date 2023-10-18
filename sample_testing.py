class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def size(self):
        return len(self.items)
    

new_Queue = Queue()

#Adding elements in the Queue
new_Queue.enqueue("A")
new_Queue.enqueue("B")
new_Queue.enqueue("C")
new_Queue.enqueue("D")


#Removing elements from the Queue
print(new_Queue.dequeue())
print(new_Queue.dequeue())

print(new_Queue.is_empty())

print(new_Queue.size())