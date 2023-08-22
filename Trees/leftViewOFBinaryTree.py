class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def left_view_util(root, level, max_level, result):
    if root is None:
        return
    
    if level > max_level[0]:
        result.append(root.data)
        max_level[0] = level

    left_view_util(root.left, level + 1, max_level, result)
    left_view_util(root.right, level + 1, max_level, result)

def left_view(root):
    result = []
    max_level = [0]  # Use a list to keep track of the maximum level visited
    left_view_util(root, 1, max_level, result)
    return result

# Example tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

left_view_nodes = left_view(root)
print("Left view of the tree:", left_view_nodes)
