
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
def isIdentical(x, y):
 
    if x is None and y is None:
        return True
 
   
    return (x is not None and y is not None) and (x.key == y.key) and \
        isIdentical(x.left, y.left) and isIdentical(x.right, y.right)
 
 
if __name__ == '__main__':
 
   #First Binary Tree
    x = Node(22)
    x.left = Node(12)
    x.right = Node(16)
    x.left.left = Node(6)
    x.left.right = Node(12)
    x.right.left = Node(18)
    x.right.right = Node(25)
 
    #Second Binary Tree
    y = Node(22)
    y.left = Node(12)
    y.right = Node(16)
    y.left.left = Node(6)
    y.left.right = Node(12)
    y.right.left = Node(18)
    y.right.right = Node(25)
 
    if isIdentical(x, y):
        print('The given binary trees are identical')
    else:
        print('The given binary trees are not identical')