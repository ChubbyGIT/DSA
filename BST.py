class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    @staticmethod
    def build_tree(elements):
        print(elements)
        root = BinarySearchTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


# Example usage
numbers_tree = BinarySearchTreeNode.build_tree([17, 4, 1, 20, 9, 23, 18, 34])

print("In-order traversal:", numbers_tree.in_order_traversal())
print("Pre-order traversal:", numbers_tree.pre_order_traversal())
print("Post-order traversal:", numbers_tree.post_order_traversal())

print()
numbers_tree = numbers_tree.delete(17)
print("After deleting 17 (in-order):", numbers_tree.in_order_traversal())
print("After deleting 17 (pre-order):", numbers_tree.pre_order_traversal())
print("After deleting 17 (post-order):", numbers_tree.post_order_traversal())

numbers_tree.add_child(17)
print()
print("In-order traversal after adding 17:", numbers_tree.in_order_traversal())
print("Pre-order traversal after adding 17:", numbers_tree.pre_order_traversal())
print("Post-order traversal after adding 17:", numbers_tree.post_order_traversal())
