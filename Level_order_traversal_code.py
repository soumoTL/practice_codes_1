class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
def printLevel(root, level):
 
    
    if root is None:
        return False
 
    if level == 1:
        print(root.key, end=' ')
 
        return True
 
    left = printLevel(root.left, level - 1)
    right = printLevel(root.right, level - 1)
 
    return left or right
 
 
def levelOrderTraversal(root):
 
    level = 1
 
    while printLevel(root, level):
        level = level + 1
 
 
if __name__ == '__main__':
 
    root = Node(20)
    root.left = Node(11)
    root.right = Node(20)
    root.left.left = Node(9)
    root.left.right = Node(12)
    root.right.left = Node(18)
    root.right.right = Node(25)
 
    levelOrderTraversal(root)
 
