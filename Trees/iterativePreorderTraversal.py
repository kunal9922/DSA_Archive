class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
class BinaryTree:
    def iterativePreOrder(self, root: Node):
        if not root:
            return None
        stack = [root] # Push the root into the stack
        while stack:
            currNode = stack.pop()
            print(currNode.data)
            # Push right child first
            if currNode.right:
                stack.append(currNode.right)
            # Push left child second
            if currNode.left:
                stack.append(currNode.left)          

    def iterativeInOrder(self, root: Node):
        if not root:
            return None
        stack = [] # Initialize an empty stack
        currNode = root
        while stack or currNode:
            # Go to the leftmost node and push all the nodes along the way
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            # Pop the top of the stack and print its data
            currNode = stack.pop()
            print(currNode.data)
            # Move to the right child if it exists
            currNode = currNode.right

    def iterativePostOrder(self, root):
        if not root:
            return None
        # using two stacks
        s1 = [root]
        s2 = []
        while s1:
            currNode = s1.pop()
            s2.append(currNode)
            if currNode.left:
                s1.append(currNode.left)
            if currNode.right:
                s1.append(currNode.right)
        
        while s2:
            print(s2.pop().data)
# Example tree:
#       10
#     /   \
#    8     2
#   / \   / \
#  3   5 6   20
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(20)

t = BinaryTree()
print("Pre Order Tree Traversal")
t.iterativePreOrder(root)
print("In Order Tree Traversal")
t.iterativeInOrder(root)
print("Post Order Tree Traversal")
t.iterativePostOrder(root)