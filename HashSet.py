from TreeSet import *
from MySet import *


class HashSet(MySet):
    def __init__(self, length=1000):
        self.hashset = []
        self.length = length

        # size will be 0 if empty
        self.size_of_hashset = 0

        # HashSet array list empty positions creation
        for i in range(length):
            self.hashset.append(None)

    def __str__(self):
        objects_in_hashset = ""
        for index in range(self.length):
            if self.hashset[index] is not None:
                objects_in_hashset += "Index: " + str(index) + ", TreeSet: " + str(self.hashset[index]) + "\n"
        return objects_in_hashset

    def mod_to_find_index(self, data):
        return hash(data) % self.length

    def add(self, data):
        index = self.mod_to_find_index(data)

        # If spot is empty, create TreeSet and add data
        if self.hashset[index] is None:
            new_treeset = TreeSet()
            new_treeset.add(data)
            self.hashset[index] = new_treeset

        # Checks if index already contains value
        elif self.hashset[index].contains(data) is True:
            return data

        # Collision, data is added to TreeSet
        else:
            self.hashset[index].add(data)
        self.size_of_hashset += 1
        return data

    def remove(self, data):
        index = self.mod_to_find_index(data)

        # HashSet checks the TreeSet if the value is present, removes if present
        if self.hashset[index] is not None and self.hashset[index].contains(data) is True:
            self.hashset[index].remove(data)
            self.size_of_hashset -= 1

        return data

    def contains(self, data):
        index = self.mod_to_find_index(data)

        # HashSet does not contain the value
        if self.hashset[index] is None:
            return False

        # HashSet checks the TreeSet if the value is present
        else:
            return self.hashset[index].contains(data)

    def is_empty(self):
        return self.size_of_hashset == 0

    def size(self):
        return self.size_of_hashset
