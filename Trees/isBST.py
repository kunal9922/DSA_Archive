class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def isBSTUtil(root, prev):
    # Base case: Empty tree is a BST
    if root is None:
        return True

    # Recur on the left subtree
    if not isBSTUtil(root.left, prev):
        return False

    # Check if current node's value is greater than previous node's value
    if root.data <= prev[0]:
        return False

    # Update the previous node's value
    prev[0] = root.data

    # Recur on the right subtree
    return isBSTUtil(root.right, prev)

def isBST(root):
    prev = [float('-inf')]  # Use a list to maintain the previous value
    return isBSTUtil(root, prev)

# Example tree:
#       3
#      / \
#     1   5
#    / \   \
#   0   2   4
root = Node(3)
root.left = Node(1)
root.right = Node(5)
root.right.right = Node(4)
root.left.left = Node(0)
root.left.right = Node(2)

if isBST(root):
    print("The tree is a Binary Search Tree.")
else:
    print("The tree is not a Binary Search Tree.")
