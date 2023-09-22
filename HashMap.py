from TreeMap import *
from MyMap import *


class HashMap(MyMap):
    def __init__(self, length=1000):
        self.hashmap = []
        self.length = length
        self.size_of_hashmap = 0

        for i in range(length):
            self.hashmap.append(None)

    # Finds hash value of key
    def mod_then_hash_key(self, key):
        hashed_key = hash(key)
        modded_hashed_key = hashed_key % self.length
        return modded_hashed_key

    # Adds a key-value pair to the hashmap. If the key already exists, it updates the associated value.
    def put(self, key, value):
        modded_hashed_key = self.mod_then_hash_key(key)
        if self.hashmap[modded_hashed_key] is None:
            new_treemap = TreeMap()
            new_treemap.put(key, value)
            self.hashmap[modded_hashed_key] = new_treemap
            self.size_of_hashmap += 1
        elif self.hashmap[modded_hashed_key].contains_key(key) and self.hashmap[modded_hashed_key].get(key) == value:
            return value
        elif self.hashmap[modded_hashed_key].contains_key(key) and self.hashmap[modded_hashed_key].get(key) != value:
            self.hashmap[modded_hashed_key].put(key, value)  # updates key-value pair
        else:
            self.hashmap[modded_hashed_key].put(key, value)  # adds key-value pair
            self.size_of_hashmap += 1
        return value

    # Removes a key-value pair from the hashmap based on the given key. If not found, returns None.
    def remove(self, key):
        modded_hashed_key = self.mod_then_hash_key(key)
        if self.hashmap[modded_hashed_key] is None or not self.hashmap[modded_hashed_key].contains_key(key):
            return None
        elif self.hashmap[modded_hashed_key].contains_key(key):
            self.hashmap[modded_hashed_key].remove(key)
            self.size_of_hashmap -= 1
            return key

    # get(key): This method retrieves the value associated with a given key. If not found, returns None.
    def get(self, key):
        modded_hashed_key = self.mod_then_hash_key(key)
        if self.hashmap[modded_hashed_key] is None:
            return None
        elif self.hashmap[modded_hashed_key].contains_key(key):
            return self.hashmap[modded_hashed_key].get(key)

    # Checks if a key is present in the hashmap and returns a Boolean.
    def contains_key(self, key):
        modded_hashed_key = self.mod_then_hash_key(key)
        if self.hashmap[modded_hashed_key] is None:
            return False
        elif self.hashmap[modded_hashed_key].contains_key(key):
            return True
        return False

    # Returns the number of key-value pairs currently stored in the hashmap.
    def size(self):
        return self.size_of_hashmap

    # Returns Boolean based on if it is empty or not.
    def is_empty(self):
        return self.size_of_hashmap == 0

    def __str__(self):
        objects_in_hashmap = ""
        for index in range(self.length):
            if self.hashmap[index] is not None:
                objects_in_hashmap += f"Index: {index}, TreeMap: {self.hashmap[index].__str__()}\n"
        return objects_in_hashmap
