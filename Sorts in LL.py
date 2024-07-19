class Node:
    def __init__(self, data):
        # Initialize a node with data and the next pointer set to None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with the head set to None
        self.head = None

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the linked list is empty, set the head to the new node
        if self.head is None:
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # Append the new node at the end of the list
        last_node.next = new_node

    def prepend(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Set the new node's next pointer to the current head
        new_node.next = self.head
        # Update the head to the new node
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head
        # If the head node contains the key, update the head and delete the node
        if current_node and current_node.data == key:
            self.head = current_node.next 
            current_node = None
            return
        prev = None
        # Traverse the list to find the node to be deleted
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        # If the key is not found, do nothing
        if current_node is None:
            return
        # Unlink the node from the list
        prev.next = current_node.next
        current_node = None

    def print_list(self):
        # Traverse the list and print each node's data
        current_node = self.head
        while current_node:
            print(current_node.data, end='->')
            current_node = current_node.next
        print("None")

    def bubble_sort(self):
        end = None
        while end != self.head:
            current = self.head
            while current.next != end:
                next_node = current.next
                if current.data > next_node.data:
                    # Swap the data
                    current.data, next_node.data = next_node.data, current.data
                current = next_node
            end = current

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, head_ref, new_node):
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            head_ref = new_node
        else:
            current = head_ref
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None
        left = LinkedList()
        right = LinkedList()
        left.head = self.head
        right.head = next_to_middle
        left.merge_sort()
        right.merge_sort()
        self.head = self.sorted_merge(left.head, right.head)

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def quick_sort(self):
        self.head = self.quick_sort_recur(self.head)

    def quick_sort_recur(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        lesser_head, equal_head, greater_head = self.partition(head, pivot)
        lesser_sorted = self.quick_sort_recur(lesser_head)
        greater_sorted = self.quick_sort_recur(greater_head)
        return self.concat(lesser_sorted, equal_head, greater_sorted)

    def partition(self, head, pivot):
        lesser_head = lesser_tail = Node(0)
        equal_head = equal_tail = Node(0)
        greater_head = greater_tail = Node(0)
        current = head
        while current:
            if current.data < pivot.data:
                lesser_tail.next = current
                lesser_tail = current
            elif current.data > pivot.data:
                greater_tail.next = current
                greater_tail = current
            else:
                equal_tail.next = current
                equal_tail = current
            current = current.next
        lesser_tail.next = equal_tail.next = greater_tail.next = None
        return lesser_head.next, equal_head.next, greater_head.next

    def concat(self, lesser, equal, greater):
        head = tail = Node(0)
        for part in [lesser, equal, greater]:
            while part:
                tail.next = part
                tail = part
                part = part.next
        return head.next

# Example usage:
llist = LinkedList()
llist.append(64)
llist.append(34)
llist.append(25)
llist.append(12)
llist.append(22)
llist.append(11)
llist.append(90)

print("Original list:")
llist.print_list()

print("Bubble Sort:")
llist.bubble_sort()
llist.print_list()

# Reset list for next sort
llist = LinkedList()
llist.append(64)
llist.append(34)
llist.append(25)
llist.append(12)
llist.append(22)
llist.append(11)
llist.append(90)

print("Insertion Sort:")
llist.insertion_sort()
llist.print_list()

# Reset list for next sort
llist = LinkedList()
llist.append(64)
llist.append(34)
llist.append(25)
llist.append(12)
llist.append(22)
llist.append(11)
llist.append(90)

print("Merge Sort:")
llist.merge_sort()
llist.print_list()

# Reset list for next sort
llist = LinkedList()
llist.append(64)
llist.append(34)
llist.append(25)
llist.append(12)
llist.append(22)
llist.append(11)
llist.append(90)

print("Quick Sort:")
llist.quick_sort()
llist.print_list()
