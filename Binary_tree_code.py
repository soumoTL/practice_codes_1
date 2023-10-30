class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        

    def traversepreorder(self):
        print(self.val, end = " ")
        if self.left:
            self.left.traversepreorder()
        if self.right:
            self.right.traversepreorder()
        

    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.val, end = " ")
        if self.right:
            self.right.traverseinorder()
        
    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()
        if self.right:
            self.right.traversepostorder()
        print(self.val, end = " ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre Order traversal", end = " ")
root.traversepreorder()
print("\nIn Order traversal", end = " ")
root.traverseinorder()
print("\nPost Order traversal", end = " ")
root.traversepostorder()

     