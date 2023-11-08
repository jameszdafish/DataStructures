class Node:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous = previous_node
        self.next = next_node


# DLL is "Doubly Linked List"
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        print_string = ""
        current_node = self.head
        while current_node is not None:
            print_string += f"{current_node.data}, "
            current_node = current_node.next
        return print_string

    # adds data to the index of DLL
    def insert(self, index, data):
        # account for end cases
        if index < 0 or index > self.length:
            return

        # new index 0
        elif index == 0:
            self.appendleft(data)

        # insert behind tail
        elif index == self.length:
            self.append(data)

        # between new head and new tail
        else:
            current_node_index = 0
            current_node = self.head
            while current_node_index < index:
                if current_node_index == index - 1:
                    # assign previous attributes of each nodes
                    current_node.next.previous = Node(data)
                    current_node.next.previous.previous = current_node

                    # save node so we can assign next attributes of each nodes
                    saved_node = current_node.next
                    current_node.next = current_node.next.previous
                    current_node.next.next = saved_node
                    return data

                current_node = current_node.next
                current_node_index += 1

    # adds data to the rear of DLL
    def append(self, data):
        # length = 0
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        # length > 0
        else:
            self.tail.next = Node(data)  # set next (after tail)
            self.tail.next.previous = self.tail  # set previous
            self.tail = self.tail.next  # reassign tail
        self.length += 1
        return data

    # adds data to the front of DLL
    def appendleft(self, data):
        # length = 0
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        # length > 0
        else:
            self.head.previous = Node(data)  # set previous (before head)
            self.head.previous.next = self.head  # set next
            self.head = self.head.previous  # reassign head
        self.length += 1
        return data

    # adds more than one data to the rear of DLL
    def extend(self, *multiple_data):
        for data in multiple_data:
            self.append(data)
            self.length += 1
        return multiple_data

    # adds more than one data to the front of DLL
    def extendleft(self, *multiple_data):
        for data in multiple_data:
            self.appendleft(data)
            self.length += 1
        return multiple_data

    # deletes the data from the index
    def delete(self, index):
        # account for end cases
        if index > self.length - 1 or index < 0:
            return

        # delete head
        elif index == 0:
            return self.popleft

        # delete tail
        elif index == self.length - 1:
            return self.pop

        # delete index between the head and tail
        else:
            current_node_index = 0
            current_node = self.head
            while current_node_index < index:
                # replaces deletion node using the previous and next nodes of the deletion node
                if current_node_index == index - 1:
                    data = current_node.next.data
                    current_node.next.next.previous = current_node
                    current_node.next = current_node.next.next
                    return data

                # iterates until we current_node is before the deletion node
                current_node = current_node.next
                current_node_index += 1

    # deletes the data from the rear of DLL
    def pop(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            data = self.tail.data
            self.head, self.tail = None, None
            self.length -= 1
            return data
        else:
            data = self.tail.data
            self.tail.previous.next = None
            self.tail = self.tail.previous
            self.length -= 1
            return data

    # deletes the data from the front of DLL
    def popleft(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            data = self.head.data
            self.head, self.tail = None, None
            self.length -= 1
            return data
        else:
            data = self.head.data
            self.head.next.previous = None
            self.head = self.head.next
            self.length -= 1
            return data

    # checks if DLL is empty
    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    # reorders DLL by "rotating" indices forwards(+) or backwards(-)
    def rotate(self, n=1):
        # check for end-case
        if n == 0:
            return

        # connect head and tail, so we can cut the chain of nodes elsewhere to create a new "head" and "tail"
        self.head.previous = self.tail
        self.tail.next = self.head

        # depending on direction of rotation, we change head and tail
        if n > 0:
            # move head and tail one node at a time for "n" times
            for repitition in range(n):
                # set head as tail
                self.head = self.tail
                # set tail as previous node
                self.tail = self.tail.previous
        elif n < 0:
            # adding the length of the deque and the negative n value is going to see how far head and tail move
            number_of_node_moves = n + self.length

            # move head and tail one node at a time for "number_of_node_moves" times
            for repitition in range(number_of_node_moves):
                # set head as tail
                self.head = self.tail
                # set tail as previous node
                self.tail = self.tail.previous

        # "cut" the head and tail from each other
        self.head.previous = None
        self.tail.next = None

    # flips the order of the DLL
    def reverse(self):
        # Create a pointer
        current_node = self.tail

        # Create a new node list based on the current nodes
        new_node = Node(self.tail.data)
        self.head = new_node
        for node in range(self.length - 1):
            current_node = current_node.previous
            new_node.next = Node(current_node.data)
            new_node.next.previous = new_node
            new_node = new_node.next

            if current_node.previous is None:
                self.tail = new_node

    # traverse the list from the front to the back
    def iterateForward(self):
        self.list = []
        self.iterateForwardHelper(self.head)
        return self.list

    # helper for iterateForward
    def iterateForwardHelper(self, current_node):
        if current_node:
            self.list.append(current_node.data)
            current_node = current_node.next
            return self.iterateForwardHelper(current_node)

    # traverse the list from the back to the front
    def iterateBackward(self):
        self.list = []
        self.iterateBackwardHelper(self.tail)
        return self.list

    # helper for iterateForward
    def iterateBackwardHelper(self, current_node):
        if current_node:
            self.list.append(current_node.data)
            current_node = current_node.previous
            return self.iterateBackwardHelper(current_node)
