
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)  


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)  
print("Top:", stack.peek())  
print("Pop:", stack.pop())    
print("Stack:", stack.items) 
print("Is Empty:", stack.is_empty())  
print("Size:", stack.size())  
