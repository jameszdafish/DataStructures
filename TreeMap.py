from MyMap import *


class TreeNode:
    def __init__(self, key, value, right=None, left=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left


class TreeMap(MyMap):
    def __init__(self):
        self.head = None
        self.length = 0
        self.list = []

    # Helper of put()
    def put_recursively_helper(self, key, value, current_treenode):
        if current_treenode is None:
            self.head = TreeNode(key, value)
            self.length += 1
            return value
        elif key == current_treenode.key and current_treenode.value != value:
            current_treenode.value = value
            return value
        elif key == current_treenode.key:
            return value
        elif key > current_treenode.key:
            if current_treenode.right is None:
                current_treenode.right = TreeNode(key, value)
                self.length += 1
                return value
            current_treenode = current_treenode.right
        elif key < current_treenode.key:
            if current_treenode.left is None:
                current_treenode.left = TreeNode(key, value)
                self.length += 1
                return value
            current_treenode = current_treenode.left
        return self.put_recursively_helper(key, value, current_treenode)

    # Puts key-value pair in TreeMap
    def put(self, key, value):
        return self.put_recursively_helper(key, value, self.head)

    # Remove Helper Method
    def find_rightmost_child(self, current_node, removal_node):
        if current_node.right is not None:
            current_node.right = self.find_rightmost_child(current_node.right, removal_node)
            return current_node
        else:
            removal_node.key = current_node.key
            removal_node.value = current_node.value
            return current_node.left

    # Remove Helper Method
    def remove_head(self, current_node):
        if current_node.left is None:
            return current_node.right
        else:
            current_node.left = self.find_rightmost_child(current_node.left, current_node)
            return current_node

    # Remove Helper Method
    def remove_node(self, key, current_node):
        if current_node is None:
            return None
        if key > current_node.key:
            current_node.right = self.remove_node(key, current_node.right)
            return current_node
        elif key < current_node.key:
            current_node.left = self.remove_node(key, current_node.left)
            return current_node
        else:
            self.length -= 1
            return self.remove_head(current_node)

    # Remove Method
    def remove(self, key):
        self.head = self.remove_node(key, self.head)
        return key

    # Get Helper Method
    def get_recursively_helper(self, key, current_node):
        if current_node is None:
            return None
        elif key == current_node.key:
            return current_node.value
        elif key > current_node.key:
            current_node = current_node.right
        elif key < current_node.key:
            current_node = current_node.left
        return self.get_recursively_helper(key, current_node)

    # Returns the value found at key, returns none if it's not found
    def get(self, key):
        return self.get_recursively_helper(key, self.head)

    # Checks TreeSet if key is present, returns Boolean T/F
    def contains_key(self, key):
        # Use Get Method to find value, if key does not exist, value_of_key is None
        value_of_key = self.get(key)
        return value_of_key is not None

    # Returns the number of items stored in the TreeSet
    def size(self):
        return self.length

    # Checks if TreeSet is empty, returns Boolean T/F
    def is_empty(self):
        return self.head is None

    # Print Method In Order
    def inorder_traversal(self):
        self.list = []
        self.inorder_traversal_helper(self.head)
        return self.list

    # In Order Helper Method
    def inorder_traversal_helper(self, current_node):
        if current_node:
            self.inorder_traversal_helper(current_node.left)
            self.list.append((current_node.key, current_node.value))
            self.inorder_traversal_helper(current_node.right)

    # Print Method Pre Order
    def preorder_traversal(self):
        self.list = []
        self.preorder_traversal_helper(self.head)
        return self.list

    # Pre Order Helper Method
    def preorder_traversal_helper(self, current_node):
        if current_node:
            self.list.append((current_node.key, current_node.value))
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
            self.list.append((current_node.key, current_node.value))

    def __str__(self):
        return str(self.inorder_traversal())
