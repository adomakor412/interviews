"""
File: arraydict.py
Author: Ken Lambert
"""

from abstractdict import AbstractDict, Entry

class ArrayDict(AbstractDict):
    """Represents an array-based dictionary."""

    def __init__(self,  keys = None, values = None):
        """Will copy entries to the dictionary
        from keys and values if they are present."""
        self.items = list()
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def __iter__(self):
        """Serves up the keys in the dictionary."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor].key
            cursor += 1    

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self.getIndex(key)
        if index == -1: raise KeyError("Missing: " + str(key))
        return self.items[index].value

    # Mutators
    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        index = self.getIndex(key)
        if index == -1:
            self.items.append(Entry(key, value))
            self.size += 1
        else:
            self.items[index].value = value

    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value 
        if the key is in the dictionary,
        or returns the default value otherwise."""
        index = self.getIndex(key)
        if index == -1: return defaultValue
        self.size -= 1
        return self.items.pop(index).value

    def getIndex(self, key):
        """Helper method for key search."""
        index = 0
        for entry in self.items:
            if entry.key == key:
                return index
            index += 1
        return -1       

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
    main(ArrayDict)

