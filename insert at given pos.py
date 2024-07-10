class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position.")
            return
        if position == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Position out of range.")
                return
            current_node = current_node.next
        if current_node is None:
            print("Position out of range.")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.print_list()

    # Inserting element 3 at position 2
    ll.insert_at_position(3, 2)
    ll.print_list()
