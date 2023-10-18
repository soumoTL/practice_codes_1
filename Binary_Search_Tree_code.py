#Creating a Node
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
#Inorder traversal     
def inordertranversal(root):
    if root is not None:
        inordertranversal(root.left)

        print(str(root.key), end = " ")
        
        inordertranversal(root.right)
        
#Inserting a Node
def insert(node, key):
    
    #Return a new node if the tree is empty
    if node is None:
        return node(key)
    
    if key <  node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        
    return node

#Finding the inorder successor
def minValueNode(node):
    current = node
    
    #Finding the leftmost node 
    while(current.left is not None):
        current=current.left
    return current

#Deleting a Node 


        
        


        