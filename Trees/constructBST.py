class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def buildBST(root: Node, val):
    if root is None:
        return Node(val)
    elif val <= root.data:
        root.left = buildBST(root.left, val)
    else:
        root.right = buildBST(root.right, val)
    
    return root

