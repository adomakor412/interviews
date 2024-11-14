"""
File: treesortedset.py

A tree-based sorted set implementation.
"""

from linkedbst import LinkedBST
from abstractset import AbstractSet

class TreeSortedSet(AbstractSet):
    """An tree-based sorted set implementation."""

    def __init__(self, sourceCollection = None):
        self.items = LinkedBST(sourceCollection)

    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        return item in self.items

    def __iter__(self):
        """Supports an inorder traversal on a view of self."""
        return self.items.inorder()

    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if not item in self:
            self.items.add(item)

    # Remaining methods are exercises
