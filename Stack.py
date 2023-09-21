from LinkedList import *


class JamesStack:
    def __init__(self):
        self.linked_list_object = LinkedList()

    # Adds the data to the top of the Stack Project
    def push(self, data):
        self.linked_list_object.insert(0, data)
        return data

    # Returns the data at the top of the stack
    def peek(self):
        return self.linked_list_object.get(0)

    # Removes the data at the top of the stack and returns that data
    def pop(self):
        removed_item = self.peek()
        self.linked_list_object.remove(0)
        return removed_item

    # Returns true if there is any data in the stack, false otherwise
    def is_empty(self):
        return self.linked_list_object.is_empty()

    # Returns how many data points are in ze stack
    def size(self):
        return self.linked_list_object.size()
