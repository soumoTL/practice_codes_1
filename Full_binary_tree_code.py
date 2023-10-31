class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_full_binary_tree(root):
    if root is None:
        return True  # An empty tree is considered a full binary tree

    # If a node has no children, it's still a full binary tree
    if root.left is None and root.right is None:
        return True

    # If a node has one child but not both, it's not a full binary tree
    if root.left is None or root.right is None:
        return False

    # Recursively check the left and right subtrees
    return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)

# Create a full binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Check if it's a full binary tree
if is_full_binary_tree(root):
    print("It's a full binary tree.")
else:
    print("It's not a full binary tree.")
