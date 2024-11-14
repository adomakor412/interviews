"""
File: hashdict.py
Author: Ken Lambert
"""

from abstractdict import AbstractDict, Entry
from node import Node
from arrays import Array

class HashDict(AbstractDict):
    """Represents a hash-based dictionary."""

    DEFAULT_CAPACITY = 9

    def __init__(self, keys = None, values = None,
                 capacity = None):
        """Will copy entries to the dictionary
        from keys and values if they are present."""
        if capacity is None:
            self.capacity = HashDict.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        self.array = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def __contains__(self, key):
        """Returns True if key is in self or False otherwise."""
        self.index = abs(hash(key)) % len(self.array)
        self.priorNode = None
        self.foundNode = self.array[self.index]
        while self.foundNode != None:
            if self.foundNode.data.key == key: 
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        # Exercise

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        if not key in self: raise KeyError("Missing: " + str(key))
        return self.foundNode.data.value

    # Mutators
        def clear(self):
        """Makes self become empty."""
        # Exercise

    def __setitem__(self, key, value):
        """If the key is in the dictionary,
        replaces the old value with the new value.
        Othwerise, adds the key and value to it."""
        if key in self: 
            self.foundNode.data.value = value
        else:
            newNode = Node(Entry(key, value), self.array[self.index])
            self.array[self.index] = newNode
            self.size += 1

    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value 
        if the key is in the dictionary,
        or returns the default value otherwise."""
        # Exercise

def main(dictionaryType):
    d = dictionaryType()
    for key in range(1, 6):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    aClone = dictionaryType(d.keys(), d.values())
    print("\nA clone:", aClone)
    print("\nThe keys:", set(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nKey Value (using [])")
    for key in d:
        print(key, " ", d[key])
    print("\nDelete all keys:")
    for key in range(1, 6):
        print(d.pop(key))
    print("\nLength: ", len(d))
    newD = dictionaryType([7, 2, 8], [8, 3, 9])
    print("\nA clone:", aClone)
    print("\nA second dictionary:", newD)
    print("\nA Concatenate a clone and second:", aClone + newD)

    
if __name__ == "__main__":
    main(HashDict)

