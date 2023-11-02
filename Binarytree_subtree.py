class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_subtree(tree, subtree):
    if not subtree:
        return True
    if not tree:
        return False

    if is_identical(tree, subtree):
        return True

    return is_subtree(tree.left, subtree) or is_subtree(tree.right, subtree)

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.value == root2.value) and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)


subtree = TreeNode(2)
subtree.left = TreeNode(4)
subtree.right = TreeNode(5)

if is_subtree(tree, subtree):
    print("The 'subtree' is a subtree of the 'tree'.")
else:
    print("The 'subtree' is not a subtree of the 'tree'.")
