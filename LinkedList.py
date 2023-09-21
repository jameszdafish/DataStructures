class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class JamesLinkedList:

    # creating the linked list by defining the instance variables
    def __init__(self):
        self.head = None
        self.length = 0
        self.last_node = None

    # displays string
    def __str__(self):
        if self.head is None:
            return "There are no stored nodes"
        x = self.head
        string_that_holds_all_node_data = ""
        string_that_holds_all_node_data += f"{x.data}"
        for i in range(self.length - 1):
            x = x.next
            if x == self.last_node:
                string_that_holds_all_node_data += f", and {x.data}"
            elif x != self.last_node:
                string_that_holds_all_node_data += f", {x.data}"

        return f"All the data in the linked list: {string_that_holds_all_node_data}"

    def get_node(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    # adds items to specific index while keeping the previous numbers too
    def insert(self, index, data):
        if index == self.length:
            self.append(data)
        elif index == 0:
            placeholder_node = self.head
            self.head = Node(data)
            self.head.next = placeholder_node
        elif 0 < index < self.length:
            previous_node = self.get_node(index - 1)
            previous_node.next = Node(data, previous_node.next)
        self.length += 1

    # adds item to end of list
    def append(self, data):
        if self.length == 0:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
        self.length += 1

    # removes item from specific index
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.last_node = None
        elif 0 < index < self.length:
            select_remove = self.get_node(index - 1)
            select_remove.next = select_remove.next.next
            self.length -= 1

            if index == self.length:
                self.last_node = select_remove

    # returns item data from index number
    def get(self, index):
        if index >= self.length:
            return

        return self.get_node(index).data

    # returns how many items are in list
    def size(self):
        return self.length

    # checks whether the list is empty
    def is_empty(self):
        return self.length == 0

    # checks whether the list contains this data
    def contains(self, data):
        checker = self.head
        for i in range(self.length):
            if checker.data == data:
                return True
            checker = checker.next
        return False

    # removes all occurrences of item from the list
    def remove_all(self, data):
        while self.head is not None and self.head.data == data:
            self.head = self.head.next
            self.length -= 1

        current_node = self.head
        for i in range(self.length - 1):
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                current_node = current_node.next

        self.last_node = current_node
