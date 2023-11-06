class Node:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous = previous_node
        self.next = next_node


class Deque:
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

    # adds data to the rear of queue
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

    # adds data to the front of queue
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

    # adds more than one data to the rear of queue
    def extend(self, *multiple_data):
        for data in multiple_data:
            self.append(data)
            self.length += 1
        return multiple_data

    # adds more than one data to the front of queue
    def extendleft(self, *multiple_data):
        for data in multiple_data:
            self.appendleft(data)
            self.length += 1
        return multiple_data

    # deletes the data from the rear of queue
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

    # deletes the data from the front of queue
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

    # reorders queue by "rotating" indices forwards(+) or backwards(-)
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

    # flips the order of the queue
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


mydeque = Deque()
# mydeque.append("0")
# mydeque.appendleft("1")
# mydeque.append("2")
# mydeque.appendleft("3")
# mydeque.extend("5", "6", "7")
# mydeque.extendleft("5", "6", "7")
# mydeque.pop()
# mydeque.popleft()
mydeque.append(1)
mydeque.append(2)
mydeque.append(3)
mydeque.append(4)
mydeque.append(5)
mydeque.append(6)
mydeque.append(7)
mydeque.append(8)
print(mydeque.__str__())
mydeque.reverse()
print(mydeque.__str__())
print(mydeque.tail.data)
