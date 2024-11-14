"""
File: ermodel.py
Author: Ken Lambert

Defines the classes ERModel, Patient, and Condition for an
emergency room scheduler.
"""

from linkedpriorityqueue import LinkedPriorityQueue

class Condition(object):
    """Represents a condition."""

    def __init__(self, rank):
        self.rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __str__(self):
        """Returns the string rep of a condition."""
        if   self.rank == 1: return "critical"
        elif self.rank == 2: return "serious"
        else:                return "fair"

class Patient(object):
    """Represents a patient with a name and a condition."""

    def __init__(self, name, condition):
        self.name = name
        self.condition = condition

    def __eq__(self, other):
        return self.condition == other.condition

    def __lt__(self, other):
        return self._ondition < other.condition

    def __le__(self, other):
        return self.condition <= other.condition

    def __str__(self):
        """Returns the string rep of a patient."""
        return self.name + " / " + str(self.condition)

class ERModel(object):
    """Model of a scheduler."""

    def __init__(self):
        pass

    def isEmpty(self):
        """Returns True if there are patients in the model
        or False otherwise."""
        return True

    def schedule(self, p):
        """Adds a patient to the schedule."""
        pass

    def treatNext(self):
        """Returns the patient treated or None if there are none."""
        return None
