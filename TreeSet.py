from MySet import *


class TreeNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class TreeSet(MySet):
    def __init__(self):
        self.head = None
        self.length = 0
        self.list = []

    # Helper of add_recursively
    def add_recursively_helper(self, data, current_treenode):
        if current_treenode is None:
            self.head = TreeNode(data)
            self.length += 1
            return data
        elif data == current_treenode.data:
            return
        elif data > current_treenode.data:
            if current_treenode.right is None:
                current_treenode.right = TreeNode(data)
                self.length += 1
                return data
            current_treenode = current_treenode.right
        elif data < current_treenode.data:
            if current_treenode.left is None:
                current_treenode.left = TreeNode(data)
                self.length += 1
                return data
            current_treenode = current_treenode.left
        return self.add_recursively_helper(data, current_treenode)

    # Adds item to TreeSet, but recursively
    def add(self, data):
        return self.add_recursively_helper(data, self.head)

    # Remove Helper Method
    def find_rightmost_child(self, current_node, removal_node):
        if current_node.right is not None:
            current_node.right = self.find_rightmost_child(current_node.right, removal_node)
            return current_node
        else:
            removal_node.data = current_node.data
            return current_node.left

    # Remove Helper Method
    def remove_head(self, current_node):
        if current_node.left is None:
            return current_node.right
        else:
            current_node.left = self.find_rightmost_child(current_node.left, current_node)
            return current_node

    # Remove Helper Method
    def remove_node(self, data, current_node):
        if current_node is None:
            return None
        if data > current_node.data:
            current_node.right = self.remove_node(data, current_node.right)
            return current_node
        elif data < current_node.data:
            current_node.left = self.remove_node(data, current_node.left)
            return current_node
        else:
            self.length -= 1
            return self.remove_head(current_node)

    # Remove Method
    def remove(self, data):
        self.head = self.remove_node(data, self.head)
        return data

    # Checks TreeSet if data is present, returns Boolean T/F
    def contains(self, data):
        current_treenode = self.head
        while current_treenode is not None:
            if data > current_treenode.data:
                current_treenode = current_treenode.right
            elif data < current_treenode.data:
                current_treenode = current_treenode.left
            elif current_treenode.data == data:
                return True
        return False

    # Checks if TreeSet is empty, returns Boolean T/F
    def is_empty(self):
        return self.head is None

    # Returns the number of items stored in the TreeSet
    def size(self):
        return self.length

    # Print Method In Order
    def inorder_traversal(self):
        self.list = []
        self.inorder_traversal_helper(self.head)
        return self.list

    # In Order Helper Method
    def inorder_traversal_helper(self, current_node):
        if current_node:
            self.inorder_traversal_helper(current_node.left)
            self.list.append(current_node.data)
            self.inorder_traversal_helper(current_node.right)

    # Print Method Pre Order
    def preorder_traversal(self):
        self.list = []
        self.preorder_traversal_helper(self.head)
        return self.list

    # Pre Order Helper Method
    def preorder_traversal_helper(self, current_node):
        if current_node:
            self.list.append(current_node.data)
            self.preorder_traversal_helper(current_node.left)
            self.preorder_traversal_helper(current_node.right)

    # Print Method Post Order
    def postorder_traversal(self):
        self.list = []
        self.postorder_traversal_helper(self.head)
        return self.list

    # Post Order Helper Method
    def postorder_traversal_helper(self, current_node):
        if current_node:
            self.postorder_traversal_helper(current_node.left)
            self.postorder_traversal_helper(current_node.right)
            self.list.append(current_node.data)

    def __str__(self):
        return str(self.inorder_traversal())
