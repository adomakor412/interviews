"""
File: linkedbag.py
Author: Ken Lambert
"""

from node import Node
from abstractdict import AbstractDict, Entry

class LinkedDict(AbstractDict):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, keys = None, values = None):
        """Will copy entries to the dictionary
        from keys and values if they are present."""
        # Include a reference to previous node for popping
        self.items = self.previousNode = None
        AbstractDict.__init__(self, keys, values)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while not cursor is None:
            yield cursor.data.key
            cursor = cursor.next

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self.getIndex(key)
        if index is None: raise KeyError("Missing: " + str(key))
        return index.data.value

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None

    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        index = self.getIndex(key)
        if index is None:
            self.items = Node(Entry(key, value), self.items)
            self.size += 1
        else:
            index.data.value = value

    def pop(self, key):
        """Removes the key and returns the associated value 
        if the key is in the dictionary,
        or returns the default value otherwise."""
        index = self.getIndex(key)
        if index is None: return defaultValue
        self.size -= 1
        # Two cases: either at the head or thereafter.
        if self.previousNode is None:
            self.items = self.items.next
        else:
            self.previousNode.next = index.next
        return index.data.value

    def getIndex(self, key):
        """Helper method for key search."""
        # Tracks the node before the node containing the key
        self.previousNode = None
        index = self.items
        while index != None:
            if index.data.key == key:
                return index
            self.previousNode = index
            index = index.next
        return None       
        
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
    
# Include your dictionary type as an argument to main
if __name__ == "__main__":
    main(LinkedDict)

