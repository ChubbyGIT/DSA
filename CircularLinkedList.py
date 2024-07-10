class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node

    def delete_node(self, key):
        if self.head.data == key:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            if self.head == self.head.next:
                self.head = None
            else:
                current_node.next = self.head.next
                self.head = self.head.next
        else:
            current_node = self.head
            prev = None
            while current_node.next != self.head:
                prev = current_node
                current_node = current_node.next
                if current_node.data == key:
                    prev.next = current_node.next
                    current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()

# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.prepend(0)
    cll.print_list()

    # Deleting node with data value 2
    cll.delete_node(2)
    cll.print_list()
