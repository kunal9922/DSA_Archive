class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SelfOrganizingLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def transpose(self, data):
        if not self.head:
            return

        # If the accessed element is the head, nothing to transpose
        if self.head.data == data:
            return

        prev = None
        current = self.head

        # Find the node with the given data
        while current and current.data != data:
            prev = current
            current = current.next

        # If the data was not found, do nothing
        if not current:
            return

        # Transpose the current node with the previous one
        if prev:
            prev.data, current.data = current.data, prev.data
        else:
            # If the accessed element is the first element, make it the new head
            self.head = current.next

# Example usage:
if __name__ == "__main__":
    sol = SelfOrganizingLinkedList()
    sol.append(1)
    sol.append(2)
    sol.append(3)
    sol.append(4)

    print("Original List:")
    sol.display()

    # Accessing an element triggers the Transpose method
    sol.transpose(3)
    print("List after accessing 3:")
    sol.display()
