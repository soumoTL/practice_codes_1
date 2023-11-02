class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_full_binary_tree(preorder, postorder):
    if not preorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)

    if len(preorder) == 1:
        return root

    left_subtree_root_value = preorder[1]

    index = postorder.index(left_subtree_root_value)

    root.left = construct_full_binary_tree(preorder[1:index + 2], postorder[:index + 1])
    root.right = construct_full_binary_tree(preorder[index + 2:], postorder[index + 1:-1])

    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

root = construct_full_binary_tree(preorder, postorder)
print("In-Order Traversal of Constructed Tree:")
in_order_traversal(root)
